# -*- coding: utf-8 -*-
"""Documento recebido no WhatsApp (Infinitum) -> pasta certa do cliente no Drive + tarefa no ADVBOX.

Regra de ouro (pops/README 4.1): documento mora no Drive; no ADVBOX vai o LINK (a API do ADVBOX
nem tem upload de documento).

ROTEAMENTO (na ordem):
  1. Telefone -> cliente (config/clientes.json: whatsapps / contato_financeiro). Desconhecido ->
     00_ESCRITORIO/ENTRADA_WHATSAPP + tarefa de triagem para o atendimento.
  2. Numero CNJ na legenda ou no nome do arquivo -> CLIENTES/<cliente>/02_JUDICIAL/<processo>/01_DOCUMENTOS_DO_CLIENTE.
  3. Palavra-chave de uma demanda extrajudicial ABERTA do cliente (clientes.json ->
     demandas_extrajudiciais[].palavras_chave) -> 03_EXTRAJUDICIAL/<demanda>/01_DOCUMENTOS_RECEBIDOS.
     E assim que o cliente de assessoria com varias demandas nao vira bagunca.
  4. Documento pessoal/societario (RG, CPF, CNH, contrato social, comprovante de endereco,
     procuracao) -> 01_CONTRATO_E_DOCUMENTOS.
  5. Cliente com um unico processo e sem demanda aberta -> esse processo.
  6. Nao deu para saber -> CLIENTES/<cliente>/99_A_CLASSIFICAR + tarefa "classificar documento".
  Nunca chuta entre dois clientes: telefone ambiguo vai para a triagem.

TAREFA NO ADVBOX: "[DOCUMENTO] Documento recebido - <cliente> - <processo/assunto>" com o link do
Drive, prazo de 1 dia util, no processo (lawsuit) do caso ou no registro de assessoria do cliente
(o ADVBOX exige lawsuits_id para qualquer tarefa).

Idempotente por hash do arquivo (tabela documentos_recebidos).

ENTRADA:
  - manual/teste:  python automacoes/drive/documento_whatsapp.py --arquivo X.pdf --telefone 62999999999 --legenda "..."
  - automatica:    receptor_webhook.py chama arquivar() quando o Infinitum avisa (ver DEPENDENCIA abaixo).

DEPENDENCIA DO INFINITUM (nao resolvida por codigo): a API publica nao entrega mensagens nem
anexos. O caminho possivel e montar no Infinitum uma automacao "Mensagem no WhatsApp" -> "Crie
card" (com o anexo e o telefone em campos do card) + a integracao "Enviar Webhook" quando o card
for criado, apontando para o receptor_webhook.py na VPS. [A CONFERIR na tela do Infinitum: se a
automacao consegue gravar o ANEXO (link do arquivo) num campo do card.] Se nao conseguir, a
alternativa e a equipe encaminhar o documento para um e-mail/pasta e rodar este script com --arquivo.
"""
from __future__ import annotations

import argparse
import hashlib
import mimetypes
import re
import sys
import tempfile
from datetime import timedelta
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from comum import advbox, db, drive  # noqa: E402
from comum.cadastros import cliente_por_telefone  # noqa: E402
from comum.config import add_modo, banner, bloquear_exemplo, escritorio, hoje, utf8_stdout  # noqa: E402
from comum.estrutura import E, caminho_cliente, caminho_demanda, caminho_processo  # noqa: E402
from comum.nomes import achar_cnj, nome_arquivo, sem_acento  # noqa: E402

DOC_PESSOAL = ("rg", "cpf", "cnh", "identidade", "comprovante de endereco", "comprovante de residencia",
               "contrato social", "cartao cnpj", "procuracao", "certidao de casamento", "certidao de nascimento",
               "alteracao contratual", "documentos pessoais")


def _n(s: str) -> str:
    return re.sub(r"\s+", " ", sem_acento(s).lower()).strip()


def rotear(cliente: dict | None, legenda: str, nome_original: str) -> dict:
    """Devolve {caminho, contexto, lawsuit_id, area, motivo}. Funcao pura (testavel offline)."""
    texto = _n(f"{legenda} {nome_original}")
    if not cliente:
        return {"caminho": ["00_ESCRITORIO", "ENTRADA_WHATSAPP"], "contexto": "remetente nao cadastrado",
                "lawsuit_id": None, "area": "atendimento", "motivo": "telefone sem cliente"}
    adv = cliente.get("advbox") or {}
    registro = adv.get("registro_assessoria_lawsuit_id")
    cnj = achar_cnj(f"{legenda} {nome_original}")
    if cnj:
        alvo = re.sub(r"\D", "", cnj)
        for p in cliente.get("processos") or []:
            if re.sub(r"\D", "", str(p.get("numero"))) == alvo:
                return {"caminho": caminho_processo(cliente, p) + [E["processo"][0]], "contexto": cnj,
                        "lawsuit_id": p.get("advbox_lawsuit_id") or registro, "area": p.get("area"),
                        "motivo": "numero do processo na legenda"}
        return {"caminho": caminho_processo(cliente, {"numero": cnj}) + [E["processo"][0]], "contexto": cnj,
                "lawsuit_id": registro, "area": cliente.get("area_padrao"),
                "motivo": "numero CNJ na legenda, processo ainda nao cadastrado em clientes.json"}
    for d in cliente.get("demandas_extrajudiciais") or []:
        if d.get("encerrada_em"):
            continue
        chaves = [_n(k) for k in (d.get("palavras_chave") or []) + [d.get("assunto", "")] if k]
        if any(k and re.search(r"\b" + re.escape(k) + r"\b", texto) for k in chaves):
            return {"caminho": caminho_demanda(cliente, d) + [E["demanda"][0]], "contexto": d.get("assunto"),
                    "lawsuit_id": d.get("advbox_lawsuit_id") or registro, "area": d.get("area") or cliente.get("area_padrao"),
                    "motivo": "palavra-chave da demanda"}
    if any(re.search(r"\b" + re.escape(k) + r"\b", texto) for k in DOC_PESSOAL):
        return {"caminho": caminho_cliente(cliente) + ["01_CONTRATO_E_DOCUMENTOS"], "contexto": "documentos do cliente",
                "lawsuit_id": registro, "area": "atendimento", "motivo": "documento pessoal/societario"}
    procs = [p for p in cliente.get("processos") or [] if p.get("numero")]
    abertas = [d for d in cliente.get("demandas_extrajudiciais") or [] if not d.get("encerrada_em")]
    if len(procs) == 1 and not abertas:
        p = procs[0]
        return {"caminho": caminho_processo(cliente, p) + [E["processo"][0]], "contexto": p.get("numero"),
                "lawsuit_id": p.get("advbox_lawsuit_id") or registro, "area": p.get("area"),
                "motivo": "cliente com um unico caso"}
    return {"caminho": caminho_cliente(cliente) + ["99_A_CLASSIFICAR"], "contexto": "a classificar",
            "lawsuit_id": registro, "area": "atendimento", "motivo": "sem processo/demanda identificavel"}


