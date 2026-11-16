# -*- coding: utf-8 -*-
"""Pagamento da equipe e das despesas fixas pelo Asaas (POP-ADM-02).

FAVORECIDOS: o Asaas nao tem um cadastro de "favorecido" pela API — cada transferencia leva a
chave Pix. O cadastro fica em config/colaboradores.json (equipe: chave Pix informada pelo
PROPRIO colaborador no formulario do RH) e config/despesas_fixas.json (aluguel, sistemas...).

COMO FUNCIONA A AUTORIZACAO POR TOKEN (conferido na doc do Asaas em 16/11/2026):
  - A transferencia criada pela API (POST /v3/transfers) com `scheduleDate` fica agendada.
  - Se a conta tiver a "validacao de eventos criticos" por Token (App Asaas ou SMS) ligada, a
    transferencia fica PENDENTE ate alguem autorizar: o campo `authorized` vem false
    ("false quando aguarda autorizacao atraves do Token SMS", referencia da API) e o FAQ de
    transferencias diz "a transferencia pode permanecer pendente ate a autorizacao".
    E esse o "acordar e aprovar o token": a Dra. Lais abre o app/painel do Asaas, ve o Pix e
    aprova com o token. NADA sai sem esse toque humano.
  - Alternativa da doc ("Mecanismo para validacao de saque via webhooks"): o Asaas chama uma URL
    nossa e a nossa aplicacao aprova/recusa. NAO usamos: tiraria a aprovacao humana.
  - Recomendado pela doc ("Mecanismos de seguranca"): cadastrar o IP da VPS na whitelist de IPs
    da chave de API (requisicao de outro IP recebe 403).
  [A CONFERIR NA CONTA DELES: se a validacao por token esta ligada para transferencias via API
   e por qual canal o token chega (app ou SMS). A doc diz que "a necessidade do token depende da
   operacao, das configuracoes da conta e do endpoint". Homologar no sandbox, onde o token e 000000.]
  - O Asaas tambem aceita Pix recorrente (`recurring`: MONTHLY, ate 11 repeticoes). Nao usamos:
    agendar mes a mes deixa aumento, desconto e desligamento sob controle.

Subcomandos:
  agendar      --mes AAAA-MM   cria os Pix agendados do mes (equipe + despesas por Pix)
  aviso-do-dia                 manda a Dra. Lais a lista do que sai hoje + saldo; cria a tarefa no ADVBOX
  saldo        [--dias 2]      avisa se o saldo nao cobre os pagamentos dos proximos N dias
  comprovantes --mes AAAA-MM   baixa os comprovantes dos Pix concluidos e arquiva no Drive
  boleto       --despesa ID --linha ... --data AAAA-MM-DD   agenda pagamento de boleto (POST /bill)
  listar       --mes AAAA-MM   mostra o que esta agendado e o status

Tudo em dry-run sem --go.
"""
from __future__ import annotations

import argparse
import sys
from datetime import date, timedelta
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from comum import advbox, db, mensageria  # noqa: E402
from comum.asaas import AsaasCliente  # noqa: E402
from comum.cadastros import (colaborador_por_id, colaboradores, despesas, lista_colaboradores,  # noqa: E402
                             lista_despesas, pasta_do_colaborador)
from comum.config import (add_modo, banner, bloquear_exemplo, brl, data_br, escritorio, hoje,  # noqa: E402
                          utf8_stdout)

TIPOS_CHAVE = ("CPF", "CNPJ", "EMAIL", "PHONE", "EVP")


def data_pagamento(mes: str, dia: int, antecipar_fds=True) -> date:
    ano, m = (int(x) for x in mes.split("-"))
    import calendar
    d = date(ano, m, min(int(dia), calendar.monthrange(ano, m)[1]))
    if antecipar_fds:
        while d.weekday() >= 5:          # sabado/domingo -> sexta (Pix funciona, mas a equipe recebe antes)
            d -= timedelta(days=1)
    return d


