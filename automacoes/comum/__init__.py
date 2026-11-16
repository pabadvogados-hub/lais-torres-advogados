# -*- coding: utf-8 -*-
"""Camada comum das automacoes do escritorio Lais Torres & Alex Brunno.

config      -> .env, JSONs de config/, pastas de dados, --dry-run/--go
db          -> SQLite local (estado: o que ja foi enviado, emitido, agendado)
asaas       -> API Asaas v3 (cobranca, notificacoes, NF, transferencias, extrato)
advbox      -> API ADVBOX (processos, clientes, tarefas, documentos)
infinitum   -> API publica do Infinitum (cards; envio por card + automacao)
mensageria  -> modelos {{chave}} e fila/envio de mensagens
drive       -> Google Drive (pastas idempotentes, upload, docx->pdf)
nomes       -> convencao de nomes de pasta e arquivo
"""
