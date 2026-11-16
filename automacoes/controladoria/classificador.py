# -*- coding: utf-8 -*-
"""Classificador de intimacoes por regras (sem IA), segundo a arvore do POP-OP-02.

Categorias (pedido do escritorio):
  MERO_ANDAMENTO | EMBARGOS_DE_DECLARACAO | AGRAVO | APELACAO | RECURSO_ORDINARIO | OUTROS
  OUTROS sempre vem com `subtipo`: intimacao_para_agir, custas, audiencia, citacao, acordao,
  recurso_inominado, interlocutoria_sem_recurso_imediato, nao_identificado.

Cada resultado traz: categoria, subtipo, peca sugerida, dias, contagem, base legal, ramo,
gatilho (o trecho que decidiu), confianca, `confirmar_advogado` e `tambem_cabe` (ex.: toda
sentenca/decisao abre embargos de declaracao em paralelo, 5 dias uteis, SE houver omissao,
contradicao, obscuridade ou erro material — quem decide e o advogado).

Ideias reaproveitadas de _BASE_SISTEMA_VIRGEM/.../controladoria_motor/classificador.py
(calibrado em 30 publicacoes reais): tirar os marcadores "(s)/(em)/(a)" do PJe, ignorar o
CABECALHO do PJe ("Fica V. Sa. intimado para tomar ciencia da Sentenca..." nao e a sentenca:
um despacho de arquivamento virou recurso ordinario por isso), ler prazo por extenso
("quinze dias") e "em N dias".

REGRA DE OURO DO POP: o agente SUGERE. Decisao, sentenca e acordao sempre vao para o advogado da
area confirmar (tarefa [CONFIRMAR CLASSIFICACAO] no mesmo dia).
"""
from __future__ import annotations

import re
import unicodedata

_MARCADOR = re.compile(r"\((?:s|a|as|os|em|m|ns|is|eis|ao|oes)\)")
_CAB_PJE = re.compile(r"fica.{0,140}?tomar ciencia d[aeo].{0,140}?(?:proferid[oa] nos autos|consta a seguir:|a seguir:)")

_EXTENSO = {"um": 1, "dois": 2, "tres": 3, "quatro": 4, "cinco": 5, "seis": 6, "sete": 7, "oito": 8,
            "nove": 9, "dez": 10, "doze": 12, "quinze": 15, "vinte": 20, "trinta": 30}
_NUM = r"(\d{1,3}|" + "|".join(sorted(_EXTENSO, key=len, reverse=True)) + r")"
_RE_DIAS = [
    re.compile(r"prazo ?:? ?(?:comum |sucessivo |legal |improrrogavel |de |)(?:de )?" + _NUM + r" ?(?:\([a-z ]+\) ?)?dias?"),
    re.compile(r"no prazo de " + _NUM + r"\b"),
    re.compile(r"\bem " + _NUM + r" ?(?:\([a-z ]+\) ?)?dias?\b"),
    re.compile(r"\b" + _NUM + r" ?\([a-z ]+\) ?dias?\b"),
]


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode()
    s = re.sub(r"<[^>]+>", " ", s)
    s = _MARCADOR.sub("", s)
    return re.sub(r"\s+", " ", s).lower().strip()


def dias_do_texto(t: str) -> int | None:
    for rx in _RE_DIAS:
        m = rx.search(t)
        if m:
            tok = m.group(1)
            n = int(tok) if tok.isdigit() else _EXTENSO.get(tok)
            if n and 1 <= n <= 90:
                return n
    return None


def ramo(tribunal: str, classe: str, texto: str) -> str:
    t, c = (tribunal or "").upper(), norm(classe)
    if "TRT" in t or t.startswith("TST") or "trabalh" in c or "reclamacao trabalhista" in c:
        return "trabalhista"
    if "juizado" in c or "juizado especial" in texto[:600]:
        return "juizado"
    return "civel"


