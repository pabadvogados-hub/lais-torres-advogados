# POP-TRIB-02 — Tributário: procuração e levantamento do passivo

Versão 1 — 16/11/2026

| | |
|---|---|
| **Dono do POP** | Dr. Alex |
| **Quem executa** | Estagiário(a) do tributário `[A CONFIRMAR quem]` |
| **Gatilho** | Procuração no e-CAC concedida (POP-TRIB-01) ou contrato tributário assinado (POP-ATD-03) |
| **Termina quando** | Todos os extratos salvos no Drive e relatório do agente de passivo fiscal pronto |
| **Prazo** | Até 1 dia útil após a procuração (o trabalho em si leva cerca de 1h20) |

## Objetivo

Levantar **todo** o passivo federal da empresa, no e-CAC (Receita) e no Regularize (PGFN), em PDFs
padronizados, para o agente de passivo fiscal calcular a CAPAG e os cenários. Antes, isso levava
horas; com o extrato na mão, a IA faz a análise de vários clientes de uma vez.

## Automação x pessoa

| A automação faz | A pessoa faz |
|---|---|
| Cria a pasta do cliente no Drive com as subpastas | Confere a pasta |
| Lê os PDFs e monta o relatório de passivo e CAPAG | Baixa os PDFs no e-CAC e no Regularize (exigem login com certificado ou gov.br) |
| Cria a tarefa de análise para o Dr. Alex | Confere se nenhum relatório ficou faltando |

## Passo a passo

1. **Criar a pasta** `04 CLIENTES/{{cliente}}/05 TRIBUTÁRIO/` com `01 DOCUMENTOS FISCAIS`, `02 RELATÓRIOS` e `03 PETIÇÕES`. — *D0*
2. **Conferir a procuração eletrônica no e-CAC**: outorgante (CNPJ do cliente), outorgado
   (CPF do Dr. Alex ou CNPJ do escritório `[A CONFIRMAR]`), serviços liberados e validade
   `[A CONFIRMAR prazo padrão]`. Se faltar serviço, pedir nova procuração ao cliente. — *D0*
3. **Coletar no e-CAC** (cerca de 30 minutos), depois de "Alterar perfil de acesso" para o CNPJ do cliente:
   - Relatório de Situação Fiscal → `AAAA-MM-DD_{{CLIENTE}}_eCAC-SituacaoFiscal.pdf`
   - Caixa Postal: procurar intimações e termos de exclusão do Simples Nacional (há prazo para
     impugnar **(conferir o prazo indicado no próprio termo)**). Achou algo com prazo: avisar o Dr. Alex no mesmo dia.
   - Parcelamentos ativos e parcelas em atraso.
   - Débitos vencidos ainda não inscritos em dívida ativa.
   - Processos administrativos e certidão.
4. **Coletar no Regularize** (cerca de 40 minutos):
   - Notificações.
   - Relatório consolidado da dívida ativa.
   - Negociações e parcelamentos (SISPAR).
   - Simulação de adesão às modalidades disponíveis, salva em PDF com data e hora.
   - CAPAG: faixa e informações apresentadas.
5. **Levantar também** (quando houver): dívida ativa estadual (Sefaz do estado) e municipal, e
   execuções fiscais (consulta pública dos tribunais). A transação da PGFN cobre só dívida federal;
   estadual e municipal seguem regras próprias **(conferir com o Dr. Alex)**. — *se houver*
6. **Rodar o agente de passivo fiscal** com todos os PDFs. O relatório vai para `02 RELATÓRIOS`. — *D1*
7. **Criar a tarefa** de análise para o Dr. Alex (POP-TRIB-03). — *D1*

## O que vira tarefa no ADVBOX

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[TRIB] Levantamento do passivo - {{cliente}}` | Estagiário(a) do tributário | 1 dia útil após a procuração |
| `[TRIB] Análise e parecer - {{cliente}}` | Dr. Alex | 2 dias úteis após o levantamento |

## Onde salva no Drive

`04 CLIENTES/{{cliente}}/05 TRIBUTÁRIO/01 DOCUMENTOS FISCAIS/` (extratos) e `02 RELATÓRIOS/` (relatório do agente).

## Pendências `[A CONFIRMAR]`
- Outorgado da procuração (CPF do Dr. Alex ou CNPJ do escritório) e validade padrão.
- Quem executa o levantamento.