def _baixar(url: str) -> Path:
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    ext = mimetypes.guess_extension((r.headers.get("Content-Type") or "").split(";")[0].strip()) or ""
    nome = Path(url.split("?")[0]).name or "documento"
    if not Path(nome).suffix and ext:
        nome += ext
    destino = Path(tempfile.mkdtemp()) / nome
    destino.write_bytes(r.content)
    return destino


def arquivar(arquivo: str | Path | None = None, url: str | None = None, telefone: str = "", legenda: str = "",
             executar: bool = False, cfg: dict | None = None) -> dict:
    cfg = cfg or escritorio()
    local = Path(arquivo) if arquivo else _baixar(url)
    conteudo = local.read_bytes()
    h = hashlib.sha256(conteudo).hexdigest()
    con = db.conectar()
    if db.ja_existe(con, "documentos_recebidos", hash=h):
        return {"ja_arquivado": True, "hash": h}
    cliente = cliente_por_telefone(telefone)
    rota = rotear(cliente, legenda, local.name)
    nome = nome_arquivo("DOC-CLIENTE", legenda or local.stem, local.suffix, quando=hoje())
    res = {"cliente": (cliente or {}).get("nome"), "destino": "/".join(rota["caminho"]), "nome": nome,
           "motivo": rota["motivo"], "hash": h}
    raiz = (cfg.get("drive") or {}).get("raiz_id")
    link = ""
    if raiz and drive.credenciais_disponiveis():
        svc = drive.servico()
        pid = drive.garantir_caminho(svc, raiz, rota["caminho"], executar=executar)
        f = drive.enviar_arquivo(svc, local, pid, nome, executar=executar)
        link = f.get("webViewLink") or ""
        res["drive"] = f
    else:
        res["drive"] = "sem raiz_id/credencial: nao subiu"
    adv = cfg.get("advbox") or {}
    resp = (adv.get("responsaveis") or {})
    quem = resp.get(rota.get("area") or "") or resp.get("atendimento")
    lid = rota["lawsuit_id"] or (adv.get("processo_administrativo_id") if not cliente else None)
    prazo = hoje() + timedelta(days=1)          # 1 dia util
    while prazo.weekday() >= 5:
        prazo += timedelta(days=1)
    titulo = (f"[DOCUMENTO] Documento recebido - {(cliente or {}).get('nome') or telefone} - {rota['contexto']}")
    comentario = (f"{titulo}\nArquivo: {nome}\nPasta: {res['destino']}\nLink: {link or '(dry-run)'}\n"
                  f"Legenda do cliente: {legenda or '-'}\nRoteamento: {rota['motivo']}\n"
                  + ("Conferir e mover para a pasta certa (99_A_CLASSIFICAR)." if "CLASSIFICAR" in res["destino"]
                     or "ENTRADA" in res["destino"] else ""))
    res["tarefa"] = advbox.criar_tarefa(lid, (adv.get("tipos_tarefa") or {}).get("documento_recebido"),
                                        [quem] if quem else [], adv.get("usuario_robo_id"), comentario,
                                        start_date=hoje().isoformat(), date_deadline=prazo.isoformat(),
                                        executar=executar)
    if executar and isinstance(res["drive"], dict) and not res["drive"].get("_dry_run"):
        db.gravar(con, "documentos_recebidos", hash=h, cliente=res["cliente"], destino=res["destino"],
                  drive_id=(res["drive"].get("id") or ""), tarefa=str(res["tarefa"])[:200])
    return res


def main():
    utf8_stdout()
    ap = add_modo(argparse.ArgumentParser(description="Arquiva documento do WhatsApp no Drive + tarefa no ADVBOX"))
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--arquivo")
    g.add_argument("--url")
    ap.add_argument("--telefone", default="")
    ap.add_argument("--legenda", default="")
    a = ap.parse_args()
    banner(a.go, "Documento do WhatsApp")
    cfg = escritorio()
    bloquear_exemplo(cfg, "escritorio", a.go)
    r = arquivar(a.arquivo, a.url, a.telefone, a.legenda, a.go, cfg)
    for k, v in r.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
