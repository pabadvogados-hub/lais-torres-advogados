# -*- coding: utf-8 -*-
""""Como esta o meu processo?" — busca no ADVBOX (SO LEITURA) e devolve os dados para o agente de
atendimento redigir a resposta em linguagem simples (POP-ATD-01 / MSG-01).

Nao envia nada ao cliente: imprime o processo, a fase, as ultimas movimentacoes e as tarefas
pendentes. O agente redige; a pessoa do atendimento confere e envia pelo Infinitum.

Uso:
    python automacoes/atendimento/status_processo.py --processo 0801234-56.2026.8.10.0040
    python automacoes/atendimento/status_processo.py --telefone 62999999999     (processos do cadastro)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from comum import advbox  # noqa: E402
from comum.cadastros import cliente_por_telefone  # noqa: E402
from comum.config import utf8_stdout  # noqa: E402
from comum.nomes import formatar_cnj  # noqa: E402


def resumo(numero: str) -> dict:
    achados = advbox.buscar_processo(formatar_cnj(numero) or numero)
    if not achados:
        return {"processo": numero, "erro": "nao encontrado no ADVBOX"}
    p = achados[0]
    movs = advbox.ultimas_movimentacoes(p["id"])[:8]
    return {
        "processo": p.get("process_number") or numero,
        "advbox_id": p.get("id"),
        "tipo": p.get("type") or p.get("type_lawsuit"),
        "fase": p.get("stage") or p.get("step"),
        "responsavel": p.get("responsible") or p.get("user"),
        "clientes": p.get("customers"),
        "ultimas_movimentacoes": [{"data": m.get("date"), "texto": (m.get("description") or m.get("title") or "")[:400]}
                                  for m in movs],
    }


def main():
    utf8_stdout()
    ap = argparse.ArgumentParser(description="Status do processo no ADVBOX (leitura)")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--processo")
    g.add_argument("--telefone")
    a = ap.parse_args()
    if a.processo:
        numeros = [a.processo]
    else:
        c = cliente_por_telefone(a.telefone)
        if not c:
            raise SystemExit("telefone sem cliente em config/clientes.json")
        numeros = [p["numero"] for p in c.get("processos") or [] if p.get("numero")]
        print(f"Cliente: {c.get('nome')} — {len(numeros)} processo(s) no cadastro")
    for n in numeros:
        print(json.dumps(resumo(n), ensure_ascii=False, indent=2, default=str))


if __name__ == "__main__":
    main()
