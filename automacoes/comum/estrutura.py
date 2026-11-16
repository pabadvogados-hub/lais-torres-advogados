# -*- coding: utf-8 -*-
"""Caminhos do Drive a partir de automacoes/drive/estrutura_drive.json (fonte unica dos nomes)."""
from __future__ import annotations

import json
from datetime import date

from .config import AUTOMACOES_DIR
from .nomes import pasta_cliente, pasta_demanda, pasta_processo

E = json.loads((AUTOMACOES_DIR / "drive" / "estrutura_drive.json").read_text("utf-8"))


def caminho_cliente(cliente: dict) -> list[str]:
    return ["CLIENTES", pasta_cliente(cliente.get("nome") or cliente.get("id"))]


def subpastas_cliente(cliente: dict) -> list[list[str]]:
    subs = [[s] for s in E["cliente"]]
    if (cliente.get("tipo") or "").lower() == "assessoria":
        subs += [[s] for s in E["cliente_assessoria"]]
    if cliente.get("tributario"):
        for pai, filhos in E["cliente_tributario"].items():
            subs += [[pai, f] for f in filhos]
    return subs


def caminho_processo(cliente: dict, proc: dict) -> list[str]:
    return caminho_cliente(cliente) + ["02_JUDICIAL", pasta_processo(proc.get("numero", ""), proc.get("parte_contraria", ""),
                                                                    proc.get("tipo_acao", ""))]


def caminho_demanda(cliente: dict, dem: dict) -> list[str]:
    return caminho_cliente(cliente) + ["03_EXTRAJUDICIAL", pasta_demanda(dem.get("assunto", ""),
                                                                         dem.get("aberta_em") or date.today())]


def caminho_financeiro(ano: int, mes: int, sub: str | None = None) -> list[str]:
    c = ["FINANCEIRO", str(ano), f"{int(mes):02d}"]
    return c + [sub] if sub else c
