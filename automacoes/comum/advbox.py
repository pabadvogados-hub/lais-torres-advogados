# -*- coding: utf-8 -*-
"""Cliente da API ADVBOX (adaptado do cliente ADVBOX que o Casal da IA ja usa em producao, sem
nenhum ID de outro escritorio: remetente, tipos de tarefa e responsaveis vem de config/escritorio.json).

Base: https://app.advbox.com.br/api/v1 · Auth: Bearer (env ADVBOX_API_TOKEN)
Limites: 30 GET/minuto, 500 POST/dia por rota, 500 PUT/dia.
Doc para IA: http://api.softwareadvbox.com.br/llms-full.txt (conferida em 16/11/2026).

O QUE A API PERMITE CRIAR (conferido na doc):
  POST /posts         tarefa  -> obrigatorios: from, guests, tasks_id, lawsuits_id, start_date
                                  opcionais:   start_time, end_date, end_time, date_deadline, local,
                                               comments, urgent, important, display_schedule
                       ** lawsuits_id e OBRIGATORIO: nao existe tarefa sem processo. **
                       Por isso cada cliente de assessoria precisa de um registro "processo" de
                       assessoria/consultivo no ADVBOX para pendurar as tarefas extrajudiciais,
                       e o escritorio precisa de um registro "ADMINISTRATIVO" para tarefas de
                       RH/financeiro (IDs em config/escritorio.json -> advbox).
  POST /customers     cliente -> users_id, customers_origins_id, name (+ opcionais)
  POST /lawsuits      processo-> users_id, customers_id[], stages_id, type_lawsuits_id
  POST /lawsuits/movement     -> lawsuit_id, date (DD/MM/AAAA), description (>= 10 caracteres)
  POST /transactions  lancamento financeiro
  NAO EXISTE upload de documento: GET /documents e GET /documents/{id}/download sao so leitura
  (o download devolve uma temporary_url de S3 que expira em 300 s).
"""
from __future__ import annotations

import os
import time

import requests

BASE = "https://app.advbox.com.br/api/v1"
_ultimo_get = [0.0]
_INTERVALO_GET = 2.1   # 30 GET/min
_settings = {"dados": None, "ts": 0.0}


def _headers():
    token = os.getenv("ADVBOX_API_TOKEN")
    if not token:
        raise RuntimeError("ADVBOX_API_TOKEN ausente em config/.env")
    return {"Authorization": f"Bearer {token.strip()}", "Content-Type": "application/json",
            "Accept": "application/json", "User-Agent": "Escritorio-LaisTorres-Automacoes/1.0"}


def req(method, endpoint, params=None, json_data=None, retries=2):
    """Devolve o JSON; levanta RuntimeError com o texto do ADVBOX em caso de erro."""
    if method == "GET":
        espera = _INTERVALO_GET - (time.time() - _ultimo_get[0])
        if espera > 0:
            time.sleep(espera)
        _ultimo_get[0] = time.time()
    url = BASE + endpoint
    ultimo = ""
    for tentativa in range(retries + 1):
        try:
            r = requests.request(method, url, headers=_headers(), params=params, json=json_data, timeout=40)
        except requests.exceptions.RequestException as e:
            ultimo = f"conexao: {e}"
            time.sleep(3)
            continue
        if r.status_code == 429:
            time.sleep(int(r.headers.get("Retry-After", 15)))
            continue
        if r.status_code >= 500 and tentativa < retries:
            time.sleep(3)
            continue
        if r.status_code >= 400:
            raise RuntimeError(f"ADVBOX {method} {endpoint} -> HTTP {r.status_code}: {r.text[:300]}")
        return r.json() if r.text else {}
    raise RuntimeError(f"ADVBOX {method} {endpoint} falhou: {ultimo}")


