# -*- coding: utf-8 -*-
"""Modelos {{chave}} e saida das mensagens de WhatsApp.

Dois modos (config/escritorio.json -> "mensageria" -> "modo"):

  "fila" (PADRAO)       -> grava dados/fila_mensagens.jsonl e dados/saida/fila_mensagens_<data>.csv.
                           A equipe (ou outra automacao) envia pelo WhatsApp do Infinitum.
  "infinitum_card"      -> cria um card no POP de envios do Infinitum; a automacao nativa do POP
                           ("card criado" -> "Envie WhatsApp da organizacao") manda a mensagem.
                           Depende de conferir na tela do Infinitum que a acao aceita telefone e
                           texto vindos dos campos do card (ver comum/infinitum.py).

Em dry-run nada e gravado nem enviado: so imprime.
"""
from __future__ import annotations

import csv
import json
import re

from . import infinitum
from .config import SAIDA_DIR, DADOS_DIR, agora_iso, escritorio, garantir_dir, hoje, so_digitos

_RE_CHAVE = re.compile(r"\{\{\s*([^{}]+?)\s*\}\}")


def render(modelo: str, dados: dict) -> tuple[str, list[str]]:
    """Troca {{chave}} pelos dados. Devolve (texto, chaves_faltando). Chave sem valor fica
    visivel no texto ({{chave}}) para ninguem enviar mensagem com lacuna sem perceber."""
    faltando = []

    def troca(m):
        chave = m.group(1).strip()
        v = dados.get(chave)
        if v is None or str(v).strip() == "":
            faltando.append(chave)
            return m.group(0)
        return str(v)

    return _RE_CHAVE.sub(troca, modelo), faltando


def telefone_whatsapp(tel) -> str:
    """Formato 55 + DDD + numero. Vazio se invalido."""
    d = so_digitos(tel)
    if not d:
        return ""
    if not d.startswith("55"):
        d = "55" + d
    return d if len(d) in (12, 13) else ""


def enviar(telefone: str, texto: str, origem: str, referencia: str = "", titulo: str = "",
           executar: bool = False, cfg: dict | None = None) -> dict:
    cfg = cfg or escritorio()
    m = cfg.get("mensageria") or {}
    modo = m.get("modo") or "fila"
    tel = telefone_whatsapp(telefone)
    registro = {"criado_em": agora_iso(), "origem": origem, "referencia": referencia,
                "telefone": tel, "texto": texto, "modo": modo}
    if not tel:
        registro["erro"] = "telefone ausente ou invalido"
        print(f"    [SEM TELEFONE] {origem} {referencia}: mensagem nao enviada")
        return registro

    if not executar:
        print(f"    [DRY-RUN -> {modo}] {tel} | {texto[:160].replace(chr(10), ' ')}...")
        registro["dry_run"] = True
        return registro

    if modo == "infinitum_card":
        ids = m.get("infinitum") or {}
        faltam = [k for k in ("org_id", "pop_id", "fase_id", "campo_telefone_id", "campo_mensagem_id")
                  if not ids.get(k)]
        if faltam:
            raise RuntimeError(f"mensageria.infinitum incompleto em escritorio.json: {faltam}")
        values = [{"field_id": ids["campo_telefone_id"], "value": tel},
                  {"field_id": ids["campo_mensagem_id"], "value": texto}]
        resp = infinitum.criar_card(ids["org_id"], ids["pop_id"], ids["fase_id"],
                                    titulo or f"{origem} {referencia}", values, executar=True)
        card = resp if isinstance(resp, dict) else {}
        if isinstance(card.get("data"), dict):
            card = card["data"]
        registro["card"] = card.get("id")
        _gravar_fila(registro)  # fica registrado tambem
        return registro

    _gravar_fila(registro)
    return registro


def _gravar_fila(registro: dict):
    garantir_dir(DADOS_DIR)
    with open(DADOS_DIR / "fila_mensagens.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(registro, ensure_ascii=False) + "\n")
    garantir_dir(SAIDA_DIR)
    csv_path = SAIDA_DIR / f"fila_mensagens_{hoje().isoformat()}.csv"
    novo = not csv_path.exists()
    with open(csv_path, "a", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";")
        if novo:
            w.writerow(["criado_em", "origem", "referencia", "telefone", "texto", "modo"])
        w.writerow([registro["criado_em"], registro["origem"], registro["referencia"],
                    registro["telefone"], registro["texto"], registro["modo"]])
