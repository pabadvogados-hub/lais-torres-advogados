# -*- coding: utf-8 -*-
"""Exporta o que a API PUBLICA do Infinitum expoe (so leitura), para entrar no backup semanal.

RESPOSTA DIRETA A PERGUNTA "a API do Infinitum expoe o historico de mensagens?": NAO.
Pelo que o Casal da IA testou com token real (05 a 09/2026, 61 endpoints em docs.infinitum.app.br),
a API publica tem organizacoes, POPs, fases, campos, CARDS, Finance (Asaas), Tasks, Databases/
Records e Pop Automations — nenhum endpoint de conversa/mensagem do WhatsApp. Este script salva o
que da: POPs com fases, campos e todos os cards (com os valores), em dados/infinitum/AAAA-MM-DD/.
Para as CONVERSAS, ver a secao "Backup do WhatsApp" do automacoes/README.md (alternativas).

Tasks e Databases: os caminhos de leitura nao foram testados aqui; o script tenta e registra a
falha sem parar o backup.

Uso: python automacoes/backup/exportar_infinitum.py [--go]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from comum import infinitum  # noqa: E402
from comum.config import DADOS_DIR, add_modo, banner, escritorio, garantir_dir, hoje, utf8_stdout  # noqa: E402


def _org_id() -> str:
    cfg = escritorio()
    org = ((cfg.get("mensageria") or {}).get("infinitum") or {}).get("org_id")
    if org:
        return org
    d = infinitum.minha_organizacao()
    lista = infinitum.desembrulhar(d)
    if not lista and isinstance(d, dict):
        lista = [d.get("data") if isinstance(d.get("data"), dict) else d]
    return str((lista[0] or {}).get("id") or "") if lista else ""


def exportar(executar: bool = False) -> Path | None:
    if not os.getenv("INFINITUM_PUBLIC_TOKEN"):
        print("  Infinitum: sem INFINITUM_PUBLIC_TOKEN — exportacao pulada.")
        return None
    org = _org_id()
    pops = infinitum.listar_pops(org)
    print(f"  Infinitum: org {org}, {len(pops)} POP(s) visiveis pela API")
    destino = garantir_dir(DADOS_DIR / "infinitum" / hoje().isoformat()) if executar else None
    for pop in pops:
        pid = pop.get("id")
        detalhe = infinitum.obter_pop(pid)
        campos = infinitum.campos_do_pop(pid)
        cards = infinitum.listar_cards(org, pid)
        print(f"    - {pop.get('name') or pop.get('title') or pid}: {len(cards)} card(s), {len(campos)} campo(s)")
        if executar:
            (destino / f"pop_{pid}.json").write_text(json.dumps(
                {"pop": detalhe, "campos": campos, "cards": cards}, ensure_ascii=False, indent=1), encoding="utf-8")
    for nome, endpoint, params in (("tasks", "/tasks", {"organization_id": org}),
                                   ("databases", f"/organizations/{org}/databases", None)):
        try:
            dados = infinitum.req("GET", endpoint, params=params)
            if executar:
                (destino / f"{nome}.json").write_text(json.dumps(dados, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"    - {nome}: ok")
        except RuntimeError as e:
            print(f"    - {nome}: nao exportado ({str(e)[:120]})")
    return destino


def main():
    utf8_stdout()
    a = add_modo(argparse.ArgumentParser(description="Exporta POPs/cards do Infinitum (leitura)")).parse_args()
    banner(a.go, "Exportacao Infinitum")
    print("  Destino:", exportar(a.go) or "(dry-run: nada gravado)")


if __name__ == "__main__":
    main()
