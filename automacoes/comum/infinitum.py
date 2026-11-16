# -*- coding: utf-8 -*-
"""Cliente da API PUBLICA do Infinitum (adaptado do infinitum_integration.py do Casal da IA,
sem token nem IDs de outra organizacao).

Base: https://public.infinitum.app.br/api/v1/public · Auth: header X-Public-Token
(env INFINITUM_PUBLIC_TOKEN). Doc: docs.infinitum.app.br.

O QUE A API PUBLICA PERMITE (testado pelo Casal da IA em 05-09/2026 com token real):
  - ler organizacao, POPs, fases, campos (pop-fields), cards;
  - criar card (POST /cards: organization_id, pop_id, phase_id, title, values[{field_id, value}]);
  - atualizar values do card (PUT /cards/{id}: SUBSTITUI a lista inteira -> sempre fazer merge);
  - mover card (PUT /cards/{id}/move com {"new_phase_id": ..., "position": 0}; position obrigatorio);
  - grupos Finance (Asaas), Tasks, Databases/Records, Pop Automations.
  NAO HA ENDPOINT PUBLICO PARA ENVIAR MENSAGEM DE WHATSAPP NEM PARA LER O HISTORICO DE CONVERSAS.

COMO ENVIAMOS WHATSAPP PELO INFINITUM, ENTAO: por CARD + AUTOMACAO NATIVA.
  O script cria um card num POP "ENVIOS AUTOMATICOS" com os campos telefone e mensagem; no
  Infinitum, uma automacao do POP ("Sempre que um card for criado" -> "Envie WhatsApp da
  organizacao") dispara a mensagem. [A CONFERIR NA TELA DO INFINITUM: se a acao "Envie WhatsApp"
  aceita o TELEFONE e o TEXTO vindos dos campos do card. Se nao aceitar, o modo fica em "fila"
  e a equipe envia a fila gerada.]
"""
from __future__ import annotations

import os
import time

import requests

BASE = (os.getenv("INFINITUM_BASE_URL") or "https://public.infinitum.app.br/api/v1/public").rstrip("/")


def _headers():
    token = os.getenv("INFINITUM_PUBLIC_TOKEN")
    if not token:
        raise RuntimeError("INFINITUM_PUBLIC_TOKEN ausente em config/.env")
    return {"X-Public-Token": token.strip(), "Content-Type": "application/json",
            "Accept": "application/json", "User-Agent": "Escritorio-LaisTorres-Automacoes/1.0"}


def req(method, endpoint, params=None, json_data=None, retries=2):
    url = BASE + endpoint
    for tentativa in range(retries + 1):
        try:
            r = requests.request(method, url, headers=_headers(), params=params, json=json_data, timeout=30)
        except requests.exceptions.RequestException as e:
            if tentativa < retries:
                time.sleep(3)
                continue
            raise RuntimeError(f"Infinitum conexao: {e}")
        if r.status_code == 429:
            time.sleep(int(r.headers.get("Retry-After", 10)))
            continue
        if r.status_code >= 500 and tentativa < retries:
            time.sleep(3)
            continue
        if r.status_code >= 400:
            raise RuntimeError(f"Infinitum {method} {endpoint} -> HTTP {r.status_code}: {r.text[:300]}")
        return r.json() if r.text else {}
    return {}


def desembrulhar(resp):
    if isinstance(resp, list):
        return resp
    if isinstance(resp, dict):
        for k in ("data", "cards", "items", "results"):
            if isinstance(resp.get(k), list):
                return resp[k]
    return []


def minha_organizacao():
    return req("GET", "/organizations/my")


def listar_pops(org_id):
    return desembrulhar(req("GET", f"/organizations/{org_id}/pops", params={"limit": 100}))


def obter_pop(pop_id):
    return req("GET", f"/pops/{pop_id}")


def campos_do_pop(pop_id):
    return desembrulhar(req("GET", "/pop-fields/by-pop", params={"pop_id": pop_id, "limit": 200}))


def listar_cards(org_id, pop_id=None, limit=100, max_paginas=200):
    saida, pagina = [], 1
    while pagina <= max_paginas:
        params = {"organization_id": org_id, "limit": limit, "page": pagina}
        if pop_id:
            params["pop_id"] = pop_id
        lote = desembrulhar(req("GET", "/cards", params=params))
        saida.extend(lote)
        if len(lote) < limit:
            break
        pagina += 1
    return saida


def obter_card(card_id):
    return req("GET", f"/cards/{card_id}")


def criar_card(org_id, pop_id, phase_id, titulo, values, executar=False):
    payload = {"organization_id": org_id, "pop_id": pop_id, "phase_id": phase_id,
               "title": titulo[:200], "values": values}
    if not executar:
        return {"_dry_run": True, "_endpoint": "POST /cards", "_payload": payload}
    return req("POST", "/cards", json_data=payload)


def card_id_do_payload(payload):
    """O webhook nativo do Infinitum manda o id do card em chaves variadas e aninhadas."""
    if isinstance(payload, dict):
        for k in ("card_id", "cardId", "cardID"):
            if payload.get(k):
                return str(payload[k])
        for k in ("card", "data", "payload"):
            achado = card_id_do_payload(payload.get(k))
            if achado:
                return achado
        if payload.get("id") and ("title" in payload or "values" in payload or "phase_id" in payload):
            return str(payload["id"])
    elif isinstance(payload, list):
        for item in payload:
            achado = card_id_do_payload(item)
            if achado:
                return achado
    return None


def valores_do_card(card: dict) -> dict:
    """{label normalizado: valor} a partir de values[] (field_label/value)."""
    out = {}
    for v in (card or {}).get("values") or []:
        rotulo = str(v.get("field_label") or v.get("label") or v.get("field_id") or "").strip().lower()
        if rotulo:
            out[rotulo] = v.get("value")
    return out
