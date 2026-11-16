# POP-TRIB-03 — Tributário: análise jurídica, CAPAG e parecer

Versão 1 — 16/11/2026

| | |
|---|---|
| **Dono do POP** | Dr. Alex |
| **Quem executa** | IA (primeira versão do relatório e do parecer); Dr. Alex (análise e aprovação) |
| **Gatilho** | Levantamento do passivo concluído (POP-TRIB-02) |
| **Termina quando** | Parecer aprovado pelo Dr. Alex e reunião de proposta marcada (POP-TRIB-04) |
| **Prazo** | Até 2 dias úteis após o levantamento |

## Objetivo

Responder ao cliente, com números, três perguntas: **quanto ele deve de verdade, em que faixa de
CAPAG ele está e quanto pode economizar**. O parecer é a base da proposta.

## Normas de referência (conferir a versão vigente a cada caso)

- Lei 13.988/2020 (transação tributária) e Portaria PGFN nº 6.757/2022 (regulamenta a transação na PGFN).
- **Edital vigente** de transação por adesão, consultado no Regularize **no dia** (condições mudam por edital).
- CTN, art. 174 (prescrição); CTN, arts. 150, § 4º, e 173 (decadência); Lei 6.830/1980, art. 40, e
  STJ, Tema 566 (prescrição intercorrente na execução fiscal).

Regras de transação mudam com frequência: **todo percentual, prazo e entrada vem do edital ou da
portaria vigente na data da análise, nunca de memória**.

## Automação x pessoa

| A IA faz | O Dr. Alex faz |
|---|---|
| Lê os extratos e monta o quadro do passivo (por inscrição, tributo, situação) | Confere o quadro com os extratos |
| Calcula a CAPAG e a faixa (A, B, C, D) e os cenários de desconto e parcela pelo edital informado | Confere a faixa, o edital e os cenários |
| Aponta possíveis prescrições, decadências e nulidades para conferência | Decide o que se sustenta juridicamente |
| Redige a primeira versão do parecer | Revisa, ajusta e aprova |

## Passo a passo

1. **Analisar nesta ordem** (IA aponta, Dr. Alex decide): — *D1*
   1. Prescrição do crédito e prescrição intercorrente nas execuções.
   2. Decadência.
   3. Nulidades da CDA.
   4. Impedimento de 2 anos por transação rescindida (Lei 13.988/2020, art. 4º, § 4º) **(conferir)**.
   5. Elegibilidade ao edital vigente.
   6. CAPAG presumida (a que a PGFN calculou) contra a CAPAG efetiva (a real da empresa).
   7. Execuções fiscais em curso, bloqueios e penhoras.
   8. Riscos de redirecionamento aos sócios e riscos penais (apropriação indébita, por exemplo).
2. **Decidir a estratégia pela árvore abaixo.** — *D1*
3. **Escrever o parecer** no timbrado: passivo, CAPAG, análise, elegibilidade, estratégia com
   cronograma e **três cenários** (conservador, provável, otimista) de desconto, entrada e parcela. — *D2*
4. **Aprovar** (Dr. Alex) e marcar a reunião de proposta (POP-TRIB-04). — *D2*

## Árvore de decisão

| Se encontrar | Então |
|---|---|
| Débito da Receita vencido há mais de 90 dias e ainda não inscrito em dívida ativa | Avaliar pedido de remessa à PGFN para inscrição, para poder transacionar (POP-TRIB-05, passo A) |
| Impedimento de 2 anos ativo | Transação bloqueada. Avaliar outras saídas (parcelamento ordinário, negócio jurídico processual) |
| CAPAG em faixa que não dá desconto, com chance real de mudar de faixa | Avaliar pedido de revisão da CAPAG (POP-TRIB-05, passo B) |
| Inscrições elegíveis ao edital vigente | Simular e aderir (POP-TRIB-05, passo C) |
| Parcelamento em risco de rescisão | **Quitar as parcelas vencidas antes de tudo** e avisar o cliente no mesmo dia |
| Execução fiscal com tese documental (prescrição, pagamento, nulidade) | Avaliar exceção de pré-executividade |
| Débito estadual ou municipal relevante | Avaliar programas próprios do estado ou município **(conferir)** |

Em regra, os descontos da transação alcançam os créditos classificados como de difícil recuperação
ou irrecuperáveis (faixas C e D) **(conferir no edital e na portaria vigentes)**.

## O que vira tarefa no ADVBOX

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[TRIB] Análise e parecer - {{cliente}}` | Dr. Alex | 2 dias úteis após o levantamento |
| `[TRIB] Reunião de proposta - {{cliente}}` | Dr. Alex | Até 2 dias úteis após o parecer |
| `[URGENTE] Parcelamento em risco - {{cliente}}` | Dr. Alex | Mesmo dia |

## Onde salva no Drive

`CLIENTES/{{cliente}}/05_TRIBUTARIO/02_RELATORIOS/` — `AAAA-MM-DD_PARECER-TRIBUTARIO_{{cliente}}.pdf` e a planilha de cenários.

## Pendências `[A CONFIRMAR]`
- Papel timbrado do escritório para o parecer.
- Itens marcados **(conferir)**: sempre pela norma e pelo edital vigentes na data.