def settings(force=False) -> dict:
    """GET /settings (usuarios, tipos de tarefa em 'tasks', fases, tipos de processo, financeiro)."""
    if not force and _settings["dados"] and time.time() - _settings["ts"] < 3600:
        return _settings["dados"]
    d = req("GET", "/settings") or {}
    fin = d.get("financial")
    if isinstance(fin, dict):
        for k in ("banks", "categories", "cost_centers", "departments"):
            d.setdefault(k, fin.get(k, []))
    _settings.update(dados=d, ts=time.time())
    return d


def buscar_processo(numero_processo) -> list[dict]:
    d = req("GET", "/lawsuits", params={"process_number": numero_processo})
    return d.get("data", []) if isinstance(d, dict) else []


def buscar_cliente(nome=None, identificacao=None) -> list[dict]:
    params = {}
    if nome:
        params["name"] = nome
    if identificacao:
        params["identification"] = identificacao
    d = req("GET", "/customers", params=params)
    return d.get("data", []) if isinstance(d, dict) else []


def ultimas_movimentacoes(lawsuit_id) -> list[dict]:
    d = req("GET", "/last_movements", params={"lawsuit_id": lawsuit_id, "limit": 20, "offset": 0})
    return d.get("data", []) if isinstance(d, dict) else []


def criar_tarefa(lawsuit_id, tasks_id, guests, from_id, comments, start_date,
                 end_date=None, date_deadline=None, urgent=False, executar=False) -> dict:
    """POST /posts. Em dry-run devolve o payload. `from` precisa ir como string (licao de producao)."""
    if not lawsuit_id:
        return {"erro": "ADVBOX exige lawsuits_id para criar tarefa (configure o processo/registro)"}
    if not tasks_id or not from_id or not guests:
        return {"erro": "faltam IDs do ADVBOX (tasks_id / from / guests) em config/escritorio.json"}
    payload = {
        "lawsuits_id": str(lawsuit_id),
        "start_date": str(start_date)[:10],
        "from": str(from_id),
        "guests": [str(g) for g in (guests if isinstance(guests, list) else [guests])],
        "tasks_id": str(tasks_id),
        "comments": comments,
    }
    if end_date:
        payload["end_date"] = str(end_date)[:10]
    if date_deadline:
        payload["date_deadline"] = str(date_deadline)[:10]
    if urgent:
        payload["urgent"] = True
        payload["important"] = True
    if not executar:
        return {"_dry_run": True, "_endpoint": "POST /posts", "_payload": payload}
    return req("POST", "/posts", json_data=payload)


def listar_documentos(customer_id=None, post_id=None, nome=None, limit=1000) -> list[dict]:
    """GET /documents (exige ao menos um filtro). Itens: id, name, size, links.download,
    attached_to{type,id,label}, uploaded_at."""
    params = {"limit": limit, "offset": 0}
    if customer_id:
        params["customer_id"] = customer_id
    if post_id:
        params["post_id"] = post_id
    if nome:
        params["name"] = nome
    saida = []
    while True:
        d = req("GET", "/documents", params=params)
        lote = d.get("data", []) if isinstance(d, dict) else []
        saida.extend(lote)
        if len(saida) >= int(d.get("totalCount") or 0) or not lote:
            break
        params["offset"] += limit
    return saida


def url_temporaria_documento(doc: dict) -> str:
    """Usa links.download (recomendado pela doc) e devolve a temporary_url (vale 5 minutos)."""
    link = ((doc.get("links") or {}).get("download")) or f"/documents/{doc.get('id')}/download"
    endpoint = link.split("/api/v1", 1)[-1] if link.startswith("http") else link
    d = req("GET", endpoint)
    return ((d or {}).get("data") or {}).get("temporary_url", "")


def listar_clientes(limit=100) -> list[dict]:
    saida, offset = [], 0
    while True:
        d = req("GET", "/customers", params={"limit": limit, "offset": offset})
        lote = d.get("data", []) if isinstance(d, dict) else []
        saida.extend(lote)
        if len(saida) >= int(d.get("totalCount") or 0) or not lote:
            break
        offset += limit
    return saida
