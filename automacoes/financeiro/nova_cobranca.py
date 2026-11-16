# -*- coding: utf-8 -*-
"""Cria cliente + cobranca no Asaas a partir de dados minimos.

Dois usos:

  AVULSO (contrato que nao e de assessoria): voce passa nome, CPF/CNPJ, telefone, valor,
  vencimento e forma de pagamento; o script cadastra o cliente (com as notificacoes do Asaas
  DESLIGADAS), gera a cobranca (ou N parcelas mensais) e enfileira a mensagem com o link.

  ASSESSORIA (--assessoria): registra os 12 boletos mensais de uma vez, cada um com o seu
  vencimento. Boleto registrado aparece no DDA do banco do cliente (se o cliente tiver DDA
  ativo no banco dele, pelo mesmo CPF/CNPJ). Cada mes e uma cobranca separada (nao um
  parcelamento): a nota fiscal, o lembrete e um eventual ajuste valem mes a mes.

Idempotencia: externalReference fixo por cliente+mes (assessoria) ou por --ref (avulso).
Rodar de novo nao duplica: a cobranca que ja existe e reaproveitada.

Uso:
    python automacoes/financeiro/nova_cobranca.py --nome "EMPRESA X LTDA" --doc 00.000.000/0000-00 \
        --telefone 6299999999 --email fin@x.com.br --valor 1500 --vencimento 2026-12-10 \
        --assessoria --meses 12 --referencia "honorários de assessoria"
    python automacoes/financeiro/nova_cobranca.py --nome "FULANO" --doc 000.000.000-00 --telefone ... \
        --valor 3000 --vencimento 2026-12-05 --parcelas 3 --forma UNDEFINED --ref contrato-123 \
        --referencia "honorários do contrato de revisão contratual"
    ... --go    para criar de verdade
"""
from __future__ import annotations

import argparse
import calendar
import os
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from comum import mensageria  # noqa: E402
from comum.asaas import AsaasCliente  # noqa: E402
from comum.config import (add_modo, banner, bloquear_exemplo, brl, data_br, escritorio,  # noqa: E402
                          so_digitos, utf8_stdout)

MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto",
         "setembro", "outubro", "novembro", "dezembro"]


def somar_meses(d: date, n: int) -> date:
    """Mesmo dia do mes, n meses depois; dia 31 em mes curto vira o ultimo dia do mes."""
    m = d.month - 1 + n
    ano, mes = d.year + m // 12, m % 12 + 1
    dia = min(d.day, calendar.monthrange(ano, mes)[1])
    return date(ano, mes, dia)


def valida_doc(doc: str) -> bool:
    d = so_digitos(doc)
    if len(d) == 11:
        if d == d[0] * 11:
            return False
        for i in (9, 10):
            s = sum(int(d[j]) * ((i + 1) - j) for j in range(i))
            if (s * 10 % 11) % 10 != int(d[i]):
                return False
        return True
    if len(d) == 14:
        if d == d[0] * 14:
            return False
        pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        pesos2 = [6] + pesos1
        for pesos, pos in ((pesos1, 12), (pesos2, 13)):
            s = sum(int(d[i]) * pesos[i] for i in range(len(pesos)))
            dv = 0 if s % 11 < 2 else 11 - s % 11
            if dv != int(d[pos]):
                return False
        return True
    return False


def planejar(args) -> list[dict]:
    """Lista de cobrancas a criar: [{valor, vencimento, descricao, ref}]."""
    venc0 = date.fromisoformat(args.vencimento)
    doc = so_digitos(args.doc)
    itens = []
    if args.assessoria:
        for i in range(args.meses):
            v = somar_meses(venc0, i)
            # referencia do mes de competencia = mes do vencimento (ajustavel em --competencia-anterior)
            comp = somar_meses(v, -1) if args.competencia_anterior else v
            desc = f"{args.referencia} de {MESES[comp.month - 1]}/{comp.year}"
            itens.append({"valor": args.valor, "vencimento": v.isoformat(), "descricao": desc,
                          "ref": f"assess:{doc}:{comp.strftime('%Y-%m')}"})
    else:
        n = max(1, args.parcelas)
        base = round(args.valor / n, 2)
        for i in range(n):
            v = somar_meses(venc0, i)
            valor = base if i < n - 1 else round(args.valor - base * (n - 1), 2)
            desc = args.referencia if n == 1 else f"{args.referencia} (parcela {i + 1} de {n})"
            itens.append({"valor": valor, "vencimento": v.isoformat(), "descricao": desc,
                          "ref": f"{args.ref or 'avulso:' + doc}:{i + 1}de{n}"})
    return itens


