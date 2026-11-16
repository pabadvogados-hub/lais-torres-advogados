# -*- coding: utf-8 -*-
"""Cliente da API Asaas v3 da conta do escritorio.

Adaptado de _BASE_SISTEMA_VIRGEM/INTEGRACOES/asaas_cobranca.py e asaas_integration.py
(o _req que nunca levanta excecao, a trava de idempotencia por externalReference e o
telefone no formato do Asaas). Acrescentado: notificacoes, nota fiscal, transferencias
(Pix agendado), pagamento de boleto, saldo e extrato.

Auth: header `access_token` com a chave da conta (env ASAAS_API_KEY).
Ambiente: ASAAS_BASE_URL (producao https://api.asaas.com/v3; sandbox
https://api-sandbox.asaas.com/v3 — homologar la antes).

ESCRITA: toda funcao que cria/altera recebe `executar`. Sem `executar=True` ela devolve
{"_dry_run": True, "_payload": ...} e nao chama a API.

MODO OFFLINE: AsaasCliente(fixture="arquivo.json") responde os GET a partir de um JSON
{"/payments": [...], "/financialTransactions": [...], "/finance/balance": {...}, ...}.
Serve para testar regua, relatorio e NF sem credencial.
"""
from __future__ import annotations

import json
import os
import time
from pathlib import Path

import requests

from .config import so_digitos

BASE_PADRAO = "https://api.asaas.com/v3"
UA = "Escritorio-LaisTorres-Automacoes/1.0"


def telefone_asaas(telefone) -> str:
    """Celular no formato do Asaas: DDD + 9 digitos, sem o 55. (copiado da base virgem)"""
    tel = so_digitos(telefone)
    if tel.startswith("55") and len(tel) in (12, 13):
        tel = tel[2:]
    if len(tel) == 10 and tel[2] in "6789":
        tel = tel[:2] + "9" + tel[2:]
    if len(tel) not in (10, 11) or set(tel) == {"0"}:
        return ""
    return tel


def erros_legiveis(corpo) -> list[str]:
    if not isinstance(corpo, dict):
        return [str(corpo)[:200]]
    saida = []
    for e in corpo.get("errors") or []:
        saida.append(f"{e.get('description') or ''} ({e.get('code') or ''})".strip())
    if not saida and corpo.get("erro_conexao"):
        saida.append(corpo["erro_conexao"])
    return saida


def _dry(payload, endpoint):
    return {"_dry_run": True, "_endpoint": endpoint, "_payload": payload}


