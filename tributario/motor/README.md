# Motor de prospecção tributária

Acha empresas com dívida na PGFN, dá uma nota de 0 a 100 e busca o contato pela BrasilAPI.
**Não manda mensagem e não mexe em CRM nenhum**: só gera a lista.

```
python tributario/motor/motor_autonomo.py               # rodada normal: 300 consultas
python tributario/motor/motor_autonomo.py --lote 500
python tributario/motor/motor_autonomo.py --reprocessar # refaz a soma do trimestre
```

## O que ele faz

1. Confere em dadosabertos.pgfn.gov.br se saiu trimestre novo e baixa (cerca de 1,5 GB, sem o FGTS).
   Desde o 3º trimestre de 2026, o arquivo "não previdenciário" se chama `Dados_abertos_Sistema_SIDA.zip`.
2. Lê os CSVs direto do zip e soma a dívida por CNPJ. Entra só pessoa jurídica devedora principal. Ficam de
   fora órgãos públicos, falidas, empresas em recuperação, sindicatos e condomínios.
3. Dá a nota:
   - dívida em cobrança e ainda não negociada: até 30
   - não ajuizada: até 25
   - inscrição recente: 15
   - faixa de R$ 100 mil a 1 milhão: 15
   - UF preferida (MA, PA, TO ou GO): 10
   - 3 ou mais inscrições: 5
4. Consulta um lote por dia na BrasilAPI e guarda o resultado em cache, com pausa de 0,9 s entre as consultas.
5. Grava `leads/leads_tributario.csv` só com empresas **ativas e com telefone**, em ordem de nota.

Os ajustes ficam em `CONFIG`, no topo do arquivo: `faixa_min`, `faixa_max`, `ufs` e `ufs_preferidas`.
O escritório favorece **MA, PA e TO** (a região de Imperatriz) e **GO** (campanhas com a identidade de
Goiânia). Para buscar só nesses estados, ponha a mesma lista em `ufs`.

## Rodar sozinho todo dia

Na VPS do escritório (Módulo 7), pelo cron, às 7h10:

```
10 7 * * * cd /opt/escritorio && python3 tributario/motor/motor_autonomo.py --lote 400
```

Num computador Windows:

```
schtasks /Create /TN "Motor Tributario" /TR "\"C:\caminho\python.exe\" \"C:\caminho\tributario\motor\motor_autonomo.py\" --lote 400" /SC DAILY /ST 07:10
```

As pastas `data/` (zips da PGFN) e `leads/` (lista e cache) ficam fora do git. A lista não vai para o
repositório: ela tem telefone e e-mail de empresas reais.
