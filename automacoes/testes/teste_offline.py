# -*- coding: utf-8 -*-
"""Teste offline de todas as automacoes — nenhuma chamada de rede, nenhuma credencial.

Usa fixtures FICTICIAS (fixture_asaas.json, fixture_djen.json), banco temporario e data simulada.
Uso: python automacoes/testes/teste_offline.py
"""
from __future__ import annotations

import os
import sys
import tempfile
from datetime import date
from pathlib import Path

TMP = tempfile.mkdtemp(prefix="escritorio_teste_")
os.environ["ESCRITORIO_DADOS_DIR"] = TMP
os.environ["ESCRITORIO_HOJE"] = "2026-12-05"
for k in ("ASAAS_API_KEY", "ADVBOX_API_TOKEN", "INFINITUM_PUBLIC_TOKEN", "ZAPSIGN_API_TOKEN"):
    os.environ.pop(k, None)

AQUI = Path(__file__).resolve().parent
AUT = AQUI.parent
for p in (AUT, AUT / "financeiro", AUT / "controladoria", AUT / "drive", AUT / "rh"):
    sys.path.insert(0, str(p))

from comum.config import MODELOS_DIR, utf8_stdout  # noqa: E402

utf8_stdout()
FALHAS: list[str] = []


def chk(nome, cond, detalhe=""):
    print(f"  [{'ok' if cond else 'FALHA'}] {nome}{(' — ' + str(detalhe)) if detalhe and not cond else ''}")
    if not cond:
        FALHAS.append(nome)


def t_nomes():
    print("\n# nomes / convencao")
    from comum import nomes
    chk("CNJ formatado", nomes.formatar_cnj("08012345620268100040") == "0801234-56.2026.8.10.0040")
    chk("CNJ achado na legenda", nomes.achar_cnj("segue doc do proc 0801234-56.2026.8.10.0040 ok") ==
        "0801234-56.2026.8.10.0040")
    chk("nome de arquivo", nomes.nome_arquivo("guia custas", "Diligência oficial", "PDF", date(2026, 11, 16)) ==
        "2026-11-16_GUIA-CUSTAS_diligencia-oficial.pdf")
    chk("pasta de demanda", nomes.pasta_demanda("notificação fornecedor X", "2026-11-18") ==
        "2026-11-18 - NOTIFICAÇÃO FORNECEDOR X")


def t_mensageria():
    print("\n# mensageria")
    from comum import mensageria
    txt, falt = mensageria.render("Oi {{nome}}, link {{link}}", {"nome": "Ana"})
    chk("render mantem lacuna visivel", "{{link}}" in txt and falt == ["link"])
    chk("telefone 55", mensageria.telefone_whatsapp("(99) 99114-0000") == "5599991140000")


def t_regua():
    print("\n# regua de cobranca (fixture, 2026-12-05)")
    import regua_cobranca as rc
    from comum.asaas import AsaasCliente
    chk("marco 10", rc.escolher_marco(10) == 10)
    chk("marco 9 (tolerancia)", rc.escolher_marco(9) == 10)
    chk("dia 7 sem marco", rc.escolher_marco(7) is None)
    chk("marco 4 -> 5", rc.escolher_marco(4) == 5)
    chk("marco 0", rc.escolher_marco(0) == 0)
    mods = rc.ler_modelos()
    chk("MSG-07 lido (modelos 1,1-NF,2,3,4,6,7,8)", all(k in mods for k in ("1", "1-NF", "2", "3", "4", "6", "7", "8")),
        sorted(mods))
    chk("modelo 1 fala do DDA", "DDA" in mods["1"])
    chk("condicional da nota (sem nota)", "{{link_nota}}" not in rc.aplicar_condicional_nota(mods["6"], ""))
    chk("condicional da nota (com nota)", "nota fiscal" in rc.aplicar_condicional_nota(mods["6"], "x").lower())
    res = rc.rodar(AsaasCliente(fixture=str(AQUI / "fixture_asaas.json")), executar=False,
                   cfg={"regua": {}, "mensageria": {"modo": "fila"}}, ref=date(2026, 12, 5))
    env = " | ".join(res["enviadas"])
    chk("D-10 pay_T1", "D-10 pay_T1" in env, env)
    chk("D-5 pay_T2", "D-5 pay_T2" in env, env)
    chk("D0 pay_T4", "D0 pay_T4" in env, env)
    chk("PAGO pay_T6", "PAGO pay_T6" in env, env)
    chk("pay_T5 (7 dias) nao sai", "pay_T5" not in env)
    chk("PJ sem contato financeiro vira pendencia (nao sai com lacuna)",
        any("pay_T3" in p for p in res["pendencias"]), res["pendencias"])


