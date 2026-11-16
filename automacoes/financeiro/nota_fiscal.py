# -*- coding: utf-8 -*-
"""Nota fiscal de servico (NFS-e) pelo Asaas, sem depender do "dia 20" do contador.

Regra por cliente (config/clientes.json -> cliente.nf.quando):
  "antes"      -> empresa que so paga com nota: a nota e agendada quando a cobranca entra na
                  janela de `dias_antes` (padrao 10) do vencimento, e o link vai junto com o
                  lembrete de 10 dias (MSG-07, modelo 1-NF).
  "depois"     -> a nota e agendada quando o Asaas confirma o pagamento (RECEIVED/CONFIRMED).
  "nao_emitir" -> ignora (ou cliente sem a chave nf).

API (referencia "Agendar nota fiscal", conferida em 16/11/2026): POST /v3/invoices com
payment, serviceDescription, observations, value, deductions, effectiveDate,
municipalServiceName (+ municipalServiceId OU municipalServiceCode), taxes{retainIss, iss, pis,
cofins, csll, inss, ir}, externalReference. Status: SCHEDULED -> AUTHORIZED (ou ERROR).
A nota emitida traz pdfUrl e xmlUrl.

TRAVAS (licao de implantacao anterior: ligar a emissao "automatica" sem data de corte gera nota
retroativa de anos e nota duplicada do que o Asaas ja emitiu):
  - fiscal.emitir_desde (obrigatorio com --go): cobranca com vencimento/pagamento anterior
    nunca entra;
  - idempotencia por externalReference "nf:<payment_id>" + tabela notas do banco local;
  - fiscal incompleto (codigo do servico, aliquotas) = nao emite. Esses dados vem do CONTADOR,
    nao se inventam;
  - maximo de notas por rodada (fiscal.max_por_rodada, padrao 20).
  - Se a emissao automatica de NF estiver ligada no PAINEL do Asaas para algum cliente,
    desligue la ou tire o cliente daqui: as duas juntas duplicam a nota.

ENVIO AO CLIENTE: quando a nota fica AUTHORIZED, o link do PDF vai pelo WhatsApp (mensageria).
[A CONFERIR na conta: se o Asaas tambem manda a nota por e-mail ao cliente — a documentacao
publica nao diz, e com notificationDisabled=true pode nao mandar.]

Uso:
    python automacoes/financeiro/nota_fiscal.py              # dry-run: o que seria emitido
    python automacoes/financeiro/nota_fiscal.py --go         # agenda as notas e envia as autorizadas
Cron sugerido: todo dia 07:30 (antes da regua) e 14:00 (pega a nota autorizada no meio do dia).
"""
from __future__ import annotations

import argparse
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from comum import db, mensageria  # noqa: E402
from comum.asaas import AsaasCliente  # noqa: E402
from comum.cadastros import lista_clientes  # noqa: E402
from comum.config import (add_modo, agora_iso, banner, bloquear_exemplo, brl, carregar_json,  # noqa: E402
                          data_br, escritorio, hoje, utf8_stdout)

TAXAS = ("retainIss", "iss", "pis", "cofins", "csll", "inss", "ir")


def fiscal_incompleto(fiscal: dict) -> list[str]:
    falta = []
    if not fiscal.get("municipalServiceName"):
        falta.append("municipalServiceName")
    if not (fiscal.get("municipalServiceCode") or fiscal.get("municipalServiceId")):
        falta.append("municipalServiceCode ou municipalServiceId")
    taxes = fiscal.get("taxes") or {}
    falta += [f"taxes.{t}" for t in TAXAS if taxes.get(t) is None]
    if not fiscal.get("emitir_desde"):
        falta.append("emitir_desde (data de corte)")
    return falta


def montar_payload(pagamento: dict, fiscal: dict, ref: date) -> dict:
    p = {
        "payment": pagamento["id"],
        "serviceDescription": (fiscal.get("serviceDescription_padrao") or pagamento.get("description") or "")[:500],
        "observations": fiscal.get("observations_padrao") or (pagamento.get("description") or ""),
        "value": float(pagamento.get("value") or 0),
        "deductions": float(fiscal.get("deductions") or 0),
        "effectiveDate": ref.isoformat(),
        "municipalServiceName": fiscal.get("municipalServiceName"),
        "taxes": {t: (fiscal.get("taxes") or {}).get(t) for t in TAXAS},
        "externalReference": f"nf:{pagamento['id']}",
    }
    if fiscal.get("municipalServiceId"):
        p["municipalServiceId"] = fiscal["municipalServiceId"]
    elif fiscal.get("municipalServiceCode"):
        p["municipalServiceCode"] = fiscal["municipalServiceCode"]
    return p


def candidatos(asaas: AsaasCliente, cliente: dict, ref: date, corte: str) -> list[dict]:
    nf = cliente.get("nf") or {}
    quando = (nf.get("quando") or "").lower()
    cid = cliente.get("asaas_customer_id")
    if not cid and cliente.get("cpf_cnpj"):
        achado = asaas.buscar_cliente(cliente["cpf_cnpj"])
        cid = (achado or {}).get("id")
    if not cid or quando not in ("antes", "depois"):
        return []
    if quando == "antes":
        ate = (ref + timedelta(days=int(nf.get("dias_antes") or 10))).isoformat()
        itens = asaas.listar_cobrancas(status="PENDING", venc_de=ref.isoformat(), venc_ate=ate, customer=cid)
        itens = [p for p in itens if (p.get("dueDate") or "") >= corte]
    else:
        de = (ref - timedelta(days=5)).isoformat()
        itens = []
        for st in ("RECEIVED", "CONFIRMED"):
            itens += asaas.listar_cobrancas(status=st, pago_de=de, pago_ate=ref.isoformat(), customer=cid)
        itens = [p for p in itens if (p.get("paymentDate") or p.get("clientPaymentDate") or "") >= corte]
    for p in itens:
        p["_nf_quando"] = quando
    return itens