def favorecidos(mes: str, cfg: dict) -> list[dict]:
    antecipar = (cfg.get("pagamentos") or {}).get("antecipar_fim_de_semana", True)
    out = []
    for c in lista_colaboradores():
        p = c.get("pagamento") or {}
        if not p.get("ativo"):
            continue
        out.append({"id": f"colab:{c['id']}", "nome": c.get("nome"), "tipo": "colaborador", "colab": c,
                    "valor": p.get("valor"), "dia": p.get("dia"), "chave": p.get("pix_chave"),
                    "tipo_chave": (p.get("pix_tipo") or "").upper(),
                    "descricao": p.get("descricao") or f"Pagamento {mes} - {c.get('nome', '')}"})
    for d in lista_despesas():
        if (d.get("forma") or "").lower() != "pix":
            continue
        out.append({"id": f"desp:{d['id']}", "nome": d.get("favorecido") or d.get("descricao"), "tipo": "despesa",
                    "desp": d, "valor": d.get("valor"), "dia": d.get("dia"), "chave": d.get("pix_chave"),
                    "tipo_chave": (d.get("pix_tipo") or "").upper(),
                    "descricao": f"{d.get('descricao', '')} {mes}".strip()})
    for f in out:
        f["problemas"] = [x for x, ok in (("valor", f["valor"]), ("dia", f["dia"]), ("chave Pix", f["chave"]),
                                          ("tipo da chave", f["tipo_chave"] in TIPOS_CHAVE)) if not ok]
        if not f["problemas"]:
            f["data"] = data_pagamento(mes, f["dia"], antecipar)
    return out


def cmd_agendar(a, asaas, cfg, con):
    total = 0.0
    for f in favorecidos(a.mes, cfg):
        if f["problemas"]:
            print(f"  ! {f['id']} {f['nome']}: cadastro incompleto ({', '.join(f['problemas'])}) — nao agendado")
            continue
        if db.ja_existe(con, "transferencias", favorecido_id=f["id"], competencia=a.mes):
            print(f"  = {f['id']} {f['nome']}: ja agendado para {a.mes}")
            continue
        quando = max(f["data"], hoje())
        resp, erros = asaas.criar_pix(f["valor"], f["chave"], f["tipo_chave"], f["descricao"],
                                      data_agendada=quando.isoformat(), external_reference=f"{f['id']}:{a.mes}",
                                      executar=a.go)
        if erros:
            print(f"  ERRO {f['id']} {f['nome']}: {'; '.join(erros)}")
            continue
        total += float(f["valor"])
        print(f"  {'[dry-run] ' if not a.go else ''}{data_br(quando.isoformat())}  R$ {brl(f['valor']):>10}  "
              f"{f['nome']}  ({f['tipo_chave']})  {resp.get('id', '')} authorized={resp.get('authorized', '-')}")
        if a.go:
            db.gravar(con, "transferencias", favorecido_id=f["id"], competencia=a.mes, transfer_id=resp.get("id"),
                      valor=float(f["valor"]), schedule_date=quando.isoformat(), status=resp.get("status"))
    print(f"\nTotal agendado para {a.mes}: R$ {brl(total)}")
    print("Cada Pix so sai depois da aprovacao com token no app/painel do Asaas (se a validacao estiver ligada).")


def _do_dia(con, dia: str):
    return con.execute("SELECT * FROM transferencias WHERE schedule_date = ?", (dia,)).fetchall()


