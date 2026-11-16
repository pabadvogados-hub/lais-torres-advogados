# POP-TRIB-06 — Tributário: acompanhamento mensal das parcelas

Versão 1 — 16/11/2026

| | |
|---|---|
| **Dono do POP** | Dr. Alex |
| **Quem executa** | Estagiário(a) do tributário `[A CONFIRMAR quem]` |
| **Gatilho** | Todo mês, dia 1 |
| **Termina quando** | Todas as parcelas do mês pagas e conferidas |
| **Prazo** | Ciclo mensal (tabela abaixo) |

## Objetivo

Nenhuma transação ou parcelamento cai por parcela esquecida. A rescisão de transação gera
**impedimento de 2 anos** para nova transação (Lei 13.988/2020, art. 4º, § 4º) **(conferir)**: é o pior
resultado possível para o cliente e para o êxito do escritório.

## Automação x pessoa

| A automação faz | A pessoa faz |
|---|---|
| Lista as negociações ativas no dia 1 | Confere cada uma no e-CAC e no Regularize |
| Envia as guias ao cliente com a mensagem padrão | Emite as guias quando o sistema exigir login |
| Lembra o cliente do vencimento | Confere o pagamento e liga para quem não pagou |

## Ciclo mensal

| Quando | O que fazer |
|---|---|
| **Dia 1** | Listar todas as negociações ativas (cliente, modalidade, nº de parcelas, vencimento) |
| **Dias 1 a 19** | Conferir cada negociação e marcar o **farol** (abaixo) |
| **A partir do dia 20** | Enviar as guias do mês ao cliente com a mensagem padrão `[A CONFIRMAR dia de vencimento das parcelas de cada modalidade]` |
| **5 dias úteis após o envio** | Conferir o pagamento. Não pagou: ligar |
| **Mesmo dia** | Qualquer notificação de rescisão: avisar o Dr. Alex e o cliente |

## Farol

| Cor | Situação | Ação |
|---|---|---|
| Verde | Tudo em dia | Seguir o ciclo |
| Amarelo | 1 parcela atrasada | Ligar para o cliente no mesmo dia e mandar a guia |
| Vermelho | 2 ou mais parcelas atrasadas, entrada ou última parcela pendente, ou débito novo inscrito | Avisar o Dr. Alex no mesmo dia |
| Preto | Notificação de rescisão | Dr. Alex liga para o cliente e avalia impugnação dentro do prazo da notificação **(conferir prazo na notificação e na portaria)** |

Na dúvida entre duas cores, vale a mais grave.

## O que vira tarefa no ADVBOX

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[TRIB] Farol mensal das negociações - {{AAAA-MM}}` | Estagiário(a) do tributário | Dia 19 |
| `[TRIB] Enviar guias - {{AAAA-MM}}` | Estagiário(a) do tributário | Dia 20 |
| `[TRIB] Conferir pagamentos - {{AAAA-MM}}` | Estagiário(a) do tributário | 5 dias úteis após o envio |
| `[URGENTE] Rescisão - {{cliente}}` | Dr. Alex | Mesmo dia |

## Onde salva no Drive

`CLIENTES/{{cliente}}/05_TRIBUTARIO/01_DOCUMENTOS_FISCAIS/PARCELAS/AAAA-MM_guia.pdf` e `AAAA-MM_comprovante.pdf`.

## Pendências `[A CONFIRMAR]`
- Quem executa o controle mensal.
- Data de vencimento das parcelas em cada modalidade de transação.
