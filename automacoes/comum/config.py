# -*- coding: utf-8 -*-
"""Configuracao unica das automacoes.

Regra da casa:
  - config/.env            -> SO credenciais e caminhos (nunca versionar).
  - config/<nome>.json     -> parametros do escritorio (OABs, IDs do ADVBOX, regra de NF
                              por cliente, colaboradores, despesas). Dados pessoais: nunca versionar.
  - config/<nome>.example.json -> modelo versionado, sem dado real.

Todo script roda em DRY-RUN por padrao. So escreve em sistema externo (Asaas, ADVBOX,
Infinitum, Drive, ZapSign) com --go. E com --go o script RECUSA rodar em cima de um
.example.json: exemplo nunca vira cobranca, Pix ou tarefa de verdade.
"""
from __future__ import annotations

import json
import os
import sys
from datetime import date, datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]          # .../LAIS_TORRES_ADVOGADOS
CONFIG_DIR = RAIZ / "config"
AUTOMACOES_DIR = RAIZ / "automacoes"
MODELOS_DIR = RAIZ / "modelos"
MENSAGENS_DIR = RAIZ / "mensagens"
POPS_DIR = RAIZ / "pops"

try:
    from dotenv import load_dotenv
    load_dotenv(CONFIG_DIR / ".env")
except ImportError:  # sem python-dotenv o ambiente pode vir do systemd/cron
    pass

DADOS_DIR = Path(os.getenv("ESCRITORIO_DADOS_DIR") or (RAIZ / "dados"))
SAIDA_DIR = DADOS_DIR / "saida"


def utf8_stdout():
    """Console do Windows usa cp1252 e quebra acento vindo das APIs."""
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass


def garantir_dir(p: Path) -> Path:
    p.mkdir(parents=True, exist_ok=True)
    return p


_AVISADOS: set[str] = set()


def carregar_json(nome: str, obrigatorio: bool = False) -> dict:
    """Le config/<nome>.json. Se nao existir, cai no .example.json marcado com _EXEMPLO."""
    real = CONFIG_DIR / f"{nome}.json"
    if real.exists():
        return json.loads(real.read_text("utf-8"))
    exemplo = CONFIG_DIR / f"{nome}.example.json"
    if exemplo.exists():
        dados = json.loads(exemplo.read_text("utf-8"))
        if isinstance(dados, dict):
            dados["_EXEMPLO"] = True
        if nome not in _AVISADOS:
            _AVISADOS.add(nome)
            print(f"  AVISO: config/{nome}.json nao existe; usando {exemplo.name} (so serve para dry-run).")
        return dados
    if obrigatorio:
        raise SystemExit(f"ERRO: config/{nome}.json nao encontrado.")
    return {}


def escritorio() -> dict:
    return carregar_json("escritorio")


def bloquear_exemplo(cfg: dict, nome: str, executar: bool):
    """Com --go, recusa config de exemplo."""
    if executar and isinstance(cfg, dict) and cfg.get("_EXEMPLO"):
        raise SystemExit(f"ERRO: --go recusado: config/{nome}.json nao existe (so o exemplo). "
                         f"Copie {nome}.example.json para {nome}.json e preencha com os dados reais.")


def add_modo(parser):
    parser.add_argument("--go", action="store_true",
                        help="executa de verdade (sem isso, roda em dry-run e nao escreve em sistema externo)")
    return parser


def banner(executar: bool, titulo: str = ""):
    if executar:
        print(f"=== {titulo} — EXECUTANDO (--go): escreve em sistema externo ===")
    else:
        print(f"=== {titulo} — DRY-RUN: nada sera criado/enviado. Use --go para executar. ===")


def hoje() -> date:
    """Permite simular outra data nos testes: ESCRITORIO_HOJE=AAAA-MM-DD."""
    v = os.getenv("ESCRITORIO_HOJE")
    if v:
        return date.fromisoformat(v[:10])
    return date.today()


def agora_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def so_digitos(s) -> str:
    return "".join(c for c in str(s or "") if c.isdigit())


def brl(valor) -> str:
    """1234.5 -> '1.234,50' (o 'R$' fica no modelo da mensagem)."""
    try:
        v = float(valor or 0)
    except (TypeError, ValueError):
        return str(valor)
    s = f"{v:,.2f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def data_br(iso) -> str:
    if not iso:
        return ""
    try:
        return date.fromisoformat(str(iso)[:10]).strftime("%d/%m/%Y")
    except ValueError:
        return str(iso)