def main():
    utf8_stdout()
    ap = add_modo(argparse.ArgumentParser(description="Cliente + cobranca no Asaas (avulso ou 12 boletos da assessoria)"))
    ap.add_argument("--nome", required=True)
    ap.add_argument("--doc", required=True, help="CPF ou CNPJ")
    ap.add_argument("--telefone", default="", help="WhatsApp do responsavel financeiro")
    ap.add_argument("--email", default="")
    ap.add_argument("--contato", default="", help="primeiro nome do responsavel financeiro (vai na mensagem)")
    ap.add_argument("--valor", type=float, required=True, help="valor mensal (assessoria) ou total (avulso)")
    ap.add_argument("--vencimento", required=True, help="primeiro vencimento AAAA-MM-DD")
    ap.add_argument("--referencia", required=True,
                    help='texto da cobranca, no plural como nas mensagens: "honorários de assessoria"')
    ap.add_argument("--forma", default="BOLETO", choices=["BOLETO", "PIX", "UNDEFINED", "CREDIT_CARD"],
                    help="UNDEFINED = o cliente escolhe boleto, Pix ou cartao na pagina do Asaas")
    ap.add_argument("--assessoria", action="store_true", help="registra os boletos mensais da assessoria")
    ap.add_argument("--meses", type=int, default=12)
    ap.add_argument("--competencia-anterior", action="store_true",
                    help="o boleto de dezembro cobra novembro (competencia = mes anterior ao vencimento)")
    ap.add_argument("--parcelas", type=int, default=1, help="avulso: numero de parcelas mensais")
    ap.add_argument("--ref", default="", help="avulso: identificador do contrato (idempotencia)")
    ap.add_argument("--nao-avisar", action="store_true", help="nao enfileira a mensagem com o link")
    a = ap.parse_args()

    banner(a.go, "Nova cobranca")
    cfg = escritorio()
    bloquear_exemplo(cfg, "escritorio", a.go)
    if not valida_doc(a.doc):
        raise SystemExit(f"ERRO: CPF/CNPJ {a.doc} com digito verificador invalido. Confira com o cliente.")
    if a.assessoria and a.forma not in ("BOLETO", "UNDEFINED"):
        raise SystemExit("ERRO: assessoria usa BOLETO (ou UNDEFINED) para o boleto cair no DDA.")
    cob = cfg.get("cobranca") or {}
    if not os.getenv("ASAAS_API_KEY"):
        if a.go:
            raise SystemExit("ERRO: ASAAS_API_KEY ausente em config/.env")
        print("Sem ASAAS_API_KEY: so o plano (nenhuma consulta ao Asaas).")
        print(f"  cliente: {a.nome} | {a.doc} | notificationDisabled=true")
        for item in planejar(a):
            print(f"  {item['vencimento']}  R$ {brl(item['valor']):>10}  {item['descricao']}  ref={item['ref']}")
        return
    asaas = AsaasCliente()

    cli = asaas.buscar_cliente(a.doc)
    if cli:
        print(f"Cliente ja existe no Asaas: {cli['id']} - {cli.get('name')}")
        r = asaas.desligar_notificacoes(cli["id"], executar=a.go)
        print(f"  notificacoes do Asaas para este cliente: {r if r.get('_dry_run') else 'desligadas/conferidas'}")
        customer_id = cli["id"]
    else:
        cli, erros = asaas.criar_cliente(a.nome, a.doc, a.email, a.telefone, executar=a.go)
        if erros:
            raise SystemExit("ERRO ao criar cliente: " + "; ".join(erros))
        print(f"Cliente {'(dry-run) ' if not a.go else ''}criado com notificationDisabled=true: {cli.get('id', cli.get('_payload'))}")
        customer_id = cli.get("id") or "DRY_CUSTOMER"

    links = []
    for item in planejar(a):
        pay, ja, erros = asaas.criar_cobranca(customer_id, item["valor"], item["vencimento"], item["descricao"],
                                              item["ref"], tipo=a.forma, multa_percent=cob.get("multa_percent"),
                                              juros_mes=cob.get("juros_mes"), executar=a.go)
        if erros:
            print(f"  ERRO {item['ref']}: {'; '.join(erros)}")
            continue
        estado = "ja existia" if ja else ("dry-run" if pay.get("_dry_run") else "criada")
        print(f"  {item['vencimento']}  R$ {brl(item['valor']):>10}  {item['descricao']}  [{estado}] "
              f"{pay.get('id', '')} {pay.get('invoiceUrl', '')}")
        if pay.get("invoiceUrl"):
            links.append((item, pay["invoiceUrl"]))

    if a.nao_avisar:
        return
    # Mensagem com o link da PRIMEIRA cobranca (as seguintes chegam pela regua, 10 dias antes de cada uma)
    primeiro = links[0] if links else (planejar(a)[0], "{{link_pagamento}}")
    item, link = primeiro
    nome = (a.contato or (a.nome if len(so_digitos(a.doc)) == 11 else "")).split(" ")[0].title()
    texto = (f"{nome or '{{nome_cliente}}'}, tudo bem? Seguem os {item['descricao']}, no valor de R$ "
             f"{brl(item['valor'])}, com vencimento em {data_br(item['vencimento'])}.\n\n"
             f"Link de pagamento (boleto ou Pix): {link}")
    if a.assessoria:
        texto += "\n\nOs boletos dos próximos meses já estão registrados e aparecem no DDA do banco da empresa."
    if "{{" in texto:
        print("\nMensagem NAO enfileirada (falta nome do contato ou link). Texto:\n" + texto)
        return
    mensageria.enviar(a.telefone, texto, origem="nova_cobranca", referencia=item["ref"], executar=a.go, cfg=cfg)
    print("\nLembrete: cadastre o cliente em config/clientes.json (contato financeiro e regra de NF: antes/depois).")


if __name__ == "__main__":
    main()