def rodar(asaas: AsaasCliente, executar: bool, cfg: dict, ref: date | None = None) -> dict:
    ref = ref or hoje()
    fiscal = cfg.get("fiscal") or {}
    falta = fiscal_incompleto(fiscal)
    if falta and executar:
        raise SystemExit("ERRO: dados fiscais incompletos em escritorio.json -> fiscal (pedir ao contador): "
                         + ", ".join(falta))
    corte = fiscal.get("emitir_desde") or "9999-12-31"
    maximo = int(fiscal.get("max_por_rodada") or 20)
    con = db.conectar()
    res = {"agendadas": [], "enviadas": [], "avisos": [f"fiscal incompleto: {', '.join(falta)}"] if falta else []}

    for cliente in lista_clientes():
        for p in candidatos(asaas, cliente, ref, corte):
            if len(res["agendadas"]) >= maximo:
                res["avisos"].append(f"limite de {maximo} notas por rodada atingido; o resto fica para a proxima")
                break
            if db.ja_existe(con, "notas", payment_id=p["id"]):
                continue
            ja = asaas.nota_por_referencia(f"nf:{p['id']}")
            if ja:
                if executar:
                    db.gravar(con, "notas", payment_id=p["id"], invoice_id=ja.get("id"), status=ja.get("status"),
                              pdf_url=ja.get("pdfUrl"))
                continue
            payload = montar_payload(p, fiscal, ref)
            nota, erros = asaas.agendar_nota(payload, executar=executar)
            if erros:
                res["avisos"].append(f"{p['id']} ({cliente.get('nome')}): {'; '.join(erros)}")
                continue
            res["agendadas"].append(f"[{p['_nf_quando']}] {cliente.get('nome')} {p['id']} R$ {brl(p.get('value'))}")
            if executar:
                db.gravar(con, "notas", payment_id=p["id"], invoice_id=nota.get("id"), status=nota.get("status"),
                          pdf_url=nota.get("pdfUrl"))

    # atualiza status e envia as autorizadas ainda nao enviadas
    for row in con.execute("SELECT * FROM notas WHERE enviada_em IS NULL").fetchall():
        nota = asaas.obter_nota(row["invoice_id"]) if row["invoice_id"] else {}
        status = nota.get("status") or row["status"]
        if status == "ERROR":
            res["avisos"].append(f"nota {row['invoice_id']} da cobranca {row['payment_id']} com ERRO: "
                                 f"{nota.get('statusDescription')}")
        if executar and nota:
            con.execute("UPDATE notas SET status=?, pdf_url=? WHERE payment_id=?",
                        (status, nota.get("pdfUrl") or row["pdf_url"], row["payment_id"]))
            con.commit()
        if status != "AUTHORIZED" or not (nota.get("pdfUrl") or row["pdf_url"]):
            continue
        pay = asaas.req("GET", f"/payments/{row['payment_id']}")[1] or {}
        cli = asaas.obter_cliente(pay.get("customer")) if pay.get("customer") else {}
        local = next((c for c in lista_clientes() if c.get("asaas_customer_id") == pay.get("customer")), {})
        contato = (local.get("contato_financeiro") or {})
        nome = (contato.get("nome") or "").split(" ")[0].title()
        tel = contato.get("whatsapp") or cli.get("mobilePhone") or ""
        texto, faltando = mensageria.render(
            "{{nome_cliente}}, segue a nota fiscal referente aos {{referencia}} (R$ {{valor}}, vencimento "
            "{{vencimento}}): {{link_nota}}",
            {"nome_cliente": nome, "referencia": pay.get("description"), "valor": brl(pay.get("value")),
             "vencimento": data_br(pay.get("dueDate")), "link_nota": nota.get("pdfUrl") or row["pdf_url"]})
        if faltando:
            res["avisos"].append(f"nota {row['invoice_id']}: mensagem nao sai, faltam {faltando}")
            continue
        envio = mensageria.enviar(tel, texto, origem="nota_fiscal", referencia=row["payment_id"],
                                  executar=executar, cfg=cfg)
        if envio.get("erro"):
            res["avisos"].append(f"nota {row['invoice_id']}: {envio['erro']}")
            continue
        res["enviadas"].append(f"{row['payment_id']} -> {tel}")
        if executar:
            con.execute("UPDATE notas SET enviada_em=? WHERE payment_id=?", (agora_iso(), row["payment_id"]))
            con.commit()
    return res


def main():
    utf8_stdout()
    ap = add_modo(argparse.ArgumentParser(description="NFS-e pelo Asaas: antes ou depois do pagamento, por cliente"))
    ap.add_argument("--fixture", help="JSON offline no lugar da API (teste)")
    ap.add_argument("--data", help="data de referencia AAAA-MM-DD")
    a = ap.parse_args()
    if a.fixture and a.go:
        raise SystemExit("--fixture nao combina com --go")
    banner(a.go, "Nota fiscal")
    cfg = escritorio()
    bloquear_exemplo(cfg, "escritorio", a.go)
    bloquear_exemplo(carregar_json("clientes"), "clientes", a.go)
    res = rodar(AsaasCliente(fixture=a.fixture), a.go, cfg, date.fromisoformat(a.data) if a.data else None)
    print(f"\nNotas a agendar/agendadas: {len(res['agendadas'])}")
    for x in res["agendadas"]:
        print("  -", x)
    print(f"Notas enviadas ao cliente: {len(res['enviadas'])}")
    for x in res["avisos"]:
        print("  !", x)


if __name__ == "__main__":
    main()
