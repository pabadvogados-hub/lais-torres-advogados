# -*- coding: utf-8 -*-
"""Camada de assinatura eletronica PLUGAVEL.

PENDENCIA: o escritorio NAO tem ferramenta de assinatura confirmada (kickoff/Projeto, "o que
precisamos de voces"). Por isso o provedor e escolhido em escritorio.json -> rh.assinatura.provedor:

  "manual"  (padrao, custo zero) -> gera o PDF e um roteiro de assinatura. Opcao gratuita sugerida:
            assinatura gov.br (assinador.iti.br — cada parte assina o PDF com a conta gov.br prata
            ou ouro; assinatura eletronica avancada, Lei 14.063/2020). A Dra. Lais marca como
            assinado com `colaborador.py marcar --item contrato` quando o PDF assinado voltar.
            [A CONFIRMAR com a Dra. Lais e com a instituicao de ensino se aceitam gov.br — algumas
            faculdades tem fluxo proprio para o termo de estagio.]
  "zapsign" -> API ZapSign (adaptado de _BASE_SISTEMA_VIRGEM/INTEGRACOES/zapsign_integration.py:
            POST /api/v1/docs/ com base64_pdf e signatarios; codigo pelo WhatsApp). Exige plano
            com API (custo mensal — confirmar antes) e env ZAPSIGN_API_TOKEN.

Para plugar outro (Clicksign, D4Sign, a integracao ZapSign/Gov.br que o Infinitum anunciou "em
breve"), basta criar uma classe com enviar() e status() e registrar em PROVEDORES.
"""
from __future__ import annotations

import base64
import os
from pathlib import Path

import requests

from comum.config import SAIDA_DIR, garantir_dir


class Manual:
    nome = "manual"

    def enviar(self, pdf: bytes, nome_doc: str, signatarios: list[dict], executar=False) -> dict:
        pasta = garantir_dir(SAIDA_DIR / "assinaturas")
        roteiro = pasta / f"{nome_doc} - ROTEIRO DE ASSINATURA.md"
        linhas = [f"# Assinatura de: {nome_doc}", "",
                  "1. Envie o PDF a cada parte, na ordem abaixo.",
                  "2. Cada parte assina em https://assinador.iti.br com a conta gov.br (prata ou ouro) e devolve o PDF.",
                  "3. O PDF com todas as assinaturas vai para a pasta 02_CONTRATO_E_ADITIVOS do colaborador.",
                  "4. Marque: python automacoes/rh/colaborador.py marcar --id <id> --item contrato --go", "",
                  "## Partes"]
        linhas += [f"- {s.get('nome')} ({s.get('papel', '')}) — {s.get('email') or ''} {s.get('telefone') or ''}"
                   for s in signatarios]
        if executar:
            roteiro.write_text("\n".join(linhas) + "\n", encoding="utf-8")
            if pdf:
                (pasta / f"{nome_doc}.pdf").write_bytes(pdf)
        return {"provedor": self.nome, "pendente_manual": True, "roteiro": str(roteiro)}

    def status(self, ref: str) -> dict:
        return {"provedor": self.nome, "assinado": None, "obs": "conferencia manual"}


class ZapSign:
    nome = "zapsign"
    BASE = "https://api.zapsign.com.br/api/v1"

    def _h(self):
        tok = os.getenv("ZAPSIGN_API_TOKEN")
        if not tok:
            raise RuntimeError("ZAPSIGN_API_TOKEN ausente em config/.env")
        return {"Authorization": f"Bearer {tok}", "Content-Type": "application/json"}

    def enviar(self, pdf: bytes, nome_doc: str, signatarios: list[dict], executar=False) -> dict:
        signers = []
        for s in signatarios:
            tel = "".join(c for c in str(s.get("telefone") or "") if c.isdigit())
            if tel.startswith("55") and len(tel) > 11:
                tel = tel[2:]
            signers.append({"name": s["nome"], "email": None if tel else s.get("email"),
                            "phone_country": "55", "phone_number": tel or None,
                            "auth_mode": "assinaturaTela-tokenWhatsapp" if tel else "assinaturaTela-tokenEmail",
                            "send_automatic_whatsapp": bool(tel), "send_automatic_email": not tel and bool(s.get("email"))})
        payload = {"name": nome_doc, "base64_pdf": base64.b64encode(pdf).decode() if pdf else "",
                   "signers": signers, "lang": "pt-br", "external_id": nome_doc[:60]}
        if not executar:
            return {"_dry_run": True, "provedor": self.nome, "signers": signers}
        r = requests.post(f"{self.BASE}/docs/", headers=self._h(), json=payload, timeout=60)
        r.raise_for_status()
        d = r.json()
        return {"provedor": self.nome, "ref": d.get("token"),
                "links": [{"nome": s.get("name"), "link": s.get("sign_url")} for s in d.get("signers") or []]}

    def status(self, ref: str) -> dict:
        r = requests.get(f"{self.BASE}/docs/{ref}/", headers=self._h(), timeout=30)
        r.raise_for_status()
        d = r.json()
        return {"provedor": self.nome, "assinado": d.get("status") == "signed", "pdf_assinado": d.get("signed_file")}


PROVEDORES = {"manual": Manual, "zapsign": ZapSign}


def provedor(nome: str | None):
    cls = PROVEDORES.get((nome or "manual").lower())
    if not cls:
        raise SystemExit(f"provedor de assinatura desconhecido: {nome} (opcoes: {', '.join(PROVEDORES)})")
    return cls()
