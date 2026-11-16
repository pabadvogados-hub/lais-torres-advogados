# -*- coding: utf-8 -*-
"""Convencao de nomes de pasta e arquivo do Drive (explicada em automacoes/drive/ESTRUTURA_DRIVE.md).

Arquivo:  AAAA-MM-DD_TIPO_descricao-curta.ext        ex.: 2026-11-16_GUIA-CUSTAS_diligencia-oficial.pdf
Peca:     TIPO DA PECA - CLIENTE - N DO PROCESSO - AAAA-MM-DD.docx   (minuta: prefixo "MINUTA - ")
Pasta de cliente:   NOME EM MAIUSCULAS (razao social ou nome completo), sem / \\ : * ? " < > |
Pasta de processo:  <numero CNJ> - <parte contraria> - <tipo de acao>
Pasta de demanda:   AAAA-MM-DD - <assunto curto>      (extrajudicial: uma pasta por demanda)
Colaborador:        NOME COMPLETO - VINCULO
"""
from __future__ import annotations

import re
import unicodedata
from datetime import date

_PROIBIDOS = re.compile(r'[\\/:*?"<>|\r\n\t]+')
RE_CNJ = re.compile(r"\b(\d{7})-?(\d{2})\.?(\d{4})\.?(\d)\.?(\d{2})\.?(\d{4})\b")


def sem_acento(s: str) -> str:
    return unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode()


def limpar(s: str, maximo: int = 120) -> str:
    s = _PROIBIDOS.sub(" ", str(s or ""))
    s = re.sub(r"\s+", " ", s).strip(" .-")
    return s[:maximo].rstrip()


def slug(s: str, maximo: int = 60) -> str:
    s = sem_acento(s).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:maximo].rstrip("-") or "documento"


def tipo_doc(s: str) -> str:
    s = sem_acento(s).upper()
    return re.sub(r"[^A-Z0-9]+", "-", s).strip("-")[:30] or "DOC"


def nome_arquivo(tipo: str, descricao: str, ext: str, quando: date | str | None = None) -> str:
    d = quando if isinstance(quando, str) else (quando or date.today()).isoformat()
    ext = (ext or "").lstrip(".").lower()
    base = f"{str(d)[:10]}_{tipo_doc(tipo)}_{slug(descricao)}"
    return f"{base}.{ext}" if ext else base


def nome_peca(tipo: str, cliente: str, processo: str, quando: date | None = None, minuta=False) -> str:
    d = (quando or date.today()).isoformat()
    base = f"{limpar(tipo).upper()} - {limpar(cliente).upper()} - {formatar_cnj(processo) or limpar(processo)} - {d}"
    return ("MINUTA - " + base) if minuta else base


def pasta_cliente(nome: str) -> str:
    return limpar(nome).upper()


def pasta_processo(numero: str, parte_contraria: str = "", tipo_acao: str = "") -> str:
    partes = [formatar_cnj(numero) or limpar(numero)]
    if parte_contraria:
        partes.append(limpar(parte_contraria, 50).upper())
    if tipo_acao:
        partes.append(limpar(tipo_acao, 40).upper())
    return " - ".join(partes)


def pasta_demanda(assunto: str, quando: date | str | None = None) -> str:
    d = quando if isinstance(quando, str) else (quando or date.today()).isoformat()
    return f"{str(d)[:10]} - {limpar(assunto, 60).upper()}"


def pasta_colaborador(nome: str, vinculo: str) -> str:
    return f"{limpar(nome).upper()} - {limpar(vinculo).upper()}"


def achar_cnj(texto: str) -> str:
    m = RE_CNJ.search(texto or "")
    return "{}-{}.{}.{}.{}.{}".format(*m.groups()) if m else ""


def formatar_cnj(numero: str) -> str:
    d = "".join(c for c in str(numero or "") if c.isdigit())
    if len(d) != 20:
        return ""
    return f"{d[:7]}-{d[7:9]}.{d[9:13]}.{d[13]}.{d[14:16]}.{d[16:]}"
