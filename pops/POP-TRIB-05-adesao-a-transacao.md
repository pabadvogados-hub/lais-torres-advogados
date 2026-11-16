# POP-TRIB-05 — Tributário: medidas preparatórias e adesão à transação

Versão 1 — 16/11/2026

| | |
|---|---|
| **Dono do POP** | Dr. Alex |
| **Quem executa** | Dr. Alex; estagiário(a) do tributário prepara documentos e acompanha |
| **Gatilho** | Contrato tributário assinado (POP-TRIB-04) |
| **Termina quando** | Adesão feita, recibo no Drive, 1ª parcela paga e no controle mensal (POP-TRIB-06), êxito calculado e avisado ao financeiro |
| **Prazo** | Conforme o cronograma do parecer; adesão no dia em que a simulação for aprovada pelo cliente |

## Objetivo

Executar a estratégia do parecer. Às vezes é preciso **preparar** antes de aderir (levar débitos da
Receita para a PGFN, rever a CAPAG); depois, aderir no edital certo, sem perder a 1ª parcela.

## Passo A — Remessa de débitos da Receita para a PGFN (quando o parecer indicar)

1. Emitir o Relatório de Situação Fiscal **no dia do protocolo**.
2. Separar os débitos declarados, vencidos há mais de 90 dias, não pagos, não inscritos, sem
   parcelamento e sem suspensão. Anotar o que ficou de fora e por quê.
3. Preencher o formulário de pedido de inscrição em dívida ativa da Receita (o agente `peca-tributaria`
   monta a minuta; tese T01 do banco) e endereçar à unidade
   com jurisdição sobre o contribuinte **(conferir o formulário e o serviço vigentes no e-CAC)**.
4. Conferir que os totais do relatório, da tabela e do formulário batem.
5. Protocolar no e-CAC (Processos Digitais) e juntar os documentos **no mesmo dia** (não deixar rascunho).
6. Acompanhar: tarefa em 3 dias úteis, depois semanal. A Administração tem 30 dias para decidir
   (Lei 9.784/1999, art. 49). Negado ou sem resposta no prazo: o Dr. Alex avalia mandado de segurança.

## Passo B — Revisão da CAPAG (quando o parecer indicar ganho de faixa)

1. **Escolher uma via, sem misturar**:
   - atacar um dado desatualizado na base da PGFN (faturamento, veículo, imóvel) — mais rápida;
   - demonstrar a CAPAG efetiva com demonstrações contábeis e laudo, com o contador do cliente — mais longa.
2. Rodar o agente `avaliador-capag` (veredito, travas, vetores e documentos do art. 30 que faltam). Só
   com veredito favorável, o agente `peca-tributaria` monta o pedido no timbrado, com os documentos.
3. Protocolar no Regularize (serviço de revisão de capacidade de pagamento) **(conferir o caminho no sistema)**.
4. Antecipar as exigências que costumam vir: fluxo de caixa, distribuição de lucros, mútuos, grupo econômico.
5. **Só protocolar com o ganho de faixa confirmado nos números e com aprovação do Dr. Alex.**
   Julgado o pedido, um novo só cabe com fato superveniente ou mudança substancial da CAPAG presumida
   (Portaria PGFN 6.757/2022, art. 34-B). Recurso da decisão: 10 dias, pelo Regularize (art. 34-A).

## Passo C — Adesão

1. **Conferir o edital no dia**: vigência, data de corte, débitos abrangidos, entrada, prazo e
   descontos, no Regularize.
2. **Simular por inscrição.** Se o sistema cobrar entrada maior por causa de parcelamento anterior,
   avaliar separar as inscrições antes de aderir **(conferir regra do edital)**.
3. **Obter o "de acordo" do cliente por escrito**: enviar a simulação com entrada, parcela e prazo, e
   guardar a resposta dele (WhatsApp ou e-mail) na pasta.
4. **Aderir** e salvar o recibo e o termo na pasta.
5. **Garantir a 1ª parcela**: emitir a guia, enviar ao cliente e confirmar o pagamento. **Atraso na
   1ª parcela pode cancelar a adesão** **(conferir no edital)**.
6. **Calcular o êxito** sobre o desconto efetivo obtido e avisar a Dra. Laís (financeiro) para lançar a cobrança.
7. Incluir a negociação no controle mensal (POP-TRIB-06).

## O que vira tarefa no ADVBOX

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[TRIB] Remessa à PGFN - acompanhar - {{cliente}}` | Estagiário(a) do tributário | 3 dias úteis, depois semanal |
| `[TRIB] Revisão da CAPAG - {{cliente}}` | Dr. Alex | Cronograma do parecer |
| `[TRIB] Adesão - {{cliente}}` | Dr. Alex | Dia da simulação aprovada |
| `[TRIB] Confirmar 1ª parcela - {{cliente}}` | Estagiário(a) do tributário | Vencimento da 1ª parcela |
| `[FINANCEIRO] Lançar êxito tributário - {{cliente}}` | Dra. Laís | 2 dias úteis após a adesão |

## Onde salva no Drive

`CLIENTES/{{cliente}}/05_TRIBUTARIO/03_PETICOES/` (pedidos e protocolos) e `01_DOCUMENTOS_FISCAIS/` (simulação, recibo, termo de adesão, guias e comprovantes).

## Pendências `[A CONFIRMAR]`
- Itens marcados **(conferir)**: sempre pela norma, pelo sistema e pelo edital vigentes na data.
- Regra de cobrança do êxito (momento e forma).
