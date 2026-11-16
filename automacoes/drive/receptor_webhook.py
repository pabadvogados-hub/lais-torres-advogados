# -*- coding: utf-8 -*-
"""Receptor do webhook do Infinitum na VPS (so biblioteca padrao do Python, sem framework).

O QUE ELE FAZ
  1. Recebe POST /infinitum?token=<WEBHOOK_SEGREDO> (sem o token certo: 403).
  2. Grava o payload cru em dados/escritorio.db (webhook_eventos) e em
     dados/conversas/webhook_AAAA-MM.jsonl  -> isso e TAMBEM o arquivo das conversas que o
     Infinitum mandar por webhook (entra no backup semanal).
  3. Acha o card (card_id em qualquer nivel do payload), le os campos do card pela API publica e,
     se houver um link de arquivo, chama documento_whatsapp.arquivar() (Drive + tarefa ADVBOX).

DEPENDE DO INFINITUM (configurar na tela, dentro do POP de atendimento):
  - Automacao: "Sempre que... Mensagem no WhatsApp" -> "Faca isso... Crie card" gravando
    telefone, texto e ANEXO em campos do card;  [A CONFERIR: se o anexo pode ir para um campo]
  - Integracoes -> "+ Nova integracao" -> "Enviar Webhook" quando "Card criado", metodo POST,
    link https://<dominio-da-vps>/infinitum?token=<WEBHOOK_SEGREDO>.
  Os rotulos dos campos ficam em escritorio.json -> webhook_infinitum (campo_telefone,
  campo_arquivo, campo_legenda), comparados em minusculas.

EXPOSICAO: escuta em 127.0.0.1:8085 por padrao. Publicar atras de um nginx/caddy com HTTPS
(o Infinitum precisa de URL publica). Sem --go, registra o evento mas nao sobe nada nem cria tarefa.

Uso (VPS):  python automacoes/drive/receptor_webhook.py --porta 8085 --go
"""
from __future__ import annotations

import argparse
import hmac
import json
import os
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import documento_whatsapp  # noqa: E402
from comum import db, infinitum  # noqa: E402
from comum.config import DADOS_DIR, agora_iso, escritorio, garantir_dir, hoje, utf8_stdout  # noqa: E402

EXECUTAR = False
_trava = threading.Lock()


def _arquivar_evento(payload):
    garantir_dir(DADOS_DIR / "conversas")
    with _trava:
        with open(DADOS_DIR / "conversas" / f"webhook_{hoje().strftime('%Y-%m')}.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps({"recebido_em": agora_iso(), "payload": payload}, ensure_ascii=False) + "\n")
        con = db.conectar()
        db.registrar_webhook(con, "infinitum", payload)
        con.close()


def processar(payload) -> dict:
    cfg = escritorio()
    rot = cfg.get("webhook_infinitum") or {}
    card_id = infinitum.card_id_do_payload(payload)
    if not card_id:
        return {"ok": True, "obs": "payload sem card_id (so arquivado)"}
    card = infinitum.obter_card(card_id)
    if isinstance(card, dict) and isinstance(card.get("data"), dict):
        card = card["data"]
    vals = infinitum.valores_do_card(card)
    arquivo = vals.get((rot.get("campo_arquivo") or "arquivo").lower())
    if isinstance(arquivo, list):
        arquivo = arquivo[0] if arquivo else None
    if isinstance(arquivo, dict):
        arquivo = arquivo.get("url") or arquivo.get("link")
    if not arquivo or not str(arquivo).startswith("http"):
        return {"ok": True, "obs": "card sem link de arquivo", "card": card_id}
    tel = vals.get((rot.get("campo_telefone") or "telefone").lower()) or ""
    leg = vals.get((rot.get("campo_legenda") or "mensagem").lower()) or card.get("title") or ""
    return documento_whatsapp.arquivar(url=str(arquivo), telefone=str(tel), legenda=str(leg),
                                       executar=EXECUTAR, cfg=cfg)


class Handler(BaseHTTPRequestHandler):
    def _responder(self, codigo, corpo):
        dados = json.dumps(corpo, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(dados)))
        self.end_headers()
        self.wfile.write(dados)

    def do_GET(self):
        self._responder(200 if urlparse(self.path).path == "/saude" else 404, {"ok": True})

    def do_POST(self):
        url = urlparse(self.path)
        segredo = os.getenv("WEBHOOK_SEGREDO") or ""
        token = (parse_qs(url.query).get("token") or [""])[0]
        if url.path != "/infinitum" or not segredo or not hmac.compare_digest(token, segredo):
            return self._responder(403, {"erro": "proibido"})
        tamanho = int(self.headers.get("Content-Length") or 0)
        if tamanho > 5_000_000:
            return self._responder(413, {"erro": "payload grande demais"})
        try:
            payload = json.loads(self.rfile.read(tamanho) or b"{}")
        except ValueError:
            return self._responder(400, {"erro": "json invalido"})
        _arquivar_evento(payload)
        self._responder(200, {"ok": True})        # responde ja; processa em seguida
        threading.Thread(target=self._depois, args=(payload,), daemon=True).start()

    @staticmethod
    def _depois(payload):
        try:
            print(agora_iso(), "processado:", processar(payload), flush=True)
        except Exception as e:  # noqa: BLE001 — log e segue; o evento cru ja esta salvo
            print(agora_iso(), "ERRO ao processar evento:", e, flush=True)

    def log_message(self, fmt, *args):
        print(agora_iso(), self.address_string(), fmt % args, flush=True)


def main():
    global EXECUTAR
    utf8_stdout()
    ap = argparse.ArgumentParser(description="Receptor de webhook do Infinitum")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--porta", type=int, default=8085)
    ap.add_argument("--go", action="store_true", help="sobe no Drive e cria tarefa (sem isso, so registra)")
    a = ap.parse_args()
    if not os.getenv("WEBHOOK_SEGREDO"):
        raise SystemExit("ERRO: defina WEBHOOK_SEGREDO em config/.env (texto aleatorio longo)")
    EXECUTAR = a.go
    print(f"Receptor em http://{a.host}:{a.porta}/infinitum  ({'EXECUTANDO' if a.go else 'so registrando'})")
    ThreadingHTTPServer((a.host, a.porta), Handler).serve_forever()


if __name__ == "__main__":
    main()