class AsaasCliente:
    def __init__(self, fixture: str | None = None):
        self.base = (os.getenv("ASAAS_BASE_URL") or BASE_PADRAO).rstrip("/")
        self.fixture = None
        if fixture:
            self.fixture = json.loads(Path(fixture).read_text("utf-8"))

    # ------------------------------------------------------------------ baixo nivel
    def _headers(self):
        token = os.getenv("ASAAS_API_KEY")
        if not token:
            raise RuntimeError("ASAAS_API_KEY ausente em config/.env")
        return {"access_token": token.strip(), "User-Agent": UA, "Content-Type": "application/json"}

    def req(self, method, endpoint, params=None, json_data=None, retries=2):
        """Devolve (status, corpo). Nunca levanta: o 400 do Asaas traz o motivo e ele
        precisa chegar legivel na pendencia humana."""
        if self.fixture is not None:
            if method != "GET":
                return 0, {"erro_conexao": "modo offline (fixture): escrita bloqueada"}
            dado = self.fixture.get(endpoint)
            if dado is None:
                return 404, {}
            if isinstance(dado, list):
                return 200, {"data": dado, "hasMore": False, "totalCount": len(dado)}
            return 200, dado
        url = self.base + endpoint
        for tentativa in range(retries + 1):
            try:
                r = requests.request(method, url, headers=self._headers(), params=params,
                                     json=json_data, timeout=40)
                if r.status_code == 429:
                    time.sleep(int(r.headers.get("Retry-After", 10)))
                    continue
                try:
                    corpo = r.json() if r.text else {}
                except ValueError:
                    corpo = {"raw": r.text[:400]}
                if r.status_code >= 500 and tentativa < retries:
                    time.sleep(3)
                    continue
                return r.status_code, corpo
            except requests.exceptions.RequestException as e:
                if tentativa < retries:
                    time.sleep(3)
                    continue
                return 0, {"erro_conexao": f"{type(e).__name__}: {e}"}
        return 0, {}

    def listar(self, endpoint, params=None, limite_total=5000) -> list[dict]:
        """Pagina com limit/offset ate hasMore=False."""
        params = dict(params or {})
        params.setdefault("limit", 100)
        params["offset"] = 0
        saida: list[dict] = []
        while True:
            st, corpo = self.req("GET", endpoint, params=params)
            if st != 200:
                raise RuntimeError(f"GET {endpoint} -> HTTP {st}: {'; '.join(erros_legiveis(corpo))}")
            lote = corpo.get("data") or []
            saida.extend(lote)
            if not corpo.get("hasMore") or not lote or len(saida) >= limite_total:
                break
            params["offset"] += params["limit"]
        return saida

    # ------------------------------------------------------------------ clientes
    def buscar_cliente(self, cpf_cnpj) -> dict | None:
        doc = so_digitos(cpf_cnpj)
        if not doc:
            return None
        st, corpo = self.req("GET", "/customers", params={"cpfCnpj": doc})
        if st != 200:
            return None
        if self.fixture is not None:  # o fixture nao filtra
            dados = [c for c in corpo.get("data") or [] if so_digitos(c.get("cpfCnpj")) == doc]
        else:
            dados = corpo.get("data") or []
        return dados[0] if dados else None

    def obter_cliente(self, customer_id) -> dict:
        if self.fixture is not None:
            for c in self.fixture.get("/customers") or []:
                if c.get("id") == customer_id:
                    return c
            return {}
        st, corpo = self.req("GET", f"/customers/{customer_id}")
        return corpo if st == 200 else {}

    def criar_cliente(self, nome, cpf_cnpj, email=None, telefone=None, endereco=None,
                      executar=False) -> tuple[dict | None, list[str]]:
        """Cria o cliente com `notificationDisabled: true` — e isso que impede o Asaas de
        disparar (e cobrar) os avisos dele. A regua propria (regua_cobranca.py) assume o papel."""
        payload = {"name": nome, "cpfCnpj": so_digitos(cpf_cnpj), "notificationDisabled": True}
        if email:
            payload["email"] = email
        tel = telefone_asaas(telefone)
        if tel:
            payload["mobilePhone"] = tel
        for k, v in (endereco or {}).items():   # address, addressNumber, province, postalCode
            if v:
                payload[k] = v
        if not executar:
            return _dry(payload, "POST /customers"), []
        st, corpo = self.req("POST", "/customers", json_data=payload)
        if st in (200, 201):
            return corpo, []
        return None, erros_legiveis(corpo) or [f"falha ao criar cliente (HTTP {st})"]

    # ------------------------------------------------------------------ notificacoes
    def notificacoes_do_cliente(self, customer_id) -> list[dict]:
        st, corpo = self.req("GET", f"/customers/{customer_id}/notifications")
        if st != 200:
            return []
        return corpo.get("data") or []

    def desligar_notificacoes(self, customer_id, executar=False) -> dict:
        """Desliga TODAS as notificacoes do Asaas para um cliente que ja existia (criado antes,
        com os avisos ligados). Doc: 'Alterando notificacoes de um cliente' —
        GET /customers/{id}/notifications + PUT /notifications/batch com enabled=false."""
        notifs = self.notificacoes_do_cliente(customer_id)
        ligadas = [n for n in notifs if n.get("enabled")]
        payload = {"customer": customer_id,
                   "notifications": [{"id": n["id"], "enabled": False} for n in ligadas]}
        if not ligadas:
            return {"ok": True, "alteradas": 0, "total": len(notifs)}
        if not executar:
            return _dry(payload, "PUT /notifications/batch")
        st, corpo = self.req("PUT", "/notifications/batch", json_data=payload)
        return {"ok": st == 200, "alteradas": len(ligadas), "status": st,
                "erros": erros_legiveis(corpo) if st != 200 else []}

    # ------------------------------------------------------------------ cobrancas
    def cobranca_por_referencia(self, external_reference) -> dict | None:
        """Trava de idempotencia (base virgem): cobranca excluida volta PENDING com deleted=true."""
        if not external_reference:
            return None
        st, corpo = self.req("GET", "/payments", params={"externalReference": external_reference, "limit": 10})
        if st != 200:
            return None
        for p in corpo.get("data") or []:
            if self.fixture is not None and p.get("externalReference") != external_reference:
                continue
            if p.get("deleted"):
                continue
            if (p.get("status") or "").upper() not in ("REFUNDED", "DELETED"):
                return p
        return None

    def criar_cobranca(self, customer_id, valor, vencimento, descricao, external_reference,
                       tipo="BOLETO", multa_percent=None, juros_mes=None, desconto=None,
                       executar=False) -> tuple[dict | None, bool, list[str]]:
        """Devolve (cobranca, ja_existia, erros). Uma cobranca = um boleto registrado (entra no DDA)."""
        ja = self.cobranca_por_referencia(external_reference)
        if ja:
            return ja, True, []
        payload = {
            "customer": customer_id,
            "billingType": tipo,
            "value": round(float(valor), 2),
            "dueDate": str(vencimento)[:10],
            "description": (descricao or "")[:500],
            "externalReference": external_reference,
        }
        if multa_percent:
            payload["fine"] = {"value": float(multa_percent)}
        if juros_mes:
            payload["interest"] = {"value": float(juros_mes)}
        if desconto:
            payload["discount"] = desconto
        if not executar:
            return _dry(payload, "POST /payments"), False, []
        st, corpo = self.req("POST", "/payments", json_data=payload)
        if st in (200, 201):
            return corpo, False, []
        return None, False, erros_legiveis(corpo) or [f"falha ao emitir cobranca (HTTP {st})"]

    def listar_cobrancas(self, status=None, venc_de=None, venc_ate=None,
                         pago_de=None, pago_ate=None, customer=None) -> list[dict]:
        params = {}
        if status:
            params["status"] = status
        if venc_de:
            params["dueDate[ge]"] = venc_de
        if venc_ate:
            params["dueDate[le]"] = venc_ate
        if pago_de:
            params["paymentDate[ge]"] = pago_de
        if pago_ate:
            params["paymentDate[le]"] = pago_ate
        if customer:
            params["customer"] = customer
        itens = self.listar("/payments", params)
        # filtro local: no modo offline o fixture nao filtra; online e redundante e inofensivo
        out = []
        for p in itens:
            if p.get("deleted"):
                continue
            if status and (p.get("status") or "") != status:
                continue
            d = (p.get("dueDate") or "")[:10]
            if venc_de and d < venc_de or venc_ate and d > venc_ate:
                continue
            pg = (p.get("paymentDate") or p.get("clientPaymentDate") or "")[:10]
            if (pago_de or pago_ate) and not pg:
                continue
            if pago_de and pg < pago_de or pago_ate and pg > pago_ate:
                continue
            if customer and p.get("customer") != customer:
                continue
            out.append(p)
        return out

    # ------------------------------------------------------------------ nota fiscal
    def nota_por_referencia(self, external_reference) -> dict | None:
        st, corpo = self.req("GET", "/invoices", params={"externalReference": external_reference, "limit": 10})
        if st != 200:
            return None
        for n in corpo.get("data") or []:
            if n.get("externalReference") == external_reference and n.get("status") not in ("CANCELED",):
                return n
        return None

    def agendar_nota(self, payload, executar=False) -> tuple[dict | None, list[str]]:
        """POST /invoices (agendar nota fiscal). Campos obrigatorios pela referencia da API:
        serviceDescription, observations, value, deductions, effectiveDate,
        municipalServiceName, taxes{retainIss, iss, pis, cofins, csll, inss, ir}."""
        if not executar:
            return _dry(payload, "POST /invoices"), []
        st, corpo = self.req("POST", "/invoices", json_data=payload)
        if st in (200, 201):
            return corpo, []
        return None, erros_legiveis(corpo) or [f"falha ao agendar nota (HTTP {st})"]

    def autorizar_nota(self, invoice_id, executar=False):
        """POST /invoices/{id}/authorize — antecipa a emissao de uma nota agendada."""
        if not executar:
            return _dry({}, f"POST /invoices/{invoice_id}/authorize")
        st, corpo = self.req("POST", f"/invoices/{invoice_id}/authorize")
        return corpo if st in (200, 201) else {"erro": erros_legiveis(corpo), "status": st}

    def obter_nota(self, invoice_id) -> dict:
        st, corpo = self.req("GET", f"/invoices/{invoice_id}")
        return corpo if st == 200 else {}

    # ------------------------------------------------------------------ transferencias
    def criar_pix(self, valor, chave, tipo_chave, descricao, data_agendada=None,
                  external_reference=None, executar=False) -> tuple[dict | None, list[str]]:
        """POST /transfers para chave Pix. `scheduleDate` (AAAA-MM-DD) agenda.
        Se a conta tiver a validacao de eventos criticos por token ligada, a transferencia
        nasce com authorized=false e so sai depois que a Dra. Lais aprovar no app/painel."""
        payload = {
            "value": round(float(valor), 2),
            "operationType": "PIX",
            "pixAddressKey": chave if tipo_chave in ("EMAIL", "EVP") else so_digitos(chave),
            "pixAddressKeyType": tipo_chave,
            "description": (descricao or "")[:140],
        }
        if data_agendada:
            payload["scheduleDate"] = str(data_agendada)[:10]
        if external_reference:
            payload["externalReference"] = external_reference
        if not executar:
            return _dry(payload, "POST /transfers"), []
        st, corpo = self.req("POST", "/transfers", json_data=payload)
        if st in (200, 201):
            return corpo, []
        return None, erros_legiveis(corpo) or [f"falha ao criar transferencia (HTTP {st})"]

    def obter_transferencia(self, transfer_id) -> dict:
        st, corpo = self.req("GET", f"/transfers/{transfer_id}")
        return corpo if st == 200 else {}

    def listar_transferencias(self, de=None, ate=None) -> list[dict]:
        params = {}
        if de:
            params["dateCreated[ge]"] = de
        if ate:
            params["dateCreated[le]"] = ate
        return self.listar("/transfers", params)

    def pagar_boleto(self, linha_digitavel, data_agendada=None, descricao="", vencimento=None,
                     valor=None, executar=False):
        """POST /bill — pagamento de conta (boleto de despesa fixa) pela conta Asaas."""
        payload = {"identificationField": so_digitos(linha_digitavel), "description": descricao}
        if data_agendada:
            payload["scheduleDate"] = str(data_agendada)[:10]
        if vencimento:
            payload["dueDate"] = str(vencimento)[:10]
        if valor:
            payload["value"] = round(float(valor), 2)
        if not executar:
            return _dry(payload, "POST /bill"), []
        st, corpo = self.req("POST", "/bill", json_data=payload)
        if st in (200, 201):
            return corpo, []
        return None, erros_legiveis(corpo) or [f"falha ao agendar boleto (HTTP {st})"]

    # ------------------------------------------------------------------ saldo e extrato
    def saldo(self) -> float | None:
        st, corpo = self.req("GET", "/finance/balance")
        if st != 200:
            return None
        return float(corpo.get("balance") or 0)

    def extrato(self, inicio, fim) -> list[dict]:
        """GET /financialTransactions — movimentacao da conta (entradas, saidas, taxas)."""
        itens = self.listar("/financialTransactions", {"startDate": inicio, "finishDate": fim})
        return [t for t in itens if inicio <= (t.get("date") or "")[:10] <= fim]

    # ------------------------------------------------------------------ envio
    def link_da_cobranca(self, payment) -> str:
        return (payment or {}).get("invoiceUrl") or ""