def cmd_aviso_do_dia(a, asaas, cfg, con):
    dia = hoje().isoformat()
    linhas, total = [], 0.0
    for row in _do_dia(con, dia):
        t = asaas.obter_transferencia(row["transfer_id"]) if row["transfer_id"] else {}
        nome = row["favorecido_id"]
        if nome.startswith("colab:"):
            nome = (colaborador_por_id(nome[6:]) or {}).get("nome") or nome
        total += float(row["valor"] or 0)
        situacao = "aguardando token" if t.get("authorized") is False else (t.get("status") or row["status"] or "?")
        linhas.append(f"- {nome}: R$ {brl(row['valor'])} ({situacao})")
    if not linhas:
        print("Nada agendado para hoje.")
        return
    saldo = asaas.saldo()
    texto = (f"Pagamentos de hoje ({data_br(dia)}), para aprovar no Asaas com o token:\n" + "\n".join(linhas) +
             f"\nTotal: R$ {brl(total)} | Saldo Asaas: R$ {brl(saldo) if saldo is not None else 'indisponível'}")
    if saldo is not None and saldo < total:
        texto += "\nATENÇÃO: o saldo não cobre o total do dia."
    print(texto)
    mensageria.enviar((cfg.get("aprovador") or {}).get("whatsapp"), texto, origem="pagamentos",
                      referencia=dia, executar=a.go, cfg=cfg)
    adv = cfg.get("advbox") or {}
    r = advbox.criar_tarefa(adv.get("processo_administrativo_id"), (adv.get("tipos_tarefa") or {}).get("financeiro"),
                            [(adv.get("responsaveis") or {}).get("financeiro")], adv.get("usuario_robo_id"),
                            f"[FINANCEIRO] Aprovar pagamentos do dia - {data_br(dia)}\n\n{texto}",
                            start_date=dia, date_deadline=dia, executar=a.go)
    print("  ADVBOX:", r)


def cmd_saldo(a, asaas, cfg, con):
    ate = (hoje() + timedelta(days=a.dias)).isoformat()
    rows = con.execute("SELECT * FROM transferencias WHERE schedule_date BETWEEN ? AND ? "
                       "AND (status IS NULL OR status NOT IN ('DONE','CANCELLED','FAILED'))",
                       (hoje().isoformat(), ate)).fetchall()
    total = sum(float(r["valor"] or 0) for r in rows)
    saldo = asaas.saldo()
    print(f"Pagamentos ate {data_br(ate)}: R$ {brl(total)} | saldo: R$ {brl(saldo) if saldo is not None else '?'}")
    if saldo is not None and saldo < total:
        texto = (f"Aviso do financeiro: os pagamentos agendados até {data_br(ate)} somam R$ {brl(total)} e o saldo "
                 f"do Asaas é R$ {brl(saldo)}. Faltam R$ {brl(total - saldo)}.")
        mensageria.enviar((cfg.get("aprovador") or {}).get("whatsapp"), texto, origem="pagamentos_saldo",
                          referencia=ate, executar=a.go, cfg=cfg)


def cmd_comprovantes(a, asaas, cfg, con):
    from comum import drive
    from comum.nomes import nome_arquivo
    raiz = (cfg.get("drive") or {}).get("raiz_id")
    svc = drive.servico() if (raiz and drive.credenciais_disponiveis()) else None
    if not svc:
        print("  Drive indisponivel (sem raiz_id ou credencial): so listo.")
    ano, mes = a.mes.split("-")
    for row in con.execute("SELECT * FROM transferencias WHERE competencia = ?", (a.mes,)).fetchall():
        t = asaas.obter_transferencia(row["transfer_id"]) if row["transfer_id"] else {}
        if a.go and t.get("status"):
            con.execute("UPDATE transferencias SET status=? WHERE favorecido_id=? AND competencia=?",
                        (t["status"], row["favorecido_id"], a.mes))
            con.commit()
        if t.get("status") != "DONE" or row["comprovante"]:
            print(f"  {row['favorecido_id']}: {t.get('status') or row['status']} "
                  f"{'(comprovante ja arquivado)' if row['comprovante'] else ''}")
            continue
        url = t.get("transactionReceiptUrl")
        if not url:
            print(f"  {row['favorecido_id']}: concluido mas sem transactionReceiptUrl")
            continue
        # [A CONFERIR] o link do Asaas pode ser pagina HTML do comprovante, nao PDF: guardamos o que vier.
        conteudo, mime, ext = b"", "text/html", "html"
        if a.go:
            r = requests.get(url, timeout=60)
            conteudo = r.content
            if conteudo[:4] == b"%PDF":
                mime, ext = "application/pdf", "pdf"
        if row["favorecido_id"].startswith("colab:"):
            c = colaborador_por_id(row["favorecido_id"][6:]) or {"nome": row["favorecido_id"]}
            caminho = ["RH", pasta_do_colaborador(c), "03_PAGAMENTOS"]
            nome = f"{a.mes}_comprovante.{ext}"
        else:
            caminho = ["FINANCEIRO", ano, mes, "COMPROVANTES"]
            nome = nome_arquivo("COMPROVANTE", row["favorecido_id"].split(":", 1)[-1], ext,
                                quando=(t.get("effectiveDate") or row["schedule_date"]))
        print(f"  {row['favorecido_id']}: comprovante -> {'/'.join(caminho)}/{nome}")
        if svc and a.go:
            pid = drive.garantir_caminho(svc, raiz, caminho, executar=True)
            f = drive.enviar_bytes(svc, conteudo, nome, pid, mime, executar=True)
            con.execute("UPDATE transferencias SET comprovante=? WHERE favorecido_id=? AND competencia=?",
                        (f.get("webViewLink") or f.get("id"), row["favorecido_id"], a.mes))
            con.commit()


