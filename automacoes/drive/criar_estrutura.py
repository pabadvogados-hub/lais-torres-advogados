# -*- coding: utf-8 -*-
"""Cria a estrutura do Drive do escritorio (ESTRUTURA_DRIVE.md). Idempotente: pasta que ja existe
e reaproveitada, nunca duplicada. Nada e apagado nem movido.

Subcomandos:
  base          [--ano 2026]                 00_ESCRITORIO/*, RH, FINANCEIRO/<ano>/<01..12>/*, CLIENTES
  cliente       --id ID | --todos            CLIENTES/<NOME>/ + subpastas + processos e demandas do cadastro
  processo      --cliente ID --numero N [--parte P] [--tipo T]
  demanda       --cliente ID --assunto "..." [--data AAAA-MM-DD]
  colaborador   --id ID | --todos            RH/<NOME - VINCULO>/01..05
  docs                                       sobe pops/, checklists/, mensagens/ e modelos/ para 00_ESCRITORIO
                                             (nao sobrescreve arquivo com o mesmo nome)

Opcoes: --offline mostra o plano sem tocar no Drive; --go cria de verdade.
Raiz: escritorio.json -> drive.raiz_id (id da pasta raiz ou do Drive compartilhado do escritorio).

Uso:
    python automacoes/drive/criar_estrutura.py base --offline
    python automacoes/drive/criar_estrutura.py base --go
    python automacoes/drive/criar_estrutura.py cliente --todos --go
    python automacoes/drive/criar_estrutura.py demanda --cliente empresa-x --assunto "notificacao fornecedor" --go
"""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from comum import drive  # noqa: E402
from comum.cadastros import cliente_por_id, lista_clientes, lista_colaboradores, colaborador_por_id  # noqa: E402
from comum.cadastros import pasta_do_colaborador  # noqa: E402
from comum.config import RAIZ, add_modo, banner, bloquear_exemplo, escritorio, utf8_stdout  # noqa: E402
from comum.estrutura import (E, caminho_cliente, caminho_demanda, caminho_processo,  # noqa: E402
                             subpastas_cliente)


def _arvore(prefixo: list[str], no: dict) -> list[list[str]]:
    out = []
    for nome, filhos in no.items():
        out.append(prefixo + [nome])
        out += _arvore(prefixo + [nome], filhos or {})
    return out


def plano_base(ano: int) -> list[list[str]]:
    p = _arvore([], E["raiz"])
    for mes in range(1, 13):
        p.append(["FINANCEIRO", str(ano), f"{mes:02d}"])
        p += [["FINANCEIRO", str(ano), f"{mes:02d}", s] for s in E["financeiro_mes"]]
    p += [["00_ESCRITORIO", "CONTROLADORIA", str(ano)]]
    return p


def plano_cliente(c: dict) -> list[list[str]]:
    base = caminho_cliente(c)
    p = [base] + [base + s for s in subpastas_cliente(c)]
    for proc in c.get("processos") or []:
        if proc.get("numero"):
            cp = caminho_processo(c, proc)
            p += [cp] + [cp + [s] for s in E["processo"]]
    for dem in c.get("demandas_extrajudiciais") or []:
        if dem.get("assunto"):
            cd = caminho_demanda(c, dem)
            p += [cd] + [cd + [s] for s in E["demanda"]]
    return p


def plano_colaborador(c: dict) -> list[list[str]]:
    base = ["RH", pasta_do_colaborador(c)]
    return [base] + [base + [s] for s in E["colaborador"]]


def aplicar(plano: list[list[str]], executar: bool, offline: bool, raiz_id: str):
    vistos = set()
    plano = [p for p in plano if not (tuple(p) in vistos or vistos.add(tuple(p)))]
    if offline:
        for p in plano:
            print("  " + "    " * (len(p) - 1) + p[-1] + "/")
        print(f"\n{len(plano)} pastas no plano (offline: nada foi consultado no Drive).")
        return
    svc = drive.servico()
    for p in plano:
        drive.garantir_caminho(svc, raiz_id, p, executar=executar, log=print)
    print(f"\n{len(plano)} pastas conferidas.")


