# -*- coding: utf-8 -*-
"""Regua de cobranca PROPRIA — substitui os avisos pagos do Asaas.

Problema do kickoff: integrar o Asaas ao ADVBOX ligou todas as notificacoes do Asaas
(antes, depois do vencimento, pagamento...) e um cliente de assessoria recebeu 12 avisos,
cada um cobrado. Aqui:

  1. os clientes sao criados no Asaas com notificationDisabled=true (nova_cobranca.py), e os
     antigos tem as notificacoes desligadas por notificacoes_asaas.py;
  2. este script manda UMA mensagem por marco: 10, 5 e 3 dias antes e no dia do vencimento,
     com o link de pagamento (boleto + Pix), pelo WhatsApp do escritorio (Infinitum);
  3. pagou: os marcos seguintes nao saem (so cobranca PENDING entra) e vai o "pagamento
     recebido" (modelo 6), com o link da nota quando a nota sai apos o pagamento;
  4. atraso (modelos 7 e 8) fica DESLIGADO ate a Dra. Lais confirmar dias e tom
     (escritorio.json -> regua.atraso_ativo).

Textos: mensagens/MSG-07-lembretes-cobranca-financeira.md (lidos do arquivo; se o arquivo
mudar de formato, usa a copia embutida abaixo e avisa).

Envio: comum/mensageria.py (modo "fila" por padrao; "infinitum_card" quando a automacao do
Infinitum estiver configurada). Idempotente: (cobranca, marco) gravado em dados/escritorio.db.

Uso:
    python automacoes/financeiro/regua_cobranca.py                 # dry-run
    python automacoes/financeiro/regua_cobranca.py --go            # envia/enfileira e grava
    python automacoes/financeiro/regua_cobranca.py --fixture automacoes/testes/fixture_asaas.json
Cron sugerido (VPS): todo dia 08:00, depois do nota_fiscal.py.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from comum import db, mensageria  # noqa: E402
from comum.asaas import AsaasCliente  # noqa: E402
from comum.cadastros import cliente_por_asaas  # noqa: E402
from comum.config import (MENSAGENS_DIR, add_modo, banner, bloquear_exemplo, brl, data_br,  # noqa: E402
                          escritorio, hoje, so_digitos, utf8_stdout)

# Copia embutida do MSG-07 (versao 1 de 16/11/2026) — so usada se o arquivo nao puder ser lido.
MODELOS_PADRAO = {
    "1": ("{{nome_cliente}}, tudo bem? Passando para lembrar que os {{referencia}} da {{empresa}}, "
          "no valor de R$ {{valor}}, vencem em {{vencimento}}.\n\nPara sua comodidade, segue o link de "
          "pagamento (boleto ou Pix): {{link_pagamento}}\n\nO boleto também já aparece no DDA do banco da empresa."),
    "1-NF": "A nota fiscal correspondente está disponível aqui: {{link_nota}}",
    "2": "{{nome_cliente}}, lembrete: os {{referencia}} (R$ {{valor}}) vencem em {{vencimento}}. Link de pagamento: {{link_pagamento}}",
    "3": ("{{nome_cliente}}, faltam 3 dias para o vencimento dos {{referencia}} (R$ {{valor}}), em "
          "{{vencimento}}. Link: {{link_pagamento}}"),
    "4": ("{{nome_cliente}}, bom dia! Hoje vencem os {{referencia}} da {{empresa}} (R$ {{valor}}). Se já "
          "estiver programado, desconsidere esta mensagem. Link para pagamento: {{link_pagamento}}"),
    "6": ("{{nome_cliente}}, recebemos o pagamento dos {{referencia}}. Obrigado! [Se a nota sai após o "
          "pagamento: \"A nota fiscal está aqui: {{link_nota}}\"]"),
    "7": ("{{nome_cliente}}, não identificamos ainda o pagamento dos {{referencia}} (R$ {{valor}}), vencidos "
          "em {{vencimento}}. Se já pagou, pode desconsiderar. Caso contrário, segue o link atualizado: {{link_pagamento}}"),
    "8": ("{{nome_cliente}}, os {{referencia}} da {{empresa}} (R$ {{valor}}) seguem em aberto desde "
          "{{vencimento}}. Podemos ajudar com alguma coisa? Link para pagamento: {{link_pagamento}}"),
}
MODELO_DO_MARCO = {10: "1", 5: "2", 3: "3", 0: "4"}
MODELO_DO_ATRASO = {1: "7", 7: "8"}


def ler_modelos(arquivo: Path | None = None) -> dict:
    """Le os blocos '> ' de cada '## Modelo N' do MSG-07. Modelo 1 separa a parte 1-NF."""
    arquivo = arquivo or next(iter(sorted(MENSAGENS_DIR.glob("MSG-07*.md"))), None)
    if not arquivo or not Path(arquivo).exists():
        print("  AVISO: MSG-07 nao encontrado; usando os textos embutidos.")
        return dict(MODELOS_PADRAO)
    modelos: dict[str, list[str]] = {}
    atual = None
    for linha in Path(arquivo).read_text("utf-8").splitlines():
        m = re.match(r"^##\s+Modelo\s+(\d+)", linha)
        if m:
            atual = m.group(1)
            modelos[atual] = []
            continue
        if linha.startswith("## "):
            atual = None
            continue
        if atual == "1" and linha.startswith("**1-NF"):
            atual = "1-NF"
            modelos[atual] = []
            continue
        if atual and linha.startswith(">"):
            modelos[atual].append(linha[1:].lstrip() if len(linha) > 1 else "")
    saida = {k: "\n".join(v).strip() for k, v in modelos.items() if any(x.strip() for x in v)}
    faltam = [k for k in MODELOS_PADRAO if k not in saida]
    if faltam:
        print(f"  AVISO: MSG-07 sem os modelos {faltam}; usando a copia embutida para eles.")
        for k in faltam:
            saida[k] = MODELOS_PADRAO[k]
    return saida


def aplicar_condicional_nota(texto: str, link_nota: str) -> str:
    """Modelo 6 traz '[Se a nota sai após o pagamento: "..."]'."""
    padrao = re.compile(r'\[Se a nota[^\]]*?"([^"]+)"\]')
    return padrao.sub(lambda m: m.group(1) if link_nota else "", texto).strip()


def escolher_marco(dias: int, marcos=(10, 5, 3, 0), tolerancia: int = 1):
    """Marco cuja janela [m - tolerancia, m] contem `dias`. Tolerancia cobre um dia em que o
    cron nao rodou (VPS fora do ar) sem mandar lembrete fora de hora."""
    for m in sorted(marcos):
        if m - tolerancia <= dias <= m:
            return m
    return None


def _primeiro_nome(nome: str) -> str:
    return (nome or "").strip().split(" ")[0].title()


def dados_mensagem(asaas: AsaasCliente, pagamento: dict, cfg: dict, cache_clientes: dict) -> tuple[dict, str, dict]:
    cid = pagamento.get("customer")
    if cid not in cache_clientes:
        cache_clientes[cid] = asaas.obter_cliente(cid) or {}
    cli_asaas = cache_clientes[cid]
    local = cliente_por_asaas(cid, cli_asaas.get("cpfCnpj")) or {}
    contato = local.get("contato_financeiro") or {}
    nome_contato = contato.get("nome") or ""
    if not nome_contato and len(so_digitos(cli_asaas.get("cpfCnpj"))) == 11:
        nome_contato = cli_asaas.get("name") or ""      # pessoa fisica: o proprio cliente
    telefone = contato.get("whatsapp") or cli_asaas.get("mobilePhone") or cli_asaas.get("phone") or ""
    dados = {
        "nome_cliente": _primeiro_nome(nome_contato),
        "empresa": local.get("nome") or cli_asaas.get("name") or "",
        "nome_escritorio": (cfg.get("escritorio") or {}).get("nome_comercial") or "",
        "referencia": (pagamento.get("description") or "").strip(),
        "valor": brl(pagamento.get("value")),
        "vencimento": data_br(pagamento.get("dueDate")),
        "link_pagamento": pagamento.get("invoiceUrl") or "",
        "link_nota": "",
    }
    return dados, telefone, local


def _link_nota(asaas: AsaasCliente, con, payment_id: str) -> str:
    row = con.execute("SELECT pdf_url FROM notas WHERE payment_id = ?", (payment_id,)).fetchone()
    if row and row["pdf_url"]:
        return row["pdf_url"]
    nota = asaas.nota_por_referencia(f"nf:{payment_id}")
    return (nota or {}).get("pdfUrl") or ""


def rodar(asaas: AsaasCliente, executar: bool, cfg: dict | None = None, ref: date | None = None) -> dict:
    cfg = cfg or escritorio()
    r = cfg.get("regua") or {}
    marcos = tuple(r.get("marcos") or (10, 5, 3, 0))
    tol = int(r.get("tolerancia_dias", 1))
    ref = ref or hoje()
    modelos = ler_modelos()
    con = db.conectar()
    cache: dict = {}
    resumo = {"enviadas": [], "puladas": [], "pendencias": []}

    def ja_enviado(pid, marco_txt):
        return db.ja_existe(con, "regua_envios", payment_id=pid, marco=marco_txt)

    def disparar(pagamento, marco_txt, modelo_id, extra_nf=False):
        dados, tel, local = dados_mensagem(asaas, pagamento, cfg, cache)
        pid = pagamento["id"]
        nf_quando = ((local.get("nf") or {}).get("quando") or "").lower()
        if extra_nf or modelo_id == "6":
            dados["link_nota"] = _link_nota(asaas, con, pid)
        texto = modelos[modelo_id]
        if modelo_id == "1" and nf_quando == "antes":
            if dados["link_nota"]:
                texto = texto + "\n\n" + modelos.get("1-NF", MODELOS_PADRAO["1-NF"])
            else:
                resumo["pendencias"].append(f"{pid}: cliente com NF ANTES do pagamento e nota ainda nao emitida "
                                            f"(rode nota_fiscal.py antes da regua)")
        if modelo_id == "6":
            texto = aplicar_condicional_nota(texto, dados["link_nota"] if nf_quando == "depois" else "")
        msg, faltando = mensageria.render(texto, dados)
        if faltando:
            resumo["pendencias"].append(f"{pid} ({dados['empresa'] or pagamento.get('customer')}): "
                                        f"mensagem {marco_txt} nao sai — faltam {faltando} "
                                        f"(cadastre em config/clientes.json)")
            return
        envio = mensageria.enviar(tel, msg, origem="regua", referencia=f"{pid}:{marco_txt}",
                                  titulo=f"Cobranca {marco_txt} - {dados['empresa']}", executar=executar, cfg=cfg)
        if envio.get("erro"):
            resumo["pendencias"].append(f"{pid}: {envio['erro']}")
            return
        resumo["enviadas"].append(f"{marco_txt} {pid} {dados['empresa']} R$ {dados['valor']} venc {dados['vencimento']}")
        if executar:
            db.gravar(con, "regua_envios", payment_id=pid, marco=marco_txt, canal=envio.get("modo"),
                      telefone=envio.get("telefone"), mensagem=msg)
            if dados["link_nota"] and dados["link_nota"] in msg:
                # o link da nota ja foi junto: nota_fiscal.py nao manda de novo
                con.execute("UPDATE notas SET enviada_em = ? WHERE payment_id = ? AND enviada_em IS NULL",
                            (envio.get("criado_em"), pid))
                con.commit()

    # 1) lembretes antes do vencimento
    ate = (ref + timedelta(days=max(marcos))).isoformat()
    for p in asaas.listar_cobrancas(status="PENDING", venc_de=ref.isoformat(), venc_ate=ate):
        dias = (date.fromisoformat(p["dueDate"][:10]) - ref).days
        m = escolher_marco(dias, marcos, tol)
        if m is None:
            continue
        marco_txt = "D0" if m == 0 else f"D-{m}"
        mais_urgentes = ["D0" if x == 0 else f"D-{x}" for x in marcos if x <= m]
        if any(ja_enviado(p["id"], x) for x in mais_urgentes):
            resumo["puladas"].append(f"{marco_txt} {p['id']} (ja enviado)")
            continue
        disparar(p, marco_txt, MODELO_DO_MARCO.get(m, "2"))

    # 2) pagamento recebido (ultimos 3 dias)
    if r.get("aviso_pagamento", True):
        de = (ref - timedelta(days=3)).isoformat()
        for st in ("RECEIVED", "CONFIRMED"):
            for p in asaas.listar_cobrancas(status=st, pago_de=de, pago_ate=ref.isoformat()):
                if ja_enviado(p["id"], "PAGO"):
                    continue
                disparar(p, "PAGO", "6")

    # 3) atraso — desligado ate a Dra. Lais confirmar
    if r.get("atraso_ativo"):
        for p in asaas.listar_cobrancas(status="OVERDUE"):
            atraso = (ref - date.fromisoformat(p["dueDate"][:10])).days
            for marco_a in sorted(r.get("atraso_marcos") or (1, 7)):
                if marco_a <= atraso <= marco_a + tol:
                    txt = f"ATRASO+{marco_a}"
                    if not ja_enviado(p["id"], txt):
                        disparar(p, txt, MODELO_DO_ATRASO.get(marco_a, "7"))
    return resumo


def main():
    utf8_stdout()
    ap = add_modo(argparse.ArgumentParser(description="Regua de cobranca propria (10/5/3/0 dias)"))
    ap.add_argument("--fixture", help="JSON offline no lugar da API do Asaas (teste)")
    ap.add_argument("--data", help="simula a data de referencia AAAA-MM-DD")
    a = ap.parse_args()
    if a.fixture and a.go:
        raise SystemExit("--fixture e so para teste: nao combina com --go")
    banner(a.go, "Regua de cobranca")
    ref = date.fromisoformat(a.data) if a.data else None
    cfg = escritorio()
    bloquear_exemplo(cfg, "escritorio", a.go)
    res = rodar(AsaasCliente(fixture=a.fixture), a.go, cfg=cfg, ref=ref)
    print(f"\nMensagens: {len(res['enviadas'])}")
    for x in res["enviadas"]:
        print("  -", x)
    if res["puladas"]:
        print(f"Puladas (ja enviadas): {len(res['puladas'])}")
    if res["pendencias"]:
        print("PENDENCIAS:")
        for x in res["pendencias"]:
            print("  !", x)


if __name__ == "__main__":
    main()
