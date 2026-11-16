# -*- coding: utf-8 -*-
"""Consulta ao DJEN / API Comunica do PJe-CNJ (gratuita, oficial) por OAB.

Copiado do modulo comunica_djen.py que o Casal da IA ja usa em producao (mesma logica de retry).
Endpoint: https://comunicaapi.pje.jus.br/api/v1/comunicacao (Swagger: cnj/pcp no SwaggerHub)

PEGADINHA (validada em producao): para a MESMA consulta a API alterna entre "sistema muito ocupado",
um falso-vazio (status success com count 0) e os dados certos. Por isso a 1a pagina trata o
vazio como retentavel, com backoff (ate 10 tentativas). Sem isso o robo diz "nenhuma intimacao"
com intimacao no diario.
"""
from __future__ import annotations

import time
from datetime import date

import requests

BASE_URL = "https://comunicaapi.pje.jus.br/api/v1/comunicacao"
HEADERS = {"User-Agent": "Mozilla/5.0 Escritorio-Controladoria/1.0", "Accept": "application/json"}
MAX_ITENS = 100
MAX_TENTATIVAS = 10


def _requisitar(params, exigir_dados=False):
    tentativa, espera = 0, 2.0
    while True:
        tentativa += 1
        motivo = None
        try:
            resp = requests.get(BASE_URL, params=params, headers=HEADERS, timeout=60)
            resp.raise_for_status()
            dados = resp.json()
        except (requests.RequestException, ValueError) as e:
            dados, motivo = None, f"rede/parse ({e})"
        else:
            if dados.get("status") == "error" and "ocupado" in (dados.get("message") or "").lower():
                motivo = "ocupado"
            elif exigir_dados and not (dados.get("items") or []):
                motivo = "falso-vazio"
        if motivo is None:
            return dados
        if tentativa >= MAX_TENTATIVAS:
            if dados is not None and dados.get("status") != "error":
                return dados          # vazio de verdade depois de 10 tentativas
            raise RuntimeError(f"API Comunica indisponivel apos {tentativa} tentativas ({motivo})")
        time.sleep(espera)
        espera = min(espera * 1.6, 20)


def consultar(oab_numero=None, oab_uf=None, numero_processo=None, data_inicio=None, data_fim=None, limite=None):
    hoje = date.today().isoformat()
    base = {"dataDisponibilizacaoInicio": str(data_inicio or hoje)[:10],
            "dataDisponibilizacaoFim": str(data_fim or hoje)[:10],
            "itensPorPagina": MAX_ITENS}
    if oab_numero:
        base["numeroOab"] = "".join(c for c in str(oab_numero) if c.isdigit())
    if oab_uf:
        base["ufOab"] = oab_uf.upper()
    if numero_processo:
        base["numeroProcesso"] = "".join(filter(str.isdigit, numero_processo))
    itens, pagina, total = [], 1, None
    while True:
        dados = _requisitar(dict(base, pagina=pagina), exigir_dados=(pagina == 1))
        if total is None:
            total = dados.get("count", 0)
        lote = dados.get("items") or []
        if not lote:
            break
        itens.extend(lote)
        if limite and len(itens) >= limite:
            return itens[:limite]
        if len(itens) >= total:
            break
        pagina += 1
        time.sleep(0.4)
    return itens


def resumir(item: dict) -> dict:
    advs = []
    for a in item.get("destinatarioadvogados") or []:
        adv = a.get("advogado", {})
        advs.append(f"{adv.get('nome', '')} (OAB {adv.get('numero_oab', '')}/{adv.get('uf_oab', '')})")
    return {
        "id": str(item.get("id") or item.get("hash") or ""),
        "data": (item.get("data_disponibilizacao") or "")[:10],
        "tribunal": item.get("siglaTribunal") or "",
        "orgao": item.get("nomeOrgao") or "",
        "tipo": item.get("tipoComunicacao") or "",
        "classe": item.get("nomeClasse") or "",
        "processo": item.get("numeroprocessocommascara") or item.get("numero_processo") or "",
        "partes": [d.get("nome", "") for d in item.get("destinatarios") or []],
        "advogados": advs,
        "link": item.get("link") or "",
        "texto": (item.get("texto") or "").strip(),
    }
