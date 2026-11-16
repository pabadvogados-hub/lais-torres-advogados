# -*- coding: utf-8 -*-
"""Tira do ADVBOX os documentos que hoje so existem la e guarda no Drive (erro apontado no kickoff:
"se perdermos o ADVBOX, perdemos tudo").

So LE do ADVBOX (GET /documents e GET /documents/{id}/download, cuja temporary_url vale 5 minutos)
e grava no Drive em CLIENTES/<CLIENTE>/99_A_CLASSIFICAR/MIGRADO_ADVBOX/ com o nome
"AAAA-MM-DD_<nome original>" (data do upload no ADVBOX). Nada e apagado do ADVBOX.
A equipe depois move cada arquivo para a pasta do processo/demanda.

Clientes: os de config/clientes.json com advbox.customer_id, ou --todos (todos do ADVBOX).
Ritmo: 30 GET/min (limite da API) — um acervo de 600 arquivos leva ~20 minutos.
Idempotente: cada documento do ADVBOX e copiado uma vez (documentos_recebidos, hash "advbox:<id>").

Uso:
    python automacoes/drive/migrar_docs_advbox.py                 # dry-run: lista o que seria copiado
    python automacoes/drive/migrar_docs_advbox.py --todos --go
"""
from __future__ import annotations

import argparse
import mimetypes
import sys
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from comum import advbox, db, drive  # noqa: E402
from comum.cadastros import lista_clientes  # noqa: E402
from comum.config import add_modo, banner, bloquear_exemplo, escritorio, utf8_stdout  # noqa: E402
from comum.nomes import limpar, pasta_cliente  # noqa: E402


def main():
    utf8_stdout()
    ap = add_modo(argparse.ArgumentParser(description="Copia o acervo do ADVBOX para o Drive"))
    ap.add_argument("--todos", action="store_true", help="todos os clientes do ADVBOX (nao so os do cadastro)")
    ap.add_argument("--limite", type=int, default=0, help="maximo de arquivos nesta rodada (0 = sem limite)")
    a = ap.parse_args()
    banner(a.go, "Migracao de documentos ADVBOX -> Drive")
    cfg = escritorio()
    bloquear_exemplo(cfg, "escritorio", a.go)
    raiz = (cfg.get("drive") or {}).get("raiz_id")
    svc = drive.servico() if (raiz and drive.credenciais_disponiveis()) else None
    if a.go and not svc:
        raise SystemExit("ERRO: --go precisa de drive.raiz_id e credencial do Google")
    if a.todos:
        alvos = [(c.get("id"), c.get("name")) for c in advbox.listar_clientes()]
    else:
        alvos = [((c.get("advbox") or {}).get("customer_id"), c.get("nome")) for c in lista_clientes()
                 if (c.get("advbox") or {}).get("customer_id")]
    con = db.conectar()
    feitos = 0
    for cid, nome in alvos:
        docs = advbox.listar_documentos(customer_id=cid)
        if not docs:
            continue
        caminho = ["CLIENTES", pasta_cliente(nome), "99_A_CLASSIFICAR", "MIGRADO_ADVBOX"]
        print(f"\n{nome} ({cid}): {len(docs)} documento(s) -> {'/'.join(caminho)}")
        pid = drive.garantir_caminho(svc, raiz, caminho, executar=a.go, log=None) if svc else None
        for d in docs:
            chave = f"advbox:{d.get('id')}"
            if db.ja_existe(con, "documentos_recebidos", hash=chave):
                continue
            data = (d.get("uploaded_at") or "")[:10]
            destino = limpar(f"{data}_{d.get('name') or d.get('id')}", 150)
            anexo = d.get("attached_to") or {}
            print(f"   - {destino}  [{anexo.get('type', '')}: {anexo.get('label', '')}]")
            if not a.go:
                continue
            url = advbox.url_temporaria_documento(d)
            r = requests.get(url, timeout=180)
            r.raise_for_status()
            mime = mimetypes.guess_type(destino)[0] or "application/octet-stream"
            f = drive.enviar_bytes(svc, r.content, destino, pid, mime, executar=True)
            db.gravar(con, "documentos_recebidos", hash=chave, cliente=nome, destino="/".join(caminho),
                      drive_id=f.get("id", ""), tarefa="")
            feitos += 1
            if a.limite and feitos >= a.limite:
                print(f"\nLimite de {a.limite} atingido. Rode de novo para continuar.")
                return
    print(f"\nCopiados nesta rodada: {feitos}")


if __name__ == "__main__":
    main()