def t_relatorio():
    print("\n# relatorio financeiro")
    import relatorio_diario as rd
    from comum.asaas import AsaasCliente
    d = rd.coletar(AsaasCliente(fixture=str(AQUI / "fixture_asaas.json")), date(2026, 12, 5))
    c = rd.consolidar(d)
    chk("entradas = recebido no mes", abs(c["entradas"] - 1500.0) < 0.01, c["entradas"])
    chk("saidas do extrato", abs(c["saidas"] - 1201.99) < 0.01, c["saidas"])
    chk("inadimplencia", abs(c["inadimplencia"] - 2000.0) < 0.01, c["inadimplencia"])
    chk("a receber ate fim do mes", abs(c["a_receber"] - (1500 + 800 + 2000 + 300 + 300)) < 0.01, c["a_receber"])
    md = rd.markdown(date(2026, 12, 5), d, c)
    chk("markdown com secoes", "## Inadimplentes" in md and "OFICINA FICTICIA" in md)
    xl = rd.planilha(Path(TMP) / "rel.xlsx", d, c)
    chk("planilha gerada", xl.exists())


def t_nova_cobranca():
    print("\n# nova cobranca")
    import nova_cobranca as nc
    chk("CNPJ valido", nc.valida_doc("11.222.333/0001-81"))
    chk("CNPJ invalido", not nc.valida_doc("11.222.333/0001-82"))
    chk("CPF valido", nc.valida_doc("000.000.001-91"))
    chk("31/01 + 1 mes = 28/02", nc.somar_meses(date(2026, 1, 31), 1) == date(2026, 2, 28))

    class A:
        assessoria, meses, competencia_anterior, parcelas, ref = True, 12, False, 1, ""
        vencimento, doc, valor, referencia = "2026-12-10", "11222333000181", 1500.0, "honorários de assessoria"
    plano = nc.planejar(A)
    chk("12 boletos", len(plano) == 12)
    chk("vencimentos mensais", plano[1]["vencimento"] == "2027-01-10" and plano[11]["vencimento"] == "2027-11-10")
    chk("referencias unicas (idempotencia)", len({p["ref"] for p in plano}) == 12)

    class B(A):
        assessoria, parcelas, valor, ref = False, 3, 1000.0, "ct-1"
    p2 = nc.planejar(B)
    chk("parcelas somam o total", abs(sum(x["valor"] for x in p2) - 1000.0) < 0.001, [x["valor"] for x in p2])


def t_nota():
    print("\n# nota fiscal")
    import nota_fiscal as nf
    falta = nf.fiscal_incompleto({})
    chk("fiscal vazio bloqueia", "municipalServiceName" in falta and "emitir_desde (data de corte)" in falta)
    p = nf.montar_payload({"id": "pay_X", "value": 100, "description": "honorários"},
                          {"municipalServiceName": "SERV", "municipalServiceCode": "1", "taxes": {"iss": 2}},
                          date(2026, 12, 5))
    chk("payload com externalReference nf:<id>", p["externalReference"] == "nf:pay_X" and p["payment"] == "pay_X")


def t_pagamentos():
    print("\n# pagamentos")
    import pagamentos as pg
    chk("sabado antecipa para sexta", pg.data_pagamento("2026-12", 5) == date(2026, 12, 4))
    chk("dia 31 em fevereiro", pg.data_pagamento("2027-02", 31, antecipar_fds=False) == date(2027, 2, 28))


