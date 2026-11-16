# -*- coding: utf-8 -*-
"""Leitura dos cadastros locais (config/clientes.json, colaboradores.json, despesas_fixas.json).

Esses arquivos tem dado pessoal (CPF, chave Pix, telefone): ficam fora do Git (.gitignore) e
entram no backup cifrado da VPS.
"""
from __future__ import annotations

from .config import carregar_json, so_digitos


def clientes() -> dict:
    return carregar_json("clientes")


def lista_clientes() -> list[dict]:
    return clientes().get("clientes") or []


def cliente_por_asaas(customer_id: str = "", cpf_cnpj: str = "") -> dict | None:
    doc = so_digitos(cpf_cnpj)
    for c in lista_clientes():
        if customer_id and c.get("asaas_customer_id") == customer_id:
            return c
        if doc and so_digitos(c.get("cpf_cnpj")) == doc:
            return c
    return None


def cliente_por_telefone(telefone: str) -> dict | None:
    alvo = so_digitos(telefone)[-11:]
    if len(alvo) < 10:
        return None
    for c in lista_clientes():
        fones = list(c.get("whatsapps") or [])
        fones.append((c.get("contato_financeiro") or {}).get("whatsapp"))
        for f in fones:
            d = so_digitos(f)[-11:]
            # celular gravado com ou sem o 9 extra: compara os 8 ultimos + DDD
            if d and (d == alvo or (d[:2] == alvo[:2] and d[-8:] == alvo[-8:])):
                return c
    return None


def cliente_por_id(cid: str) -> dict | None:
    for c in lista_clientes():
        if c.get("id") == cid:
            return c
    return None


def colaboradores() -> dict:
    return carregar_json("colaboradores")


def lista_colaboradores(ativos=True) -> list[dict]:
    out = []
    for c in colaboradores().get("colaboradores") or []:
        if ativos and c.get("desligado_em"):
            continue
        out.append(c)
    return out


def colaborador_por_id(cid: str) -> dict | None:
    for c in colaboradores().get("colaboradores") or []:
        if c.get("id") == cid:
            return c
    return None


VINCULO_ROTULO = {"estagiario": "ESTAGIARIO", "associado": "ASSOCIADO", "empregado": "EMPREGADO",
                  "apoio": "APOIO", "socio": "SOCIO", "prestador": "PRESTADOR"}


def pasta_do_colaborador(c: dict) -> str:
    """Nome da pasta em RH/: 'NOME COMPLETO - VINCULO' (POP-ADM-01)."""
    from .nomes import pasta_colaborador
    vinc = VINCULO_ROTULO.get((c.get("vinculo") or "").lower(), (c.get("vinculo") or "A DEFINIR"))
    return pasta_colaborador(c.get("nome") or c.get("id") or "SEM NOME", vinc)


def despesas() -> dict:
    return carregar_json("despesas_fixas")


def lista_despesas(ativas=True) -> list[dict]:
    return [d for d in despesas().get("despesas") or [] if (d.get("ativo") or not ativas)]