def _tem(t: str, termos) -> str:
    for x in termos:
        if x in t:
            return x
    return ""


SENTENCA = ("julgo procedente", "julgo improcedente", "julgo parcialmente procedente", "julgo extinto",
            "julgo extinta", "extingo o processo", "resolvo o merito", "com resolucao do merito",
            "sem resolucao do merito", "ante o exposto, julgo", "pelo exposto, julgo", "isto posto, julgo",
            "homologo o acordo", "homologo, por sentenca", "julgo os pedidos")
ACORDAO = ("acordam os", "acordao", "acordam, ", "ementa:", "por unanimidade", "por maioria")
# So embargos DE DECLARACAO (embargos monitorios/a execucao sao outra coisa: caem em "intimacao para agir").
ED_PARTE_CONTRARIA = ("opostos embargos de declaracao", "embargos de declaracao opostos",
                      "sobre os embargos de declaracao", "parte embargada", "efeitos infringentes",
                      "efeito modificativo", "efeitos modificativos")
DECISAO = ("defiro", "indefiro", "decido", "concedo a tutela", "nego a tutela", "tutela de urgencia",
           "tutela provisoria", "liminar", "gratuidade", "desconsideracao da personalidade", "determino a penhora",
           "bloqueio", "sisbajud", "rejeito a impugnacao", "acolho a impugnacao", "inverto o onus",
           "redistribuo o onus", "homologo os calculos", "homologo o calculo", "rejeito os embargos",
           "acolho os embargos", "nego seguimento", "denego seguimento")
CONTRARRAZOES = ("contrarrazoes", "contrarrazoar", "contra-arrazoar", "contraminuta", "contraminutar",
                 "apelado para", "apelada para", "recorrido para", "recorrida para", "agravado para", "agravada para")
ROL_1015 = ("tutela", "liminar", "gratuidade", "desconsideracao da personalidade", "exibicao",
            "litisconsorte", "litisconsorcio", "intervencao de terceiro", "denunciacao", "chamamento",
            "onus da prova", "convencao de arbitragem", "efeito suspensivo")
FASE_EXECUCAO = ("cumprimento de sentenca", "execucao", "penhora", "liquidacao", "sisbajud", "bloqueio",
                 "inventario", "homologo os calculos", "homologo o calculo", "impugnacao aos calculos")
CUSTAS = ("recolha as custas", "recolhimento das custas", "recolher as custas", "preparo", "custas iniciais",
          "custas processuais", "diligencia do oficial", "guia de custas", "comprovar o recolhimento")
AUDIENCIA = ("designo audiencia", "audiencia de conciliacao", "audiencia de instrucao", "audiencia una",
             "audiencia designada", "pericia designada", "designo pericia", "nomeio perito", "audiencia para o dia")
CITACAO = ("cite-se o reu", "cite-se a re", "citacao do reu", "fica citado", "fica citada", "notificacao inicial",
           "apresentar contestacao", "apresente contestacao", "oferecer contestacao")
PARA_AGIR = ("manifeste-se", "manifestem-se", "manifestar-se", "junte", "juntar", "especifiquem", "especifique",
             "apresente", "apresentem", "replica", "emende", "emenda a inicial", "intime-se a parte autora para",
             "intime-se o autor para", "intime-se a parte requerida para", "comprove", "informe", "esclareca",
             "indique", "no prazo de")
ANDAMENTO = ("juntada", "conclusos", "concluso", "remetidos os autos", "remessa", "aguarde-se", "aguardem-se",
             "arquivem-se", "arquive-se", "certifico", "ato ordinatorio", "vista ao ministerio publico",
             "cumpra-se", "expeca-se", "cite-se", "intimem-se", "retornem os autos", "redistribua-se",
             "baixa definitiva", "transitou em julgado", "transito em julgado")


