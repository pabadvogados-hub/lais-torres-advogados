# -*- coding: utf-8 -*-
"""Gera documento a partir dos modelos em Markdown de modelos/ (formato da frente de modelos):

  - o texto do documento fica entre <!-- INICIO_DOCUMENTO --> e <!-- FIM_DOCUMENTO -->
    (o que vem antes e bloco de notas/instrucoes; sem os marcadores, usa o arquivo inteiro);
  - {{chave}} = campo;  {{#bloco}}...{{/bloco}} = trecho opcional (entra se dados[bloco] for
    verdadeiro);  {{^bloco}}...{{/bloco}} = entra se for falso;
  - campos comuns do escritorio ({{escritorio_*}}, {{lais_*}}) vem de escritorio.json -> modelos_comuns.

FISCAL (ideia de _BASE_SISTEMA_VIRGEM/INTEGRACOES/fiscal_documento.py, que nasceu de um contrato
assinado com os {{campos}} a mostra): documento com {{...}} sobrando, [A CONFIRMAR], [CONFERIR]
ou XXX nao vai para assinatura.
"""
from __future__ import annotations

import re
from pathlib import Path

_INI, _FIM = "<!-- INICIO_DOCUMENTO -->", "<!-- FIM_DOCUMENTO -->"
_SECAO = re.compile(r"\{\{([#^])\s*([\w.\-]+)\s*\}\}(.*?)\{\{/\s*\2\s*\}\}", re.S)
_CAMPO = re.compile(r"\{\{\s*([^{}#^/][^{}]*?)\s*\}\}")
_PROIBIDO = [(re.compile(r"\{\{[^}]*\}\}"), "campo {{...}} nao preenchido"),
             (re.compile(r"\[\s*A CONFIRMAR[^\]]*\]", re.I), "marca [A CONFIRMAR]"),
             (re.compile(r"\[\s*CONFERIR[^\]]*\]", re.I), "marca [CONFERIR]"),
             (re.compile(r"\bX{3,}\b"), "XXX no texto")]


def corpo_do_modelo(caminho: str | Path) -> str:
    txt = Path(caminho).read_text("utf-8")
    if _INI in txt and _FIM in txt:
        txt = txt.split(_INI, 1)[1].split(_FIM, 1)[0]
    return txt.strip() + "\n"


def campos_do_modelo(caminho: str | Path) -> list[str]:
    corpo = corpo_do_modelo(caminho)
    blocos = {m.group(2) for m in _SECAO.finditer(corpo)}
    campos = []
    for m in _CAMPO.finditer(_SECAO.sub(lambda s: s.group(3), corpo)):
        c = m.group(1).strip()
        if c not in campos:
            campos.append(c)
    return sorted(blocos) + [c for c in campos if c not in blocos]


def render(caminho: str | Path, dados: dict) -> tuple[str, list[str]]:
    texto = corpo_do_modelo(caminho)
    for _ in range(5):                       # blocos aninhados, se houver
        novo = _SECAO.sub(lambda m: m.group(3) if bool(dados.get(m.group(2))) == (m.group(1) == "#") else "", texto)
        if novo == texto:
            break
        texto = novo
    faltando = []

    def troca(m):
        c = m.group(1).strip()
        v = dados.get(c)
        if v is None or str(v).strip() == "":
            if c not in faltando:
                faltando.append(c)
            return m.group(0)
        return str(v)

    texto = _CAMPO.sub(troca, texto)
    texto = re.sub(r"\n{3,}", "\n\n", texto)      # bloco removido deixa linha em branco a mais
    return texto, faltando


def fiscal(texto: str) -> list[str]:
    achados = []
    for rx, motivo in _PROIBIDO:
        for m in rx.finditer(texto):
            achados.append(f"{motivo}: '{m.group(0)[:60]}'")
    return achados


def markdown_para_docx(texto_md: str, destino: str | Path) -> Path:
    """Conversao simples (titulos, negrito, paragrafos) — suficiente para contrato. Fonte e margens
    do papel timbrado do escritorio: [A CONFIRMAR] (POP-OP-05 item 21)."""
    from docx import Document
    from docx.shared import Pt

    doc = Document()
    estilo = doc.styles["Normal"]
    estilo.font.name = "Arial"
    estilo.font.size = Pt(11)
    for bloco in re.split(r"\n\s*\n", texto_md.strip()):
        linhas = [ln.rstrip() for ln in bloco.splitlines()]
        if not linhas:
            continue
        primeira = linhas[0]
        m = re.match(r"^(#{1,3})\s+(.*)$", primeira)
        if m and len(linhas) == 1:
            doc.add_heading(m.group(2).replace("**", ""), level=len(m.group(1)))
            continue
        p = doc.add_paragraph()
        for i, ln in enumerate(linhas):
            ln = ln.replace("&nbsp;", "").replace("\\_", "_")
            for j, parte in enumerate(re.split(r"\*\*", ln)):
                if parte:
                    p.add_run(parte).bold = (j % 2 == 1)
            if i < len(linhas) - 1:
                p.add_run().add_break()
    destino = Path(destino)
    doc.save(destino)
    return destino
