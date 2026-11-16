# POP-ADM-02 — Pagamento mensal da equipe e das despesas fixas

Versão 1 — 16/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Laís |
| **Quem executa** | Agente financeiro (agenda, avisa, arquiva); Dra. Laís (aprova com o token) |
| **Gatilho** | Dia de pagamento de cada colaborador ou vencimento de cada despesa fixa |
| **Termina quando** | Pagamento aprovado, comprovante na pasta do colaborador ou do mês, relatório do mês atualizado |
| **Prazo** | Aprovação até 10h do dia do pagamento |

## Objetivo

Acabar com o "todo mês procurar a chave Pix na conversa do WhatsApp e pagar um por um". Cada
colaborador e cada despesa fixa fica cadastrado uma vez no Asaas, o Pix é agendado, e a Dra. Laís só
**aprova o token** de manhã.

## Automação x pessoa

| O agente financeiro faz | A Dra. Laís faz |
|---|---|
| Mantém o cadastro de cada colaborador e despesa fixa no Asaas (dados do POP-ADM-01) | Confere o cadastro na primeira vez |
| Agenda o Pix ou o pagamento do boleto na data de cada um | Autoriza qualquer mudança de valor, data ou chave |
| No dia, às 8h, manda no WhatsApp da Laís a lista do que vai sair e o saldo | Aprova no Asaas com o token de segurança |
| Avisa com 2 dias úteis de antecedência se o saldo não cobre os pagamentos | Decide o que fazer (transferir, adiar) |
| Baixa o comprovante e salva na pasta certa | — |
| Atualiza o relatório do mês (o que entrou, o que saiu, custo da equipe) | Lê o relatório |

## Passo a passo

### Cadastro (uma vez por colaborador ou despesa)

1. **Colaborador**: cadastrar no Asaas nome, CPF e chave Pix **informados pelo próprio colaborador
   no formulário do POP-ADM-01** (nunca copiar de conversa antiga). Valor e dia de pagamento definidos pela Dra. Laís.
2. **Despesa fixa** (aluguel, impostos, ADVBOX, internet, Google Workspace, VPS e outras): cadastrar
   favorecido, valor ou forma de cálculo, vencimento e forma de pagamento (Pix ou boleto).
3. **Agendar** os pagamentos recorrentes no Asaas `[A CONFIRMAR: recurso de agendamento recorrente
   disponível na conta]`.

### Todo mês

| Quando | O que acontece |
|---|---|
| **2 dias úteis antes** de cada pagamento | Agente confere se o saldo do Asaas cobre os pagamentos do dia. Se não cobrir, avisa a Dra. Laís |
| **Dia do pagamento, 8h** | Agente manda à Dra. Laís a lista: quem recebe, valor, chave, total do dia, saldo |
| **Até 10h** | Dra. Laís confere e aprova no Asaas com o token de segurança `[A CONFIRMAR: como o token chega — app, SMS ou outro]` |
| **Logo após a aprovação** | Agente baixa o comprovante e salva: colaborador em `RH/{{nome}}/03_PAGAMENTOS/AAAA-MM_comprovante.pdf`; despesa em `FINANCEIRO/AAAA/MM/` |
| **Até 18h** | Se algum pagamento falhou (chave inválida, saldo), avisar a Dra. Laís |
| **Último dia útil do mês** | Relatório do mês: entradas, saídas, custo da equipe, despesas fixas e eventuais |

### Mudanças

- **Aumento, desconto, nova pessoa, desligamento**: só com ordem da Dra. Laís, por escrito. Agente atualiza o cadastro e o agendamento no mesmo dia.
- **Troca de chave Pix**: só depois de confirmar com o colaborador **por ligação ou pessoalmente**.
  Pedido de troca de chave por mensagem é um golpe comum.
- **Estagiário**: no mês do recesso, a bolsa continua se o termo prever bolsa (Lei 11.788/2008, art. 13, § 1º).
- **Tributos e encargos** sobre os pagamentos (recibo, retenções, eSocial, conforme o vínculo):
  conferir com o contador `[A CONFIRMAR]`.

## O que vira tarefa no ADVBOX

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[FINANCEIRO] Aprovar pagamentos do dia - {{data}}` | Dra. Laís | 10h do dia |
| `[FINANCEIRO] Relatório do mês - {{AAAA-MM}}` | Agente financeiro | Último dia útil do mês |

## Onde salva no Drive

- Colaborador: `RH/{{NOME}} - {{VÍNCULO}}/03_PAGAMENTOS/AAAA-MM_comprovante.pdf`
- Despesas fixas e relatório: `FINANCEIRO/AAAA/MM/`

## Pendências `[A CONFIRMAR]`
- Lista da equipe: nome, função, vínculo, valor, dia de pagamento e chave Pix de cada pessoa (pedido no Projeto, até 18/11).
- Lista de despesas fixas: favorecido, valor, vencimento.
- Recurso de Pix agendado recorrente e forma de recebimento do token na conta Asaas.
- Orientação do contador sobre recibos e encargos de cada vínculo.