def t_prazos_classificador():
    print("\n# prazos")
    import prazos
    chk("auto-teste do motor de prazos", prazos._testes())
    print("\n# classificador")
    import classificador as cl
    casos = [
        ("SENTENCA. Ante o exposto, JULGO PROCEDENTE o pedido.", "TJMA", "", "APELACAO", 15),
        ("Julgo parcialmente procedentes os pedidos e condeno a reclamada.", "TRT16", "", "RECURSO_ORDINARIO", 8),
        ("Fica V. Sa. intimado para tomar ciencia da Sentenca ID 1 proferida nos autos. Arquivem-se os autos.",
         "TRT16", "", "MERO_ANDAMENTO", None),
        ("DEFIRO a tutela de urgencia requerida.", "TJGO", "", "AGRAVO", 15),
        ("Homologo os calculos de liquidacao.", "TRT18", "", "AGRAVO", 8),
        ("Intime-se a parte autora para, no prazo de 10 (dez) dias, manifestar-se.", "TJMA", "", "OUTROS", 10),
        ("Intime-se a parte embargada para se manifestar sobre os embargos de declaracao.", "TJMA", "",
         "EMBARGOS_DE_DECLARACAO", 5),
        ("Recebo a apelacao. Intime-se o apelado para contrarrazoes.", "TJMA", "", "OUTROS", 15),
        ("Certifico a juntada da peticao. Conclusos.", "TJMA", "", "MERO_ANDAMENTO", None),
        ("Julgo improcedente o pedido.", "TJMA", "Procedimento do Juizado Especial Civel", "OUTROS", 10),
        ("Indefiro o pedido de producao de prova testemunhal.", "TJMA", "", "OUTROS", None),
    ]
    for texto, trib, classe, cat, dias in casos:
        r = cl.classificar(texto, trib, classe)
        chk(f"{cat:22} {dias!s:>4}  <- {texto[:45]}", r["categoria"] == cat and r["dias"] == dias,
            f"{r['categoria']}/{r['subtipo']}/{r['dias']}")
    r = cl.classificar("Julgo procedente o pedido.", "TJMA")
    chk("sentenca traz ED em paralelo e pede confirmacao", r["tambem_cabe"] and r["confirmar_advogado"])


def t_intimacoes():
    print("\n# controladoria (fixture DJEN, sem ADVBOX)")
    import json
    import intimacoes as it
    itens = json.loads((AQUI / "fixture_djen.json").read_text("utf-8"))["itens"]
    res = it.processar(itens, {"controladoria": {}, "advbox": {}}, executar=False)
    cats = {x["numero"]: x["c"]["categoria"] for x in res["linhas"] if not x.get("ja")}
    chk("6 intimacoes classificadas", len(cats) == 6, cats)
    chk("sentenca civel -> apelacao", cats.get("0000001-00.2026.8.10.0001") == "APELACAO", cats)
    chk("cabecalho PJe nao vira recurso", cats.get("0000003-00.2026.5.16.0001") == "MERO_ANDAMENTO", cats)
    chk("sem processo no ADVBOX vira pendencia", any("nao encontrado no ADVBOX" in p for p in res["pendencias"]))
    rel = it.relatorio(res, date(2026, 12, 5))
    chk("relatorio gerado", "| Processo |" in rel and "Pendências" in rel)


