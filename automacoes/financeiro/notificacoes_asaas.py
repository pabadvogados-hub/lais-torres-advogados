# -*- coding: utf-8 -*-
"""Confere e DESLIGA as notificacoes do Asaas dos clientes que ja existem na conta.

Clientes novos ja nascem com notificationDisabled=true (nova_cobranca.py). Os que foram
criados antes (pelo app ou pela integracao com o ADVBOX) estao com os avisos ligados — foram
eles que dispararam os 12 avisos. Rodar UMA vez na implantacao, e depois so para conferir.

Doc Asaas ("Alterando notificacoes de um cliente"): GET /customers/{id}/notifications e
PUT /notifications/batch {customer, notifications:[{id, enabled:false}]}. Com enabled=false a
notificacao nao sai por nenhum canal (e-mail, SMS, WhatsApp, ligacao).

Uso:
    python automacoes/financeiro/notificacoes_asaas.py            # so lista quem tem aviso ligado
    python automacoes/financeiro/notificacoes_asaas.py --go       # desliga
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from comum.asaas import AsaasCliente  # noqa: E402
from comum.config import add_modo, banner, utf8_stdout  # noqa: E402


def main():
    utf8_stdout()
    ap = add_modo(argparse.ArgumentParser(description="Desliga as notificacoes do Asaas de todos os clientes"))
    ap.add_argument("--cliente", help="so este customer id (cus_...)")
    a = ap.parse_args()
    banner(a.go, "Notificacoes do Asaas")
    asaas = AsaasCliente()
    clientes = [asaas.obter_cliente(a.cliente)] if a.cliente else asaas.listar("/customers")
    total_lig = 0
    for c in clientes:
        if not c or c.get("deleted"):
            continue
        notifs = asaas.notificacoes_do_cliente(c["id"])
        ligadas = [n for n in notifs if n.get("enabled")]
        if not ligadas:
            continue
        total_lig += len(ligadas)
        eventos = ", ".join(sorted({n.get("event", "?") for n in ligadas}))
        print(f"  {c['id']}  {c.get('name', '')[:40]:40}  {len(ligadas)} ligada(s): {eventos}")
        r = asaas.desligar_notificacoes(c["id"], executar=a.go)
        if a.go:
            print(f"      -> {'desligadas' if r.get('ok') else 'FALHOU: ' + str(r)}")
    print(f"\nTotal de notificacoes ligadas encontradas: {total_lig}")
    if not a.go and total_lig:
        print("Rode com --go para desligar.")
    print("Na conta: confira tambem em Minha Conta > Notificacoes se ha aviso padrao para clientes novos.")


if __name__ == "__main__":
    main()
