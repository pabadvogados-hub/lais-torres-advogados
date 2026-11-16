# POP-TRIB-04 — Tributário: proposta e fechamento

Versão 1 — 16/11/2026

| | |
|---|---|
| **Dono do POP** | Dr. Alex |
| **Quem executa** | Dr. Alex |
| **Gatilho** | Parecer aprovado (POP-TRIB-03) |
| **Termina quando** | Contrato assinado e onboarding iniciado (POP-ATD-03), ou retorno marcado em até 48 horas |
| **Prazo** | Reunião em até 2 dias úteis após o parecer |

## Objetivo

Apresentar ao cliente o passivo real, a economia possível em reais e a proposta de honorários,
e sair da reunião com contrato assinado ou com a objeção real identificada.

## Honorários

- **Clientes novos: 25% sobre o proveito econômico** (o desconto efetivamente obtido).
- **Clientes antigos: 10%** (mantido, sem reajuste).
- Valor fixo de entrada ou de diagnóstico: `[A CONFIRMAR se existe e qual valor]`.
- Desconto ou condição fora da tabela: **só o Dr. Alex decide**. Nenhum robô, estagiário ou comercial negocia preço.

## Passo a passo

1. **Apresentar os três números** do parecer: passivo real (PGFN e Receita), faixa de CAPAG e
   desconto possível, economia em reais. — *reunião*
2. **Apresentar a proposta**: honorários sobre o proveito econômico e, se houver, o fixo. Mostrar o
   retorno: economia dividida pelo honorário. — *reunião*
3. **Responder às objeções**:
   - "É caro": mostrar o retorno com os números do parecer.
   - "Não tenho para pagar o honorário agora": o êxito só é devido sobre o desconto obtido.
   - "Meu contador cuida disso": propor reunião a três com o contador.
   - "Isso é golpe?": tudo é feito nos canais oficiais (Regularize e e-CAC); nada é pago a intermediário.
4. **Fechar ou descobrir a objeção**: se aceitar, o contrato sai na hora para assinatura eletrônica.
   Se disser "vou pensar", descobrir a objeção real antes de encerrar e marcar retorno em até 48 horas. — *reunião*
5. **Passar ao operacional**: mover o card para "Fechado" e seguir o POP-ATD-03 (contrato, Asaas,
   Drive, ADVBOX) e o POP-TRIB-05. — *mesmo dia*

## O que vira tarefa no ADVBOX

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[TRIB] Retorno da proposta - {{cliente}}` | Dr. Alex | 48 horas após a reunião (se não fechou) |
| `[TRIB] Adesão / medidas preparatórias - {{cliente}}` | Dr. Alex | Conforme cronograma do parecer |

## Onde salva no Drive

Proposta e contrato: `CLIENTES/{{cliente}}/01_CONTRATO_E_DOCUMENTOS/`.

## Pendências `[A CONFIRMAR]`
- Existência e valor de honorário fixo no produto tributário.
- Forma de cálculo e momento de cobrança do êxito (na adesão, parcelado com as parcelas da transação, outro).