def _base(categoria, subtipo, peca, dias, base, ramo_, gatilho, conf, confirmar, contagem="uteis", tambem=None):
    return {"categoria": categoria, "subtipo": subtipo, "peca": peca, "dias": dias, "contagem": contagem,
            "base_legal": base, "ramo": ramo_, "gatilho": gatilho, "confianca": conf,
            "confirmar_advogado": confirmar, "tambem_cabe": tambem or []}


ED_PARALELO = {"peca": "Embargos de declaracao (se houver omissao, contradicao, obscuridade ou erro material)",
               "dias": 5, "base_legal": "CPC art. 1.023; CLT art. 897-A; Lei 9.099 art. 49"}


def classificar(texto: str, tribunal: str = "", classe: str = "", tipo_comunicacao: str = "") -> dict:
    t = norm(texto)
    corpo = _CAB_PJE.sub(" ", t)                 # le o dispositivo, nao a etiqueta do PJe
    r = ramo(tribunal, classe, corpo)
    dias_desp = dias_do_texto(corpo)

    # 1) parte contraria opos embargos: manifestacao/contrarrazoes aos ED
    g = _tem(corpo, ED_PARTE_CONTRARIA)
    if g and not _tem(corpo, SENTENCA):
        return _base("EMBARGOS_DE_DECLARACAO", "manifestacao_sobre_ed", "Manifestacao sobre embargos de declaracao",
                     dias_desp or 5, "CPC art. 1.023 §2o; CLT art. 897-A §2o", r, g, 0.8, True)

    # 2) sentenca
    g = _tem(corpo, SENTENCA)
    if g:
        if r == "trabalhista":
            return _base("RECURSO_ORDINARIO", "sentenca", "Recurso ordinario", 8, "CLT art. 895, I", r, g, 0.85,
                         True, tambem=[ED_PARALELO])
        if r == "juizado":
            return _base("OUTROS", "recurso_inominado", "Recurso inominado", 10,
                         "Lei 9.099/1995 arts. 42 e 12-A", r, g, 0.8, True, tambem=[ED_PARALELO])
        return _base("APELACAO", "sentenca", "Apelacao", 15, "CPC arts. 1.003 §5o e 1.009", r, g, 0.85, True,
                     tambem=[ED_PARALELO])

    # 3) acordao / decisao de relator
    g = _tem(corpo, ACORDAO)
    if g:
        return _base("OUTROS", "acordao", "Advogado avalia o recurso cabivel (RR/REsp/RE/agravo interno)", None,
                     "POP-OP-02, tabela de prazos", r, g, 0.7, True, tambem=[ED_PARALELO])

    # 4) custas, audiencia, citacao (antes da decisao: 'designo audiencia' nao e interlocutoria recorrivel)
    g = _tem(corpo, CUSTAS)
    if g:
        return _base("OUTROS", "custas", "Recolhimento de custas (POP-OP-01)", dias_desp or 5,
                     "prazo do despacho; sem prazo: CPC art. 218 §3o", r, g, 0.8, False)
    g = _tem(corpo, AUDIENCIA)
    if g:
        return _base("OUTROS", "audiencia", "Audiencia/pericia: agenda + preparo 5 dias uteis antes", None,
                     "data designada no despacho", r, g, 0.75, False)
    g = _tem(corpo, CITACAO)
    if g and ("citad" in corpo or "contestacao" in corpo or "notificacao inicial" in corpo):
        if r == "trabalhista":
            return _base("OUTROS", "citacao", "Contestacao trabalhista (ate a audiencia)", None,
                         "CLT arts. 841 e 847", r, g, 0.7, True)
        return _base("OUTROS", "citacao", "Contestacao", 15, "CPC art. 335", r, g, 0.7, True)

    # 5) contrarrazoes ao recurso da outra parte
    g = _tem(corpo, CONTRARRAZOES)
    if g:
        if r == "trabalhista":
            return _base("OUTROS", "contrarrazoes", "Contrarrazoes", 8, "CLT art. 900", r, g, 0.75, False)
        return _base("OUTROS", "contrarrazoes", "Contrarrazoes", 15, "CPC arts. 1.003 §5o e 1.010 §1o", r, g, 0.75,
                     False)

    # 6) decisao interlocutoria
    g = _tem(corpo, DECISAO)
    rol_ou_exec = _tem(corpo, ROL_1015) or _tem(corpo, FASE_EXECUCAO)
    if g in ("defiro", "indefiro", "decido") and not rol_ou_exec and dias_desp:
        g = ""          # "defiro o prazo de 15 dias": e intimacao para agir, nao decisao recorrivel
    if g:
        if g in ("nego seguimento", "denego seguimento"):
            if r == "trabalhista":
                return _base("AGRAVO", "agravo_de_instrumento", "Agravo de instrumento (destrancar recurso)", 8,
                             "CLT art. 897, b", r, g, 0.75, True, tambem=[ED_PARALELO])
            return _base("AGRAVO", "agravo_interno_ou_aresp", "Agravo (interno ou em recurso especial/extraordinario)",
                         15, "CPC arts. 1.021 e 1.042", r, g, 0.65, True, tambem=[ED_PARALELO])
        execucao = _tem(corpo, FASE_EXECUCAO)
        if r == "trabalhista":
            if execucao:
                return _base("AGRAVO", "agravo_de_peticao", "Agravo de peticao", 8, "CLT art. 897, a", r,
                             f"{g} + {execucao}", 0.7, True, tambem=[ED_PARALELO])
            return _base("OUTROS", "interlocutoria_sem_recurso_imediato",
                         "Registrar; nulidade na 1a oportunidade (CLT art. 795); advogado avalia MS", None,
                         "CLT art. 893 §1o; Sumula 214 TST", r, g, 0.6, True, tambem=[ED_PARALELO])
        if r == "juizado":
            return _base("OUTROS", "interlocutoria_sem_recurso_imediato",
                         "Juizado: em regra sem recurso contra interlocutoria (conferir)", None,
                         "Lei 9.099/1995", r, g, 0.55, True, tambem=[ED_PARALELO])
        rol = _tem(corpo, ROL_1015)
        if rol or execucao:
            return _base("AGRAVO", "agravo_de_instrumento", "Agravo de instrumento", 15,
                         "CPC arts. 1.003 §5o e 1.015" + (" paragrafo unico" if execucao and not rol else ""),
                         r, f"{g} + {rol or execucao}", 0.7, True, tambem=[ED_PARALELO])
        return _base("OUTROS", "interlocutoria_sem_recurso_imediato",
                     "Fora do rol do art. 1.015: impugnar em preliminar de apelacao (ou agravo por urgencia, Tema 988 STJ)",
                     None, "CPC art. 1.009 §1o", r, g, 0.55, True, tambem=[ED_PARALELO])

    # 7) intimacao para agir
    g = _tem(corpo, PARA_AGIR)
    if g or dias_desp:
        dias = dias_desp or 5
        base = "prazo do despacho" if dias_desp else (
            "CPC art. 218 §3o" if r != "trabalhista" else "sem prazo no despacho: conferir com o advogado (trabalhista)")
        return _base("OUTROS", "intimacao_para_agir", "Manifestacao/providencia determinada no despacho", dias,
                     base, r, g or f"prazo de {dias_desp} dias", 0.7 if dias_desp else 0.55,
                     not dias_desp or r == "trabalhista")

    # 8) mero andamento
    g = _tem(corpo, ANDAMENTO)
    if g:
        return _base("MERO_ANDAMENTO", "andamento", "Registrar como andamento (sem tarefa)", None,
                     "CPC art. 1.001 (despacho de mero expediente)", r, g, 0.75, False)

    return _base("OUTROS", "nao_identificado", "Ler a integra e classificar manualmente", None, "", r, "", 0.3, True)
