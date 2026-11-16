# -*- coding: utf-8 -*-
"""Google Drive do escritorio (adaptado de _BASE_SISTEMA_VIRGEM/INTEGRACOES/google_integration.py:
autenticacao OAuth com token salvo e criacao de pasta IDEMPOTENTE — nunca duplica pasta).

Credenciais (caminhos em config/.env):
  GOOGLE_OAUTH_CREDENTIALS  -> JSON do "ID do cliente OAuth" (app de desktop) do Google Cloud
  GOOGLE_TOKEN_PATH         -> onde o token fica salvo depois do primeiro login
O primeiro login abre o navegador UMA vez (rodar na maquina do escritorio, logado na conta
Google Workspace do escritorio) e o token.json gerado e copiado para a VPS.

Escopo so 'drive' (licao da base: pedir escopo a mais derruba o refresh com invalid_scope).
Funciona em Drive compartilhado (supportsAllDrives).
"""
from __future__ import annotations

import io
import mimetypes
import os
from pathlib import Path

from .config import CONFIG_DIR, RAIZ

SCOPES = ["https://www.googleapis.com/auth/drive"]
MIME_PASTA = "application/vnd.google-apps.folder"
_KW = {"supportsAllDrives": True}
_KW_LIST = {"supportsAllDrives": True, "includeItemsFromAllDrives": True}


def _caminho(env: str, padrao: str) -> Path:
    p = Path(os.getenv(env) or (CONFIG_DIR / padrao))
    return p if p.is_absolute() else RAIZ / p


def credenciais_disponiveis() -> bool:
    return _caminho("GOOGLE_TOKEN_PATH", "token_google.json").exists() or \
        _caminho("GOOGLE_OAUTH_CREDENTIALS", "oauth_google.json").exists()


def servico():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build

    token_path = _caminho("GOOGLE_TOKEN_PATH", "token_google.json")
    cred_path = _caminho("GOOGLE_OAUTH_CREDENTIALS", "oauth_google.json")
    creds = None
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not cred_path.exists():
                raise RuntimeError("Sem credencial do Google: configure GOOGLE_OAUTH_CREDENTIALS em config/.env")
            from google_auth_oauthlib.flow import InstalledAppFlow
            flow = InstalledAppFlow.from_client_secrets_file(str(cred_path), SCOPES)
            creds = flow.run_local_server(port=0)
        token_path.write_text(creds.to_json(), encoding="utf-8")
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def _esc(nome: str) -> str:
    return nome.replace("\\", "\\\\").replace("'", "\\'")


def achar(svc, nome: str, pai_id: str, pasta: bool | None = None) -> list[dict]:
    q = f"'{pai_id}' in parents and trashed=false and name='{_esc(nome)}'"
    if pasta is True:
        q += f" and mimeType='{MIME_PASTA}'"
    elif pasta is False:
        q += f" and mimeType!='{MIME_PASTA}'"
    r = svc.files().list(q=q, fields="files(id,name,webViewLink,mimeType)", pageSize=50, **_KW_LIST).execute()
    return r.get("files", [])


def garantir_pasta(svc, nome: str, pai_id: str, executar=False) -> tuple[str, bool]:
    """Devolve (id, criada). Ja existe -> reusa (se houver duplicata, usa a primeira e avisa).
    Em dry-run, pasta inexistente volta como 'DRY:<nome>'."""
    if str(pai_id).startswith("DRY:"):
        return f"DRY:{nome}", True
    achadas = achar(svc, nome, pai_id, pasta=True)
    if len(achadas) > 1:
        print(f"    ATENCAO: {len(achadas)} pastas '{nome}' no mesmo lugar; uso a primeira. Limpar a mao.")
    if achadas:
        return achadas[0]["id"], False
    if not executar:
        return f"DRY:{nome}", True
    f = svc.files().create(body={"name": nome, "mimeType": MIME_PASTA, "parents": [pai_id]},
                           fields="id", **_KW).execute()
    return f["id"], True


def garantir_caminho(svc, raiz_id: str, partes: list[str], executar=False, log=print) -> str:
    atual = raiz_id
    caminho = []
    for p in partes:
        caminho.append(p)
        atual, criada = garantir_pasta(svc, p, atual, executar)
        if criada and log:
            log(f"    {'[DRY-RUN] criaria' if not executar else 'criada'}: {'/'.join(caminho)}")
    return atual


def enviar_arquivo(svc, local: str | Path, pasta_id: str, nome: str | None = None,
                   executar=False, converter_para_google=False) -> dict:
    """Sobe o arquivo; se ja existir um com o mesmo nome na pasta, NAO sobrescreve (devolve o existente)."""
    from googleapiclient.http import MediaFileUpload

    local = Path(local)
    nome = nome or local.name
    if str(pasta_id).startswith("DRY:"):
        return {"_dry_run": True, "nome": nome, "pasta": pasta_id}
    ja = achar(svc, nome, pasta_id, pasta=False)
    if ja:
        return {"id": ja[0]["id"], "webViewLink": ja[0].get("webViewLink"), "ja_existia": True}
    if not executar:
        return {"_dry_run": True, "nome": nome, "pasta": pasta_id}
    mime = mimetypes.guess_type(str(local))[0] or "application/octet-stream"
    body = {"name": nome, "parents": [pasta_id]}
    if converter_para_google:
        body["mimeType"] = "application/vnd.google-apps.document"
    media = MediaFileUpload(str(local), mimetype=mime, resumable=False)
    return svc.files().create(body=body, media_body=media, fields="id,webViewLink", **_KW).execute()


def enviar_bytes(svc, conteudo: bytes, nome: str, pasta_id: str, mime: str, executar=False) -> dict:
    from googleapiclient.http import MediaIoBaseUpload

    if str(pasta_id).startswith("DRY:") or not executar:
        return {"_dry_run": True, "nome": nome, "pasta": pasta_id}
    ja = achar(svc, nome, pasta_id, pasta=False)
    if ja:
        return {"id": ja[0]["id"], "webViewLink": ja[0].get("webViewLink"), "ja_existia": True}
    media = MediaIoBaseUpload(io.BytesIO(conteudo), mimetype=mime, resumable=False)
    return svc.files().create(body={"name": nome, "parents": [pasta_id]}, media_body=media,
                              fields="id,webViewLink", **_KW).execute()


def docx_para_pdf(svc, docx: str | Path, pasta_temp_id: str) -> bytes:
    """Converte .docx em PDF pelo proprio Drive (sobe como Google Doc, exporta PDF, apaga o
    intermediario). Mesmo caminho que funcionou no Casal da IA (sem Word nem LibreOffice)."""
    from googleapiclient.http import MediaFileUpload

    media = MediaFileUpload(str(docx), resumable=False,
                            mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    tmp = svc.files().create(body={"name": Path(docx).stem + " (conversao)", "parents": [pasta_temp_id],
                                   "mimeType": "application/vnd.google-apps.document"},
                             media_body=media, fields="id", **_KW).execute()
    try:
        return svc.files().export(fileId=tmp["id"], mimeType="application/pdf").execute()
    finally:
        svc.files().delete(fileId=tmp["id"], **_KW).execute()
