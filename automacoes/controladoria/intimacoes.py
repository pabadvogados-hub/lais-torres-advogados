# -*- coding: utf-8 -*-
"""Rotina diaria da controladoria (POP-OP-02): le as intimacoes do DJEN pelas OABs do escritorio,
classifica, calcula o prazo e cria as tarefas no ADVBOX.

  1. DJEN/Comunica (CNJ) por OAB (config/escritorio.json -> controladoria.oabs);
  2. classificador.py: MERO_ANDAMENTO | EMBARGOS_DE_DECLARACAO | AGRAVO | APELACAO |
     RECURSO_ORDINARIO | OUTROS(+subtipo), com o gatilho e a base legal;
  3. prazos.py: publicacao, inicio, prazo fatal, prazo interno (fatal - 2 uteis), protocolo;
  4. ADVBOX (POST /posts — exige o processo cadastrado no ADVBOX):
       [PRAZO] <peca> - <partes> - <processo>          responsavel da area, fim = prazo interno,
                                                        date_deadline = prazo fatal
       [CONFIRMAR CLASSIFICACAO] ...                   decisao/sentenca/acordao/baixa confianca, hoje
       mero andamento: sem tarefa (so no relatorio);
  5. relatorio do dia em dados/saida/controladoria/AAAA-MM-DD_relatorio-controladoria.md.

Idempotente: cada comunicacao do DJEN vira tarefa uma vez (tabela controladoria do banco local).
Dry-run por padrao.

Uso:
    python automacoes/controladoria/intimacoes.py                    # DJEN de hoje, dry-run
    python automacoes/controladoria/intimacoes.py --dias 3           # ultimos 3 dias
    python automacoes/controladoria/intimacoes.py --arquivo automacoes/testes/fixture_djen.json  # offline
    python automacoes/controladoria/intimacoes.py --go               # cria as tarefas
Cron sugerido: dias uteis 07:30 (o POP pede leitura ate 11h).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import classificador  # noqa: E402
import djen  # noqa: E402
import prazos  # noqa: E402
from comum import advbox, db  # noqa: E402
from comum.cadastros import lista_clientes  # noqa: E402
from comum.config import (SAIDA_DIR, add_modo, banner, bloquear_exemplo, data_br, escritorio,  # noqa: E402
                          garantir_dir, hoje, utf8_stdout)
from comum.nomes import formatar_cnj  # noqa: E402

ROTULO = {"MERO_ANDAMENTO": "Mero andamento", "EMBARGOS_DE_DECLARACAO": "Embargos de declaracao",
          "AGRAVO": "Agravo", "APELACAO": "Apelacao", "RECURSO_ORDINARIO": "Recurso ordinario", "OUTROS": "Outros"}


def area_do_caso(c: dict, item: dict, processo_local: dict | None) -> str:
    if processo_local and processo_local.get("area"):
        return processo_local["area"]
    if "fiscal" in (item.get("classe") or "").lower() or (item.get("tribunal") or "").upper().startswith("TRF"):
        return "tributario"
    return "trabalhista" if c["ramo"] == "trabalhista" else "civel"


def processo_no_cadastro(numero: str) -> tuple[dict | None, dict | None]:
    alvo = "".join(ch for ch in numero if ch.isdigit())
    for cli in lista_clientes():
        for p in cli.get("processos") or []:
            if "".join(ch for ch in str(p.get("numero")) if ch.isdigit()) == alvo and alvo:
                return cli, p
    return None, None


def lawsuit_id(numero: str, processo_local: dict | None, pendencias: list) -> str | None:
    if processo_local and processo_local.get("advbox_lawsuit_id"):
        return str(processo_local["advbox_lawsuit_id"])
    if not os.getenv("ADVBOX_API_TOKEN"):
        return None
    try:
        achados = advbox.buscar_processo(formatar_cnj(numero) or numero)
    except RuntimeError as e:
        pendencias.append(f"{numero}: erro ao buscar no ADVBOX ({e})")
        return None
    return str(achados[0]["id"]) if achados else None


def carregar_itens(a, cfg) -> list[dict]:
    if a.arquivo:
        bruto = json.loads(Path(a.arquivo).read_text("utf-8"))
        return bruto.get("itens", bruto) if isinstance(bruto, dict) else bruto
    ctrl = cfg.get("controladoria") or {}
    oabs = [o for o in ctrl.get("oabs") or [] if o.get("numero") and o.get("uf")]
    if not oabs:
        raise SystemExit("ERRO: nenhuma OAB completa em escritorio.json -> controladoria.oabs")
    fim = a.fim or hoje().isoformat()
    ini = a.inicio or (date.fromisoformat(fim) - timedelta(days=(a.dias or ctrl.get("dias_retroativos") or 1) - 1)).isoformat()
    vistos, itens = set(), []
    for o in oabs:
        print(f"  DJEN: OAB {o['numero']}/{o['uf']} ({o.get('nome', '')}) de {ini} a {fim}...")
        for it in djen.consultar(oab_numero=o["numero"], oab_uf=o["uf"], data_inicio=ini, data_fim=fim):
            chave = str(it.get("id") or it.get("hash"))
            if chave not in vistos:
                vistos.add(chave)
                itens.append(it)
    return itens


def processar(itens: list[dict], cfg: dict, executar: bool) -> dict:
    adv = cfg.get("advbox") or {}
    tipos = adv.get("tipos_tarefa") or {}
    resp = adv.get("responsaveis") or {}
    folga = int((cfg.get("controladoria") or {}).get("prazo_interno_dias_uteis") or 2)
    con = db.conectar()
    linhas, pend = [], []
    for bruto in itens:
        bruto_djen = "siglaTribunal" in bruto or "data_disponibilizacao" in bruto
        it = djen.resumir(bruto) if bruto_djen else bruto
        cid = it.get("id") or ""
        if cid and db.ja_existe(con, "controladoria", comunicacao_id=cid):
            linhas.append({"it": it, "ja": True})
            continue
        c = classificador.classificar(it.get("texto", ""), it.get("tribunal", ""), it.get("classe", ""), it.get("tipo", ""))
        pz = prazos.calcular(it.get("data"), c["dias"], it.get("tribunal", ""), folga_interna=folga)
        cli, proc_local = processo_no_cadastro(it.get("processo", ""))
        area = area_do_caso(c, it, proc_local)
        partes = (cli or {}).get("nome") or " x ".join(p for p in (it.get("partes") or [])[:2]) or "partes nao identificadas"
        numero = formatar_cnj(it.get("processo", "")) or it.get("processo", "")
        linha = {"it": it, "c": c, "pz": pz, "area": area, "partes": partes, "numero": numero, "tarefas": []}
        linhas.append(linha)
        if c["categoria"] == "MERO_ANDAMENTO" and not c["confirmar_advogado"]:
            if executar:
                db.gravar(con, "controladoria", comunicacao_id=cid, processo=numero, categoria=c["categoria"])
            continue
        lid = lawsuit_id(numero, proc_local, pend)
        if not lid:
            pend.append(f"{numero}: processo nao encontrado no ADVBOX — tarefa nao criada (cadastrar o processo "
                        f"ou o advbox_lawsuit_id em clientes.json)")
        comentario = (f"Sugestao automatica da controladoria — CONFERIR.\n"
                      f"Classificacao: {ROTULO[c['categoria']]} / {c['subtipo']} | Peca: {c['peca']}\n"
                      f"Base legal: {c['base_legal']} | Gatilho no texto: \"{c['gatilho']}\" | "
                      f"Confianca: {c['confianca']:.0%}\n"
                      f"Disponibilizacao {data_br(pz.get('disponibilizacao'))}, publicacao {data_br(pz.get('publicacao'))}, "
                      f"inicio {data_br(pz.get('inicio_contagem'))}.\n"
                      + (f"PRAZO FATAL {data_br(pz['prazo_fatal'])} | interno {data_br(pz['prazo_interno'])} | "
                         f"protocolo ate {data_br(pz['protocolo'])}\n" if pz.get("prazo_fatal") else "Sem prazo calculado.\n")
                      + "".join(f"Tambem cabe: {t['peca']} — {t['dias']} dias uteis ({t['base_legal']})\n"
                                for t in c["tambem_cabe"])
                      + "".join(f"Aviso: {x}\n" for x in pz.get("avisos") or [])
                      + f"{it.get('tribunal', '')} | {it.get('orgao', '')}\n{it.get('link', '')}\n\n"
                      + (it.get("texto", "")[:800]))
        responsavel = resp.get(area) or resp.get("controladoria")
        tarefas = []
        if pz.get("prazo_fatal"):
            urgente = (date.fromisoformat(pz["prazo_fatal"]) - hoje()).days <= 7
            tipo = tipos.get("custas") if c["subtipo"] == "custas" else tipos.get("prazo")
            tarefas.append((f"[PRAZO] {c['peca']} - {partes} - {numero}", tipo, responsavel,
                            pz["prazo_interno"], pz["prazo_fatal"], urgente))
        elif c["subtipo"] == "audiencia":
            tarefas.append((f"[AUDIENCIA] {numero} - conferir data no despacho", tipos.get("audiencia"),
                            responsavel, None, None, False))
        if c["confirmar_advogado"]:
            tarefas.append((f"[CONFIRMAR CLASSIFICACAO] {ROTULO[c['categoria']]} ({c['subtipo']}) - {numero}",
                            tipos.get("confirmar_classificacao") or tipos.get("prazo"), responsavel,
                            hoje().isoformat(), None, True))
        ids = []
        for titulo, tipo, quem, fim, fatal, urg in tarefas:
            if not lid:
                linha["tarefas"].append((titulo, {"_dry_run": True, "_sem_processo_no_advbox": True}))
                continue
            r = advbox.criar_tarefa(lid, tipo, [quem] if quem else [], adv.get("usuario_robo_id"),
                                    titulo + "\n\n" + comentario, start_date=hoje().isoformat(),
                                    end_date=fim, date_deadline=fatal, urgent=urg, executar=executar)
            linha["tarefas"].append((titulo, r))
            if isinstance(r, dict) and r.get("erro"):
                pend.append(f"{numero}: {r['erro']}")
            elif executar and lid:
                ids.append(str(r.get("posts_id") or r.get("id") or r.get("success") or "ok"))
        if executar and lid and ids:
            db.gravar(con, "controladoria", comunicacao_id=cid, processo=numero, categoria=c["categoria"],
                      prazo_fatal=pz.get("prazo_fatal"), prazo_interno=pz.get("prazo_interno"), tarefa=",".join(ids))
    return {"linhas": linhas, "pendencias": pend}


def relatorio(res: dict, ref: date) -> str:
    L = [f"# Controladoria — {data_br(ref.isoformat())}", "",
         "Sugestão automática (DJEN por OAB). Decisão, sentença e acórdão: o advogado(a) da área confirma (POP-OP-02).",
         "", "| Processo | Tribunal | Classificação | Peça | Prazo fatal | Interno | Confiança | Confirmar? |",
         "|---|---|---|---|---|---|---:|---|"]
    novas = [x for x in res["linhas"] if not x.get("ja")]
    for x in sorted(novas, key=lambda x: (x["pz"].get("prazo_fatal") or "9999")):
        c, pz = x["c"], x["pz"]
        L.append(f"| {x['numero']} | {x['it'].get('tribunal', '')} | {ROTULO[c['categoria']]} ({c['subtipo']}) | "
                 f"{c['peca']} | {data_br(pz.get('prazo_fatal')) or '-'} | {data_br(pz.get('prazo_interno')) or '-'} | "
                 f"{c['confianca']:.0%} | {'SIM' if c['confirmar_advogado'] else 'não'} |")
    if not novas:
        L.append("| — | — | Nenhuma intimação nova | — | — | — | — | — |")
    ja = [x for x in res["linhas"] if x.get("ja")]
    if ja:
        L += ["", f"Já tratadas em rodadas anteriores: {len(ja)}."]
    if res["pendencias"]:
        L += ["", "## Pendências", ""] + [f"- {p}" for p in res["pendencias"]]
    L += ["", "## Avisos de prazo", ""]
    for x in novas:
        for av in x["pz"].get("avisos") or []:
            L.append(f"- {x['numero']}: {av}")
    return "\n".join(L) + "\n"


def main():
    utf8_stdout()
    ap = add_modo(argparse.ArgumentParser(description="Leitura e classificacao de intimacoes (DJEN -> ADVBOX)"))
    ap.add_argument("--dias", type=int, help="ultimos N dias (padrao: controladoria.dias_retroativos)")
    ap.add_argument("--inicio")
    ap.add_argument("--fim")
    ap.add_argument("--arquivo", help="JSON salvo do DJEN (lista de itens ou {itens: [...]}) — modo offline")
    ap.add_argument("--drive", action="store_true", help="com --go, sobe o relatorio para o Drive")
    a = ap.parse_args()
    banner(a.go, "Controladoria")
    cfg = escritorio()
    bloquear_exemplo(cfg, "escritorio", a.go)
    res = processar(carregar_itens(a, cfg), cfg, a.go)
    for x in res["linhas"]:
        if x.get("ja"):
            continue
        c, pz = x["c"], x["pz"]
        print(f"\n{x['numero']}  [{ROTULO[c['categoria']]} / {c['subtipo']}]  {c['peca']}")
        print(f"   gatilho: '{c['gatilho']}'  confianca {c['confianca']:.0%}  ramo {c['ramo']}  area {x['area']}")
        if pz.get("prazo_fatal"):
            print(f"   prazo: {c['dias']} dias -> fatal {data_br(pz['prazo_fatal'])}, interno {data_br(pz['prazo_interno'])}")
        for t, r in x["tarefas"]:
            print(f"   tarefa: {t.splitlines()[0]} -> {'dry-run' if r.get('_dry_run') else r}")
    ref = hoje()
    pasta = garantir_dir(SAIDA_DIR / "controladoria")
    arq = pasta / f"{ref.isoformat()}_relatorio-controladoria.md"
    arq.write_text(relatorio(res, ref), encoding="utf-8")
    print(f"\nRelatorio: {arq}")
    for p in res["pendencias"]:
        print("  !", p)
    if a.drive and a.go:
        from comum import drive
        raiz = (cfg.get("drive") or {}).get("raiz_id")
        if raiz and drive.credenciais_disponiveis():
            svc = drive.servico()
            pid = drive.garantir_caminho(svc, raiz, ["00_ESCRITORIO", "CONTROLADORIA", str(ref.year),
                                                     f"{ref.month:02d}"], executar=True)
            print("  Drive:", drive.enviar_arquivo(svc, arq, pid, executar=True))


if __name__ == "__main__":
    main()
