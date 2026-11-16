# -*- coding: utf-8 -*-
"""Motor de prazos deterministico (nenhuma IA calcula data aqui).

Adaptado de _BASE_SISTEMA_VIRGEM/SISTEMA/backend/app/controladoria_motor/motor_prazos.py e
feriados.py (Pascoa, nacionais, suspensao 20/12-20/01, feriados locais em JSON), simplificado e
com as regras do POP-OP-02 deste escritorio:

  disponibilizacao no DJEN
    -> PUBLICACAO: 1o dia util seguinte                     (CPC art. 224 §2o; Lei 11.419 art. 4o §3o)
      -> INICIO: 1o dia util seguinte a publicacao          (CPC art. 224 §3o)
        -> conta N dias UTEIS (exclui o 1o, inclui o ultimo)  (CPC art. 219; CLT art. 775)
          -> VENCIMENTO = prazo fatal
            -> PRAZO INTERNO = fatal - 2 dias uteis (peca pronta)   (POP-OP-02 / README 4.5)
            -> PROTOCOLO     = fatal - 1 dia util

PRINCIPIO DE SEGURANCA (da base): na duvida, MENOS feriado. Feriado falso empurra o vencimento
para frente (perigoso); feriado omitido puxa para tras (seguro). Por isso feriados_locais.json
nasce VAZIO para MA/GO/TO/PA: so entra o que a controladoria conferir no calendario oficial do
tribunal (TJMA, TJGO, TJTO, TJPA, TRT16, TRT18, TRT10, TRT8, TRF1). Carnaval e Corpus Christi
contam como dia util, com AVISO.

CLI:  python automacoes/controladoria/prazos.py --disp 2026-11-10 --dias 15 --tribunal TJMA
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from datetime import date, datetime, timedelta
from functools import lru_cache
from pathlib import Path

_LOCAIS_PATH = Path(__file__).with_name("feriados_locais.json")

NACIONAIS_FIXOS = {
    "01-01": "Confraternizacao Universal", "04-21": "Tiradentes", "05-01": "Dia do Trabalho",
    "09-07": "Independencia", "10-12": "N. Sra. Aparecida", "11-02": "Finados",
    "11-15": "Proclamacao da Republica", "11-20": "Consciencia Negra (Lei 14.759/2023)", "12-25": "Natal",
}

_TRT_UF = {"1": "RJ", "2": "SP", "3": "MG", "4": "RS", "5": "BA", "6": "PE", "7": "CE", "8": "PA",
           "9": "PR", "10": "DF", "11": "AM", "12": "SC", "13": "PB", "14": "RO", "15": "SP", "16": "MA",
           "17": "ES", "18": "GO", "19": "AL", "20": "SE", "21": "RN", "22": "PI", "23": "MT", "24": "MS"}


def _norm(s: str) -> str:
    return unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().strip().lower()


def _locais() -> dict:
    try:
        return json.loads(_LOCAIS_PATH.read_text("utf-8"))
    except (OSError, ValueError):
        return {}


@lru_cache(maxsize=64)
def pascoa(ano: int) -> date:
    a, b, c = ano % 19, ano // 100, ano % 100
    d, e = b // 4, b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    l_ = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l_) // 451
    mes = (h + l_ - 7 * m + 114) // 31
    dia = ((h + l_ - 7 * m + 114) % 31) + 1
    return date(ano, mes, dia)


@lru_cache(maxsize=256)
def feriados_do_ano(ano: int, uf: str = "", comarca: str = "") -> dict:
    out = {}
    for mmdd, nome in NACIONAIS_FIXOS.items():
        mm, dd = mmdd.split("-")
        out[date(ano, int(mm), int(dd))] = nome
    out[pascoa(ano) - timedelta(days=2)] = "Sexta-feira Santa"
    loc = _locais()
    for mmdd in (loc.get("UF") or {}).get(uf, []):
        mm, dd = mmdd.split("-")
        out.setdefault(date(ano, int(mm), int(dd)), f"Feriado estadual {uf}")
    if comarca:
        for mmdd in (loc.get("COMARCA") or {}).get(f"{uf}:{comarca}", []):
            mm, dd = mmdd.split("-")
            out.setdefault(date(ano, int(mm), int(dd)), f"Feriado {comarca}/{uf}")
    for chave in (uf, f"{uf}:{comarca}" if comarca else ""):
        for iso, nome in ((loc.get("DATAS") or {}).get(chave) or {}).items() if chave else ():
            try:
                d = date.fromisoformat(iso[:10])
            except ValueError:
                continue
            if d.year == ano:
                out.setdefault(d, nome or f"Suspensao {chave}")
    return out


def feriado_nacional(d: date) -> str | None:
    return feriados_do_ano(d.year).get(d)


def em_suspensao(d: date) -> bool:
    """20/12 a 20/01 (CPC art. 220; CLT art. 775-A)."""
    return (d.month == 12 and d.day >= 20) or (d.month == 1 and d.day <= 20)


def eh_dia_util(d: date, uf: str = "", comarca: str = "") -> bool:
    return d.weekday() < 5 and not em_suspensao(d) and d not in feriados_do_ano(d.year, uf, _norm(comarca))


def proximo_dia_util(d: date, uf="", comarca="", incluir_hoje=False) -> date:
    cur = d if incluir_hoje else d + timedelta(days=1)
    while not eh_dia_util(cur, uf, comarca):
        cur += timedelta(days=1)
    return cur


def dia_util_interno(d: date) -> bool:
    """Calendario da casa: seg-sex fora dos feriados nacionais (sem suspensao forense)."""
    return d.weekday() < 5 and d not in feriados_do_ano(d.year)


def uteis_antes(d: date, n: int) -> date:
    while n > 0:
        d -= timedelta(days=1)
        if dia_util_interno(d):
            n -= 1
    return d


def ponto_facultativo(d: date) -> str | None:
    p = pascoa(d.year)
    return {p - timedelta(days=48): "Carnaval (segunda)", p - timedelta(days=47): "Carnaval (terca)",
            p + timedelta(days=60): "Corpus Christi"}.get(d)


def uf_do_tribunal(tribunal: str) -> str:
    t = _norm(tribunal).upper().replace(" ", "")
    m = re.match(r"TRT0?(\d{1,2})", t)
    if m:
        return _TRT_UF.get(str(int(m.group(1))), "")
    if t in ("TJDFT", "TJDF") or t.startswith(("TST", "STJ", "STF")):
        return "DF"
    if t.startswith("TJ") and len(t) >= 4:
        return t[2:4]
    return ""          # TRF1 e outros federais: varias UFs -> so feriado nacional + aviso


def para_data(v) -> date | None:
    if isinstance(v, date):
        return v
    s = str(v or "").strip()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(s[:10], fmt).date()
        except ValueError:
            pass
    return None


def calcular(disponibilizacao, dias: int | None, tribunal: str = "", uf: str = "", comarca: str = "",
             contagem: str = "uteis", folga_interna: int = 2) -> dict:
    disp = para_data(disponibilizacao)
    if disp is None:
        return {"erro": "data de disponibilizacao invalida", "avisos": []}
    avisos = []
    uf = uf or uf_do_tribunal(tribunal)
    if not uf:
        avisos.append("UF nao identificada pelo tribunal: so feriados nacionais aplicados — conferir calendario local")
    t = _norm(tribunal).upper()
    if t.startswith("TRT10"):
        avisos.append("TRT10 abrange DF e TO: conferir feriado local do Tocantins")
    publicacao = proximo_dia_util(disp, uf, comarca)
    inicio = proximo_dia_util(publicacao, uf, comarca)
    if em_suspensao(disp) or em_suspensao(publicacao):
        avisos.append("Disponibilizada na suspensao de 20/12 a 20/01: contagem so a partir de 21/01")
    out = {"disponibilizacao": disp.isoformat(), "publicacao": publicacao.isoformat(),
           "inicio_contagem": inicio.isoformat(), "uf": uf, "contagem": contagem, "avisos": avisos}
    if not dias:
        out.update(dias=None, prazo_fatal=None, prazo_interno=None, protocolo=None)
        return out
    if contagem == "corridos":
        venc = inicio + timedelta(days=int(dias) - 1)
        if not eh_dia_util(venc, uf, comarca):
            venc = proximo_dia_util(venc, uf, comarca, incluir_hoje=True)
    else:
        venc, n = inicio, 1
        while n < int(dias):
            venc = proximo_dia_util(venc, uf, comarca)
            n += 1
    cur = disp
    while cur <= venc:
        pf = ponto_facultativo(cur)
        if pf and cur.weekday() < 5:
            avisos.append(f"{pf} ({cur.isoformat()}) contado como dia util: conferir se o tribunal suspendeu")
        cur += timedelta(days=1)
    out.update(dias=int(dias), prazo_fatal=venc.isoformat(),
               prazo_interno=uteis_antes(venc, folga_interna).isoformat(),
               protocolo=uteis_antes(venc, 1).isoformat())
    return out


def _testes():
    ok = True

    def chk(nome, got, esp):
        nonlocal ok
        bom = got == esp
        ok &= bom
        print(f"  [{'ok' if bom else 'FALHA'}] {nome}: {got} (esperado {esp})")

    r = calcular("2026-08-14", 15, tribunal="TJMA")          # sexta
    chk("publicacao apos sexta", r["publicacao"], "2026-08-17")
    chk("inicio", r["inicio_contagem"], "2026-08-18")
    r2 = calcular("2026-03-02", 5, tribunal="TJGO")           # segunda
    chk("5 uteis", r2["prazo_fatal"], "2026-03-10")
    chk("interno = fatal - 2 uteis", r2["prazo_interno"], "2026-03-06")
    chk("protocolo = fatal - 1 util", r2["protocolo"], "2026-03-09")
    chk("TRT16 -> MA", uf_do_tribunal("TRT16"), "MA")
    chk("TRT18 -> GO", uf_do_tribunal("TRT18"), "GO")
    chk("TJTO -> TO", uf_do_tribunal("TJTO"), "TO")
    r3 = calcular("2026-11-19", 5, tribunal="TJMA")           # quinta; 20/11 feriado nacional
    chk("pula Consciencia Negra", r3["publicacao"], "2026-11-23")
    chk("data em dd/mm/aaaa", calcular("19/11/2026", 5)["publicacao"], "2026-11-23")
    return ok


def main():
    ap = argparse.ArgumentParser(description="Calcula prazo processual (dias uteis, DJEN)")
    ap.add_argument("--disp", help="data de disponibilizacao no DJEN")
    ap.add_argument("--dias", type=int)
    ap.add_argument("--tribunal", default="")
    ap.add_argument("--uf", default="")
    ap.add_argument("--corridos", action="store_true")
    ap.add_argument("--teste", action="store_true")
    a = ap.parse_args()
    if a.teste or not a.disp:
        raise SystemExit(0 if _testes() else 1)
    print(json.dumps(calcular(a.disp, a.dias, a.tribunal, a.uf, contagem="corridos" if a.corridos else "uteis"),
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
