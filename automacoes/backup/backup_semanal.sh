#!/usr/bin/env bash
# Backup semanal da VPS (cron: domingo 03:30). Log em /var/log/escritorio-backup.log
#   30 3 * * 0  /opt/escritorio/automacoes/backup/backup_semanal.sh >> /var/log/escritorio-backup.log 2>&1
set -euo pipefail

BASE="${ESCRITORIO_BASE:-/opt/escritorio}"
PY="${ESCRITORIO_PY:-$BASE/venv/bin/python}"

cd "$BASE"
echo "=== $(date '+%Y-%m-%d %H:%M:%S') backup semanal ==="
"$PY" automacoes/backup/backup_semanal.py --go --infinitum --drive
echo "=== $(date '+%Y-%m-%d %H:%M:%S') fim ==="
