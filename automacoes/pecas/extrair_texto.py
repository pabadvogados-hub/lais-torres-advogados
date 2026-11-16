# -*- coding: utf-8 -*-
"""Extrai o texto de uma peca (.docx, .pdf, .md, .txt) para o agente revisor-pecas ler.

Mostra os paragrafos numerados ([P12] ...), para o parecer apontar ONDE esta cada problema,
e lista os numeros CNJ, artigos de lei e citacoes de jurisprudencia/sumula encontrados — a
lista de conferencia humana do POP-OP-05 (itens 3, 8 e 9).

Uso: python automacoes/pecas/extrair_texto.py "MINUTA - CONTESTACAO - ....docx" [--saida texto.txt]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from comum.config import utf8_stdout  # noqa: E402
from comum.nomes import RE_CNJ  # noqa: E402

RE_ART = re.compile(r"\bart(?:igo)?s?\.?\s*\d+[\w\-ºo°]*(?:[^.;\n]{0,40}?(?:CPC|CLT|CC|CF|CDC|CTN|Lei\s+n?º?\s*[\d.]+/\d{2,4}))?", re.I)
RE_JURIS = re.compile(r"\b(?:S[úu]mula(?:\s+Vinculante)?\s+n?º?\s*\d+(?:\s+do\s+\w+)?|OJ\s+n?º?\s*\d+[^.;\n]{0,30}|"
                      r"(?:REsp|AREsp|RE|ARE|AgInt|AgRg|RR|AIRR|RO|ROT|AP|HC|MS|ADI|ADC|ADPF|Tema)\s*n?º?\s*[\d.\-/]+)", re.I)


def paragrafos(caminho: Path) -> list[str]:
    suf = caminho.suffix.lower()
    if suf == ".docx":
        from docx import Document
        return [p.text.strip() for p in Document(str(caminho)).paragraphs if p.text.strip()]
    if suf == ".pdf":
        try:
            from pypdf import PdfReader
        except ImportError:
            raise SystemExit("para PDF instale pypdf (pip install pypdf)")
        texto = "\n".join((pg.extract_text() or "") for pg in PdfReader(str(caminho)).pages)
        return [b.strip() for b in re.split(r"\n\s*\n", texto) if b.strip()]
    return [b.strip() for b in re.split(r"\n\s*\n", caminho.read_text("utf-8")) if b.strip()]


def main():
    utf8_stdout()
    ap = argparse.ArgumentParser()
    ap.add_argument("arquivo")
    ap.add_argument("--saida")
    a = ap.parse_args()
    ps = paragrafos(Path(a.arquivo))
    corpo = "\n\n".join(f"[P{i}] {p}" for i, p in enumerate(ps, 1))
    tudo = "\n".join(ps)
    extra = ["", "=== PARA CONFERENCIA HUMANA ===",
             "Numeros de processo: " + (", ".join(sorted({"{}-{}.{}.{}.{}.{}".format(*m.groups())
                                                          for m in RE_CNJ.finditer(tudo)})) or "nenhum"),
             "Dispositivos citados: " + ("; ".join(sorted({m.group(0).strip() for m in RE_ART.finditer(tudo)})) or "nenhum"),
             "Jurisprudencia/sumulas/temas citados (CONFERIR NA FONTE OFICIAL): " +
             ("; ".join(sorted({m.group(0).strip() for m in RE_JURIS.finditer(tudo)})) or "nenhum")]
    saida = corpo + "\n" + "\n".join(extra) + "\n"
    if a.saida:
        Path(a.saida).write_text(saida, encoding="utf-8")
        print(f"Salvo em {a.saida} ({len(ps)} paragrafos)")
    else:
        print(saida)


if __name__ == "__main__":
    main()