def docs(executar: bool, offline: bool, raiz_id: str):
    pares = [("pops", ["00_ESCRITORIO", "POPS"]), ("checklists", ["00_ESCRITORIO", "CHECKLISTS"]),
             ("mensagens", ["00_ESCRITORIO", "MENSAGENS"]), ("modelos", ["00_ESCRITORIO", "MODELOS"])]
    svc = None if offline else drive.servico()
    for pasta_local, destino in pares:
        for arq in sorted((RAIZ / pasta_local).rglob("*.md")):
            rel = arq.relative_to(RAIZ / pasta_local)
            alvo = destino + list(rel.parent.parts)
            print(f"  {pasta_local}/{rel.as_posix()} -> {'/'.join(alvo)}/")
            if svc:
                pid = drive.garantir_caminho(svc, raiz_id, alvo, executar=executar, log=None)
                drive.enviar_arquivo(svc, arq, pid, executar=executar)


def main():
    utf8_stdout()
    ap = argparse.ArgumentParser(description="Estrutura do Drive do escritorio")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = add_modo(sub.add_parser("base"))
    s.add_argument("--ano", type=int, default=date.today().year)
    s = add_modo(sub.add_parser("cliente"))
    s.add_argument("--id")
    s.add_argument("--todos", action="store_true")
    s = add_modo(sub.add_parser("processo"))
    s.add_argument("--cliente", required=True)
    s.add_argument("--numero", required=True)
    s.add_argument("--parte", default="")
    s.add_argument("--tipo", default="")
    s = add_modo(sub.add_parser("demanda"))
    s.add_argument("--cliente", required=True)
    s.add_argument("--assunto", required=True)
    s.add_argument("--data", default=date.today().isoformat())
    s = add_modo(sub.add_parser("colaborador"))
    s.add_argument("--id")
    s.add_argument("--todos", action="store_true")
    add_modo(sub.add_parser("docs"))
    for p in sub.choices.values():
        p.add_argument("--offline", action="store_true", help="so mostra o plano")
    a = ap.parse_args()
    banner(a.go, f"Drive: {a.cmd}")
    cfg = escritorio()
    bloquear_exemplo(cfg, "escritorio", a.go)
    raiz = (cfg.get("drive") or {}).get("raiz_id") or ""
    offline = a.offline or not raiz or not drive.credenciais_disponiveis()
    if offline and not a.offline:
        print("  Sem drive.raiz_id ou sem credencial Google: mostrando so o plano.")
        if a.go:
            raise SystemExit("ERRO: --go precisa de drive.raiz_id e da credencial do Google.")

    if a.cmd == "base":
        plano = plano_base(a.ano)
    elif a.cmd == "cliente":
        alvos = lista_clientes() if a.todos else [cliente_por_id(a.id)]
        if not all(alvos):
            raise SystemExit(f"cliente {a.id} nao esta em config/clientes.json")
        plano = [p for c in alvos for p in plano_cliente(c)]
    elif a.cmd == "processo":
        c = cliente_por_id(a.cliente) or {"nome": a.cliente}
        cp = caminho_processo(c, {"numero": a.numero, "parte_contraria": a.parte, "tipo_acao": a.tipo})
        plano = [cp] + [cp + [s] for s in E["processo"]]
    elif a.cmd == "demanda":
        c = cliente_por_id(a.cliente) or {"nome": a.cliente}
        cd = caminho_demanda(c, {"assunto": a.assunto, "aberta_em": a.data})
        plano = [cd] + [cd + [s] for s in E["demanda"]]
        print("  Lembrete: registre a demanda em clientes.json -> demandas_extrajudiciais (roteia os documentos).")
    elif a.cmd == "colaborador":
        alvos = lista_colaboradores() if a.todos else [colaborador_por_id(a.id)]
        if not all(alvos):
            raise SystemExit(f"colaborador {a.id} nao esta em config/colaboradores.json")
        plano = [p for c in alvos for p in plano_colaborador(c)]
    else:
        docs(a.go, offline, raiz)
        return
    aplicar(plano, a.go, offline, raiz)


if __name__ == "__main__":
    main()
