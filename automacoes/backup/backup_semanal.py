# -*- coding: utf-8 -*-
"""Backup semanal da VPS: banco + conversas + relatorios + cadastros, cifrado, com rotacao.

O QUE ENTRA
  - dados/escritorio.db           copia consistente pela API de backup do SQLite (seguro com os
                                  scripts rodando — mesma tecnica do backup_db.sh da base virgem)
  - dados/conversas/              eventos de webhook do Infinitum (inclui mensagens, se o Infinitum
                                  mandar) e exportacoes de conversa colocadas ali (ver README)
  - dados/infinitum/              exportacao do que a API publica do Infinitum expoe (--infinitum)
  - dados/fila_mensagens.jsonl, dados/saida/   mensagens enviadas e relatorios
  - config/*.json                 cadastros (clientes, colaboradores, despesas, escritorio)
  NAO entram: config/.env e tokens (credencial nao vai para backup; se perder, gera-se outra).

CIFRA: openssl AES-256-CBC com PBKDF2, senha lida de BACKUP_SENHA_ARQUIVO (arquivo com a senha,
permissao 600, guardado TAMBEM fora da VPS — sem ela o backup nao abre). Sem senha, o backup
fica so local; para subir ao Drive a cifra e obrigatoria (ha CPF e chave Pix nos cadastros).
Restaurar: openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 -in X.tar.gz.enc -out X.tar.gz -pass file:<senha>

ROTACAO: guarda as ultimas BACKUP_MANTER (padrao 8 = ~2 meses) em BACKUP_DIR.

Uso:
    python automacoes/backup/backup_semanal.py                       # dry-run: mostra o que entraria
    python automacoes/backup/backup_semanal.py --go --infinitum --drive
Cron (VPS): domingo 03:30 -> automacoes/backup/backup_semanal.sh
"""
from __future__ import annotations

import argparse
import os
import shutil
import sqlite3
import subprocess
import sys
import tarfile
import tempfile
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from comum.config import CONFIG_DIR, DADOS_DIR, RAIZ, add_modo, banner, escritorio, garantir_dir, utf8_stdout  # noqa: E402

BACKUP_DIR = Path(os.getenv("BACKUP_DIR") or (RAIZ / "backups"))
MANTER = int(os.getenv("BACKUP_MANTER") or 8)


def _tamanho(p: Path) -> int:
    if p.is_file():
        return p.stat().st_size
    return sum(f.stat().st_size for f in p.rglob("*") if f.is_file()) if p.exists() else 0


def itens() -> list[tuple[Path, str]]:
    lista = [(DADOS_DIR / "escritorio.db", "dados/escritorio.db"),
             (DADOS_DIR / "conversas", "dados/conversas"),
             (DADOS_DIR / "infinitum", "dados/infinitum"),
             (DADOS_DIR / "fila_mensagens.jsonl", "dados/fila_mensagens.jsonl"),
             (DADOS_DIR / "lancamentos_manuais.csv", "dados/lancamentos_manuais.csv"),
             (DADOS_DIR / "saida", "dados/saida")]
    lista += [(p, f"config/{p.name}") for p in sorted(CONFIG_DIR.glob("*.json"))
              if not p.name.startswith(("token", "oauth")) and not p.name.endswith(".example.json")]
    return [(p, n) for p, n in lista if p.exists()]


def copia_sqlite(origem: Path, destino: Path):
    s = sqlite3.connect(str(origem))
    d = sqlite3.connect(str(destino))
    with d:
        s.backup(d)
    d.close()
    s.close()


def cifrar(arquivo: Path) -> Path:
    senha = os.getenv("BACKUP_SENHA_ARQUIVO")
    if not senha or not Path(senha).exists():
        raise RuntimeError("BACKUP_SENHA_ARQUIVO nao configurado")
    if not shutil.which("openssl"):
        raise RuntimeError("openssl nao encontrado (instale: apt install openssl)")
    saida = arquivo.with_name(arquivo.name + ".enc")
    subprocess.run(["openssl", "enc", "-aes-256-cbc", "-salt", "-pbkdf2", "-iter", "200000",
                    "-in", str(arquivo), "-out", str(saida), "-pass", f"file:{senha}"], check=True)
    arquivo.unlink()
    return saida


def rotacionar():
    arqs = sorted(BACKUP_DIR.glob("backup_escritorio_*.tar.gz*"))
    for velho in arqs[:-MANTER] if len(arqs) > MANTER else []:
        velho.unlink()
        print(f"  removido (rotacao): {velho.name}")


def main():
    utf8_stdout()
    ap = add_modo(argparse.ArgumentParser(description="Backup semanal (banco + conversas + cadastros)"))
    ap.add_argument("--infinitum", action="store_true", help="exporta antes o que a API do Infinitum expoe")
    ap.add_argument("--drive", action="store_true", help="sobe o arquivo cifrado para 00_ESCRITORIO/BACKUPS")
    a = ap.parse_args()
    banner(a.go, "Backup semanal")
    if a.infinitum:
        import exportar_infinitum
        exportar_infinitum.exportar(executar=a.go)
    lista = itens()
    total = 0
    for p, nome in lista:
        t = _tamanho(p)
        total += t
        print(f"  + {nome:40} {t / 1024:10.1f} KB")
    print(f"  Total bruto: {total / 1024 / 1024:.2f} MB -> {BACKUP_DIR}")
    if not a.go:
        return
    garantir_dir(BACKUP_DIR)
    carimbo = datetime.now().strftime("%Y%m%d_%H%M%S")
    arq = BACKUP_DIR / f"backup_escritorio_{carimbo}.tar.gz"
    with tempfile.TemporaryDirectory() as tmp:
        with tarfile.open(arq, "w:gz") as tar:
            for p, nome in lista:
                if p.suffix == ".db":
                    copia = Path(tmp) / p.name
                    copia_sqlite(p, copia)
                    tar.add(copia, arcname=nome)
                else:
                    tar.add(p, arcname=nome)
    try:
        arq = cifrar(arq)
        print(f"  Cifrado: {arq}")
    except RuntimeError as e:
        print(f"  AVISO: backup NAO cifrado ({e}).")
        if a.drive:
            raise SystemExit("Nao subo backup sem cifra para o Drive (dados pessoais). Configure BACKUP_SENHA_ARQUIVO.")
    print(f"  Backup: {arq} ({arq.stat().st_size / 1024 / 1024:.2f} MB)")
    rotacionar()
    if a.drive:
        from comum import drive
        raiz = (escritorio().get("drive") or {}).get("raiz_id")
        if not raiz or not drive.credenciais_disponiveis():
            raise SystemExit("Drive indisponivel (raiz_id/credencial)")
        svc = drive.servico()
        pid = drive.garantir_caminho(svc, raiz, ["00_ESCRITORIO", "BACKUPS"], executar=True)
        print("  Drive:", drive.enviar_arquivo(svc, arq, pid, executar=True))


if __name__ == "__main__":
    main()