def cmd_boleto(a, asaas, cfg, con):
    d = next((x for x in lista_despesas(ativas=False) if x.get("id") == a.despesa), None)
    if not d:
        raise SystemExit(f"despesa {a.despesa} nao esta em config/despesas_fixas.json")
    resp, erros = asaas.pagar_boleto(a.linha, a.data, descricao=d.get("descricao", ""), executar=a.go)
    print(erros or resp)


def cmd_listar(a, asaas, cfg, con):
    for row in con.execute("SELECT * FROM transferencias WHERE competencia = ? ORDER BY schedule_date",
                           (a.mes,)).fetchall():
        print(f"  {row['schedule_date']}  R$ {brl(row['valor']):>10}  {row['favorecido_id']:30} {row['status']} "
              f"{row['transfer_id'] or ''}")
    print("\nPlano do mes (cadastro):")
    for f in favorecidos(a.mes, cfg):
        print(f"  {f.get('data', '-')}  R$ {brl(f['valor'] or 0):>10}  {f['id']:30} "
              f"{'INCOMPLETO: ' + ', '.join(f['problemas']) if f['problemas'] else 'ok'}")


def main():
    utf8_stdout()
    ap = argparse.ArgumentParser(description="Pix agendado da equipe e despesas fixas (POP-ADM-02)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    proximo = (hoje().replace(day=1) + timedelta(days=32)).strftime("%Y-%m")
    for nome in ("agendar", "comprovantes", "listar"):
        s = add_modo(sub.add_parser(nome))
        s.add_argument("--mes", default=proximo if nome == "agendar" else hoje().strftime("%Y-%m"))
    add_modo(sub.add_parser("aviso-do-dia"))
    s = add_modo(sub.add_parser("saldo"))
    s.add_argument("--dias", type=int, default=2)
    s = add_modo(sub.add_parser("boleto"))
    s.add_argument("--despesa", required=True)
    s.add_argument("--linha", required=True, help="linha digitavel")
    s.add_argument("--data", required=True, help="data do pagamento AAAA-MM-DD")
    a = ap.parse_args()
    banner(a.go, f"Pagamentos: {a.cmd}")
    cfg = escritorio()
    bloquear_exemplo(cfg, "escritorio", a.go)
    if a.cmd == "agendar":
        bloquear_exemplo(colaboradores(), "colaboradores", a.go)
        bloquear_exemplo(despesas(), "despesas_fixas", a.go)
    con = db.conectar()
    {"agendar": cmd_agendar, "aviso-do-dia": cmd_aviso_do_dia, "saldo": cmd_saldo,
     "comprovantes": cmd_comprovantes, "boleto": cmd_boleto, "listar": cmd_listar}[a.cmd](a, AsaasCliente(), cfg, con)


if __name__ == "__main__":
    main()
