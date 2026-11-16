# -*- coding: utf-8 -*-
"""Relatorio financeiro diario: entradas, saidas, inadimplentes, margem e custo da equipe.

Fontes:
  - Asaas: cobrancas recebidas (entradas por cliente), cobrancas vencidas (inadimplentes),
    cobrancas a vencer no mes, extrato /financialTransactions (saidas: Pix, boletos pagos, taxas)
    e saldo;
  - config/colaboradores.json e config/despesas_fixas.json (o previsto do mes);
  - dados/lancamentos_manuais.csv (opcional): o que passa FORA do Asaas (Nubank, dinheiro).
    Colunas: data;tipo;valor;descricao;categoria   (tipo = entrada | saida; data AAAA-MM-DD)

Saida: dados/saida/relatorios/AAAA-MM-DD_relatorio_financeiro.md e .xlsx (se openpyxl estiver
instalado; senao .csv). Com --go e --drive sobe para FINANCEIRO/AAAA/MM/RELATORIOS no Drive;
com --go e --avisar manda o resumo no WhatsApp da Dra. Lais (escritorio.json -> aprovador).

Uso:
    python automacoes/financeiro/relatorio_diario.py
    python automacoes/financeiro/relatorio_diario.py --fixture automacoes/testes/fixture_asaas.json --data 2026-12-05
    python automacoes/financeiro/relatorio_diario.py --go --drive --avisar
Cron sugerido: todo dia 07:00.
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from comum import mensageria  # noqa: E402
from comum.asaas import AsaasCliente  # noqa: E402
from comum.cadastros import lista_colaboradores, lista_despesas  # noqa: E402
from comum.config import (DADOS_DIR, SAIDA_DIR, add_modo, banner, bloquear_exemplo, brl,  # noqa: E402
                          data_br, escritorio, garantir_dir, hoje, utf8_stdout)

STATUS_RECEBIDO = ("RECEIVED", "CONFIRMED", "RECEIVED_IN_CASH")


def manuais(inicio: str, fim: str) -> list[dict]:
    p = DADOS_DIR / "lancamentos_manuais.csv"
    if not p.exists():
        return []
    out = []
    with open(p, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f, delimiter=";"):
            d = (r.get("data") or "")[:10]
            if inicio <= d <= fim:
                bruto = str(r.get("valor") or "0").strip()
                if "," in bruto:                       # 1.234,56 (formato brasileiro)
                    bruto = bruto.replace(".", "").replace(",", ".")
                try:
                    v = float(bruto)
                except ValueError:
                    continue
                out.append({"data": d, "tipo": (r.get("tipo") or "").lower(), "valor": abs(v),
                            "descricao": r.get("descricao", ""), "categoria": r.get("categoria", "")})
    return out


def coletar(asaas: AsaasCliente, ref: date) -> dict:
    ini = ref.replace(day=1).isoformat()
    fim = ref.isoformat()
    nomes: dict[str, str] = {}

    def nome(cid):
        if cid not in nomes:
            nomes[cid] = (asaas.obter_cliente(cid) or {}).get("name") or cid
        return nomes[cid]

    recebidos = []
    for st in STATUS_RECEBIDO:
        for p in asaas.listar_cobrancas(status=st, pago_de=ini, pago_ate=fim):
            recebidos.append({"data": (p.get("paymentDate") or p.get("clientPaymentDate"))[:10],
                              "cliente": nome(p.get("customer")), "descricao": p.get("description") or "",
                              "valor": float(p.get("value") or 0), "liquido": float(p.get("netValue") or 0)})
    vencidas = []
    for p in asaas.listar_cobrancas(status="OVERDUE"):
        dias = (ref - date.fromisoformat(p["dueDate"][:10])).days
        vencidas.append({"cliente": nome(p.get("customer")), "vencimento": p["dueDate"][:10], "dias": dias,
                         "valor": float(p.get("value") or 0), "descricao": p.get("description") or "",
                         "link": p.get("invoiceUrl") or ""})
    primeiro_prox = date(ref.year + (ref.month == 12), ref.month % 12 + 1, 1)
    fim_mes = date.fromordinal(primeiro_prox.toordinal() - 1).isoformat()
    a_receber = asaas.listar_cobrancas(status="PENDING", venc_de=fim, venc_ate=fim_mes)
    saidas = []
    for t in asaas.extrato(ini, fim):
        v = float(t.get("value") or 0)
        if v < 0:
            saidas.append({"data": (t.get("date") or "")[:10], "tipo": t.get("type") or "",
                           "descricao": t.get("description") or "", "valor": abs(v)})
    man = manuais(ini, fim)
    return {"ini": ini, "fim": fim, "recebidos": recebidos, "vencidas": vencidas,
            "a_receber": [{"cliente": nome(p.get("customer")), "vencimento": p["dueDate"][:10],
                           "valor": float(p.get("value") or 0)} for p in a_receber],
            "saidas": saidas, "manuais": man, "saldo": asaas.saldo()}


def consolidar(d: dict) -> dict:
    ent_asaas = sum(x["valor"] for x in d["recebidos"])
    ent_man = sum(x["valor"] for x in d["manuais"] if x["tipo"] == "entrada")
    sai_asaas = sum(x["valor"] for x in d["saidas"])
    sai_man = sum(x["valor"] for x in d["manuais"] if x["tipo"] == "saida")
    taxas = sum(x["valor"] for x in d["saidas"] if "FEE" in x["tipo"].upper())
    equipe = [c for c in lista_colaboradores() if (c.get("pagamento") or {}).get("valor")]
    custo_equipe = sum(float(c["pagamento"]["valor"]) for c in equipe)
    fixas = sum(float(x.get("valor") or 0) for x in lista_despesas())
    entradas = ent_asaas + ent_man
    saidas = sai_asaas + sai_man
    margem = entradas - saidas
    inad = defaultdict(lambda: {"valor": 0.0, "qtd": 0, "maior_atraso": 0})
    for v in d["vencidas"]:
        i = inad[v["cliente"]]
        i["valor"] += v["valor"]
        i["qtd"] += 1
        i["maior_atraso"] = max(i["maior_atraso"], v["dias"])
    return {
        "entradas": entradas, "entradas_asaas": ent_asaas, "entradas_fora": ent_man,
        "saidas": saidas, "saidas_asaas": sai_asaas, "saidas_fora": sai_man, "taxas_asaas": taxas,
        "margem": margem, "margem_pct": (margem / entradas * 100) if entradas else 0.0,
        "a_receber": sum(x["valor"] for x in d["a_receber"]),
        "inadimplencia": sum(x["valor"] for x in d["vencidas"]), "inadimplentes": dict(inad),
        "custo_equipe_previsto": custo_equipe, "qtd_equipe": len(equipe),
        "despesas_fixas_previstas": fixas, "saldo": d["saldo"],
        "custo_equipe_pct": (custo_equipe / entradas * 100) if entradas else 0.0,
    }


def markdown(ref: date, d: dict, c: dict) -> str:
    L = [f"# Relatório financeiro — {data_br(ref.isoformat())}",
         "",
         f"Período: {data_br(d['ini'])} a {data_br(d['fim'])} (mês corrente até hoje). "
         "Fonte: Asaas + lançamentos manuais. Valores em R$.",
         "",
         "## Resumo",
         "",
         "| Indicador | Valor |",
         "|---|---:|",
         f"| Entradas no mês | {brl(c['entradas'])} |",
         f"| ↳ pelo Asaas | {brl(c['entradas_asaas'])} |",
         f"| ↳ fora do Asaas (manual) | {brl(c['entradas_fora'])} |",
         f"| Saídas no mês | {brl(c['saidas'])} |",
         f"| ↳ taxas do Asaas | {brl(c['taxas_asaas'])} |",
         f"| **Margem do mês** | **{brl(c['margem'])}** ({c['margem_pct']:.1f}%) |",
         f"| A receber até o fim do mês | {brl(c['a_receber'])} |",
         f"| Em atraso (inadimplência) | {brl(c['inadimplencia'])} |",
         f"| Custo mensal da equipe (cadastro) | {brl(c['custo_equipe_previsto'])} — {c['qtd_equipe']} pessoa(s), "
         f"{c['custo_equipe_pct']:.1f}% das entradas |",
         f"| Despesas fixas mensais (cadastro) | {brl(c['despesas_fixas_previstas'])} |",
         f"| Saldo na conta Asaas | {brl(c['saldo']) if c['saldo'] is not None else 'indisponível'} |",
         "",
         "## Inadimplentes",
         ""]
    if c["inadimplentes"]:
        L += ["| Cliente | Cobranças | Valor | Maior atraso (dias) |", "|---|---:|---:|---:|"]
        for nome, i in sorted(c["inadimplentes"].items(), key=lambda kv: -kv[1]["valor"]):
            L.append(f"| {nome} | {i['qtd']} | {brl(i['valor'])} | {i['maior_atraso']} |")
    else:
        L.append("Nenhuma cobrança vencida.")
    L += ["", "## Entradas do mês", ""]
    if d["recebidos"] or any(m["tipo"] == "entrada" for m in d["manuais"]):
        L += ["| Data | Cliente | Descrição | Valor |", "|---|---|---|---:|"]
        for x in sorted(d["recebidos"], key=lambda x: x["data"]):
            L.append(f"| {data_br(x['data'])} | {x['cliente']} | {x['descricao']} | {brl(x['valor'])} |")
        for x in d["manuais"]:
            if x["tipo"] == "entrada":
                L.append(f"| {data_br(x['data'])} | (manual) | {x['descricao']} | {brl(x['valor'])} |")
    else:
        L.append("Nenhuma entrada registrada.")
    L += ["", "## Saídas do mês", ""]
    if d["saidas"] or any(m["tipo"] == "saida" for m in d["manuais"]):
        L += ["| Data | Tipo | Descrição | Valor |", "|---|---|---|---:|"]
        for x in sorted(d["saidas"], key=lambda x: x["data"]):
            L.append(f"| {data_br(x['data'])} | {x['tipo']} | {x['descricao']} | {brl(x['valor'])} |")
        for x in d["manuais"]:
            if x["tipo"] == "saida":
                L.append(f"| {data_br(x['data'])} | manual/{x['categoria']} | {x['descricao']} | {brl(x['valor'])} |")
    else:
        L.append("Nenhuma saída registrada.")
    L += ["", "_Margem = entradas − saídas efetivas do mês até hoje. Custo da equipe e despesas fixas "
          "vêm do cadastro (previsto), não do extrato._", ""]
    return "\n".join(L)


def planilha(caminho: Path, d: dict, c: dict) -> Path:
    try:
        from openpyxl import Workbook
    except ImportError:
        csvp = caminho.with_suffix(".csv")
        with open(csvp, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["secao", "data", "cliente/tipo", "descricao", "valor"])
            for x in d["recebidos"]:
                w.writerow(["entrada", x["data"], x["cliente"], x["descricao"], f"{x['valor']:.2f}"])
            for x in d["saidas"]:
                w.writerow(["saida", x["data"], x["tipo"], x["descricao"], f"{x['valor']:.2f}"])
            for x in d["vencidas"]:
                w.writerow(["inadimplente", x["vencimento"], x["cliente"], x["descricao"], f"{x['valor']:.2f}"])
        return csvp
    wb = Workbook()
    ws = wb.active
    ws.title = "Resumo"
    for k, v in c.items():
        if k != "inadimplentes":
            ws.append([k, v])
    for titulo, cab, linhas in (
        ("Entradas", ["data", "cliente", "descricao", "valor", "liquido"],
         [[x["data"], x["cliente"], x["descricao"], x["valor"], x["liquido"]] for x in d["recebidos"]]),
        ("Saidas", ["data", "tipo", "descricao", "valor"],
         [[x["data"], x["tipo"], x["descricao"], x["valor"]] for x in d["saidas"]]),
        ("Inadimplentes", ["cliente", "vencimento", "dias", "valor", "descricao", "link"],
         [[x["cliente"], x["vencimento"], x["dias"], x["valor"], x["descricao"], x["link"]] for x in d["vencidas"]]),
        ("Manuais", ["data", "tipo", "valor", "descricao", "categoria"],
         [[x["data"], x["tipo"], x["valor"], x["descricao"], x["categoria"]] for x in d["manuais"]]),
        ("Equipe", ["nome", "vinculo", "valor_mensal", "dia"],
         [[x.get("nome"), x.get("vinculo"), (x.get("pagamento") or {}).get("valor"),
           (x.get("pagamento") or {}).get("dia")] for x in lista_colaboradores()]),
    ):
        s = wb.create_sheet(titulo)
        s.append(cab)
        for linha in linhas:
            s.append(linha)
    wb.save(caminho)
    return caminho


def main():
    utf8_stdout()
    ap = add_modo(argparse.ArgumentParser(description="Relatorio financeiro diario"))
    ap.add_argument("--fixture")
    ap.add_argument("--data")
    ap.add_argument("--drive", action="store_true", help="com --go, sobe os arquivos para o Drive")
    ap.add_argument("--avisar", action="store_true", help="com --go, manda o resumo no WhatsApp da aprovadora")
    a = ap.parse_args()
    if a.fixture and a.go:
        raise SystemExit("--fixture nao combina com --go")
    banner(a.go, "Relatorio financeiro diario")
    cfg = escritorio()
    bloquear_exemplo(cfg, "escritorio", a.go)
    ref = date.fromisoformat(a.data) if a.data else hoje()
    dados = coletar(AsaasCliente(fixture=a.fixture), ref)
    cons = consolidar(dados)
    pasta = garantir_dir(SAIDA_DIR / "relatorios")
    base = pasta / f"{ref.isoformat()}_relatorio_financeiro"
    md = base.with_suffix(".md")
    md.write_text(markdown(ref, dados, cons), encoding="utf-8")
    xl = planilha(base.with_suffix(".xlsx"), dados, cons)
    print(f"Gerado: {md}\nGerado: {xl}")
    print(f"Entradas R$ {brl(cons['entradas'])} | Saidas R$ {brl(cons['saidas'])} | "
          f"Margem R$ {brl(cons['margem'])} | Atraso R$ {brl(cons['inadimplencia'])}")

    if a.drive:
        from comum import drive
        raiz = (cfg.get("drive") or {}).get("raiz_id")
        if not raiz or not drive.credenciais_disponiveis():
            print("  Drive: sem raiz_id ou sem credencial — nao subiu.")
        else:
            svc = drive.servico()
            pid = drive.garantir_caminho(svc, raiz, ["FINANCEIRO", str(ref.year), f"{ref.month:02d}", "RELATORIOS"],
                                         executar=a.go)
            for arq in (md, xl):
                print("  Drive:", drive.enviar_arquivo(svc, arq, pid, executar=a.go))
    if a.avisar:
        tel = (cfg.get("aprovador") or {}).get("whatsapp")
        texto = (f"Financeiro {data_br(ref.isoformat())}: entradas no mês R$ {brl(cons['entradas'])}, saídas "
                 f"R$ {brl(cons['saidas'])}, margem R$ {brl(cons['margem'])} ({cons['margem_pct']:.0f}%). "
                 f"Em atraso: R$ {brl(cons['inadimplencia'])} ({len(cons['inadimplentes'])} cliente(s)). "
                 f"A receber até o fim do mês: R$ {brl(cons['a_receber'])}.")
        mensageria.enviar(tel, texto, origem="relatorio_financeiro", referencia=ref.isoformat(),
                          executar=a.go, cfg=cfg)


if __name__ == "__main__":
    main()
