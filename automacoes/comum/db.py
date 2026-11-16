# -*- coding: utf-8 -*-
"""Banco local (SQLite) — o "banco de dados" que vai para a VPS e entra no backup semanal.

Guarda ESTADO, nao dado de negocio: o que ja foi enviado na regua, que nota ja foi
emitida, que Pix ja foi agendado, que intimacao ja virou tarefa, que documento ja foi
arquivado. E isso que torna todos os scripts idempotentes (rodar duas vezes nao duplica).

Em dry-run nada e gravado aqui.
"""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from .config import DADOS_DIR, agora_iso, garantir_dir

DB_PATH = DADOS_DIR / "escritorio.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS regua_envios (
    payment_id  TEXT NOT NULL,
    marco       TEXT NOT NULL,            -- D-10, D-5, D-3, D0, PAGO, ATRASO+1, ATRASO+7
    criado_em   TEXT NOT NULL,
    canal       TEXT,
    telefone    TEXT,
    mensagem    TEXT,
    PRIMARY KEY (payment_id, marco)
);
CREATE TABLE IF NOT EXISTS notas (
    payment_id  TEXT PRIMARY KEY,
    invoice_id  TEXT,
    status      TEXT,
    pdf_url     TEXT,
    criado_em   TEXT,
    enviada_em  TEXT
);
CREATE TABLE IF NOT EXISTS transferencias (
    favorecido_id TEXT NOT NULL,
    competencia   TEXT NOT NULL,          -- AAAA-MM
    transfer_id   TEXT,
    valor         REAL,
    schedule_date TEXT,
    status        TEXT,
    criado_em     TEXT,
    comprovante   TEXT,                   -- id/link no Drive
    PRIMARY KEY (favorecido_id, competencia)
);
CREATE TABLE IF NOT EXISTS controladoria (
    comunicacao_id TEXT PRIMARY KEY,
    processo       TEXT,
    categoria      TEXT,
    prazo_fatal    TEXT,
    prazo_interno  TEXT,
    tarefa         TEXT,
    criado_em      TEXT
);
CREATE TABLE IF NOT EXISTS documentos_recebidos (
    hash        TEXT PRIMARY KEY,
    cliente     TEXT,
    destino     TEXT,
    drive_id    TEXT,
    tarefa      TEXT,
    criado_em   TEXT
);
CREATE TABLE IF NOT EXISTS webhook_eventos (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    recebido_em TEXT NOT NULL,
    origem      TEXT,
    payload     TEXT
);
CREATE TABLE IF NOT EXISTS rh_eventos (
    colaborador TEXT NOT NULL,
    evento      TEXT NOT NULL,
    detalhe     TEXT,
    criado_em   TEXT NOT NULL
);
"""


def conectar(path: Path | None = None) -> sqlite3.Connection:
    p = Path(path or DB_PATH)
    garantir_dir(p.parent)
    con = sqlite3.connect(str(p))
    con.row_factory = sqlite3.Row
    con.executescript(SCHEMA)
    return con


def ja_existe(con, tabela: str, **chaves) -> bool:
    cond = " AND ".join(f"{k} = ?" for k in chaves)
    cur = con.execute(f"SELECT 1 FROM {tabela} WHERE {cond} LIMIT 1", tuple(chaves.values()))
    return cur.fetchone() is not None


def gravar(con, tabela: str, **campos):
    campos.setdefault("criado_em", agora_iso())
    cols = ", ".join(campos)
    marcas = ", ".join("?" for _ in campos)
    con.execute(f"INSERT OR REPLACE INTO {tabela} ({cols}) VALUES ({marcas})", tuple(campos.values()))
    con.commit()


def registrar_webhook(con, origem: str, payload) -> int:
    cur = con.execute(
        "INSERT INTO webhook_eventos (recebido_em, origem, payload) VALUES (?, ?, ?)",
        (agora_iso(), origem, json.dumps(payload, ensure_ascii=False)))
    con.commit()
    return cur.lastrowid