def t_drive():
    print("\n# drive / roteamento de documentos")
    import criar_estrutura as ce
    import documento_whatsapp as dw
    plano = ce.plano_base(2026)
    caminhos = {"/".join(p) for p in plano}
    chk("estrutura base", {"00_ESCRITORIO/POPS", "00_ESCRITORIO/MODELOS/RH", "FINANCEIRO/2026/12/RELATORIOS",
                           "CLIENTES", "RH"} <= caminhos)
    cli = {"nome": "Oficina Ficticia Ltda", "tipo": "assessoria", "area_padrao": "civel",
           "advbox": {"registro_assessoria_lawsuit_id": "999"},
           "processos": [{"numero": "0000001-00.2026.8.10.0001", "parte_contraria": "Fulano", "tipo_acao": "Cobranca",
                          "advbox_lawsuit_id": "111", "area": "civel"}],
           "demandas_extrajudiciais": [{"assunto": "notificacao fornecedor", "aberta_em": "2026-11-18",
                                        "palavras_chave": ["fornecedor x", "duplicata"], "advbox_lawsuit_id": ""}]}
    pc = "/".join(ce.plano_cliente(cli)[1])
    chk("cliente de assessoria tem pasta de diagnostico",
        any("04_ASSESSORIA_DIAGNOSTICO" in "/".join(p) for p in ce.plano_cliente(cli)), pc)
    r = dw.rotear(cli, "segue doc do processo 0000001-00.2026.8.10.0001", "foto.jpg")
    chk("CNJ -> pasta do processo", r["caminho"][-1] == "01_DOCUMENTOS_DO_CLIENTE" and r["lawsuit_id"] == "111", r)
    r = dw.rotear(cli, "duplicata do fornecedor X", "dup.pdf")
    chk("palavra-chave -> demanda (lawsuit = registro da assessoria)",
        "03_EXTRAJUDICIAL" in r["caminho"] and r["lawsuit_id"] == "999", r)
    r = dw.rotear(cli, "meu RG", "rg.jpg")
    chk("RG -> 01_CONTRATO_E_DOCUMENTOS", r["caminho"][-1] == "01_CONTRATO_E_DOCUMENTOS", r)
    r = dw.rotear(cli, "olha isso", "x.pdf")
    chk("sem pista -> 99_A_CLASSIFICAR", r["caminho"][-1] == "99_A_CLASSIFICAR", r)
    r = dw.rotear(None, "oi", "x.pdf")
    chk("telefone desconhecido -> ENTRADA_WHATSAPP", r["caminho"] == ["00_ESCRITORIO", "ENTRADA_WHATSAPP"])


def t_modelos_rh():
    print("\n# modelos / RH")
    from comum import modelos
    tmp = Path(TMP) / "m.md"
    tmp.write_text("notas {{nao_entra}}\n<!-- INICIO_DOCUMENTO -->\nOla {{nome}}.\n{{#extra}}Bloco {{valor}}.{{/extra}}\n"
                   "Fim.\n<!-- FIM_DOCUMENTO -->\n", encoding="utf-8")
    txt, falt = modelos.render(tmp, {"nome": "Ana"})
    chk("so o corpo entre os marcadores", "notas" not in txt and "Ola Ana." in txt)
    chk("bloco opcional removido", "Bloco" not in txt and falt == [])
    txt, falt = modelos.render(tmp, {"nome": "Ana", "extra": True})
    chk("bloco opcional incluido e campo faltando apontado", "Bloco" in txt and falt == ["valor"])
    chk("fiscal barra {{campo}}", bool(modelos.fiscal(txt)))
    chk("fiscal barra [A CONFIRMAR]", bool(modelos.fiscal("data [A CONFIRMAR]")))
    est = MODELOS_DIR / "09_termo_compromisso_estagio.md"
    if est.exists():
        txt, falt = modelos.render(est, {})
        chk("termo de estagio: campos detectados", "estagiario_nome" in falt and "ies_nome" in falt, falt[:5])
        docx = modelos.markdown_para_docx(txt, Path(TMP) / "termo.docx")
        chk("docx gerado", docx.exists() and docx.stat().st_size > 1000)
    else:
        print("  (modelos/09_termo_compromisso_estagio.md ainda nao existe — pulado)")
    import json
    ck = json.loads((AUT / "rh" / "checklists_vinculo.json").read_text("utf-8"))
    chk("checklist estagiario tem seguro e TCE", {"seguro", "contrato"} <= {d["chave"] for d in ck["estagiario"]["documentos"]})
    chk("checklist associado tem averbacao", "averbacao" in {d["chave"] for d in ck["associado"]["documentos"]})


if __name__ == "__main__":
    for t in (t_nomes, t_mensageria, t_regua, t_relatorio, t_nova_cobranca, t_nota, t_pagamentos,
              t_prazos_classificador, t_intimacoes, t_drive, t_modelos_rh):
        try:
            t()
        except Exception as e:  # noqa: BLE001
            import traceback
            traceback.print_exc()
            FALHAS.append(f"{t.__name__}: {e}")
    print(f"\n{'TUDO OK' if not FALHAS else str(len(FALHAS)) + ' FALHA(S): ' + '; '.join(FALHAS)}  (dados em {TMP})")
    sys.exit(1 if FALHAS else 0)
