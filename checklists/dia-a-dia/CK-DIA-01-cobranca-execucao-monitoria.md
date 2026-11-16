# CK-DIA-01 — Demanda nova: cobrança, execução ou monitória

Versão 1 — 16/11/2026 · Dono: Dra. Larissa · Usado no POP-ATD-01 (passo 5) e no POP-OP-04

**Quando usar**: o cliente de assessoria pede para cobrar alguém que não pagou.
**Quem usa**: atendimento pergunta ao cliente e cobra os documentos; Dra. Larissa escolhe a via.
**Um checklist por devedor.**

## 1. Credor (cliente)

| Item | Resposta / OK |
|---|---|
| Empresa credora (razão social e CNPJ) — se for outra empresa do grupo, qual | |
| Procuração do escritório válida para essa empresa (se não, ver `CK-DIA-04`) | ( ) |
| Quem do cliente acompanha esta cobrança (nome e telefone) | |

## 2. Devedor

| Item | Resposta / OK |
|---|---|
| Nome completo ou razão social | |
| CPF ou CNPJ | |
| Endereço completo (residencial e, se souber, do trabalho ou da empresa) | |
| Telefone, WhatsApp e e-mail | |
| Bens que o cliente conhece (veículo, imóvel, empresa, conta bancária) | |
| Se for empresa: nome dos sócios | |

## 3. Dívida

| Item | Resposta / OK |
|---|---|
| O que foi vendido ou que serviço foi prestado | |
| Valor original | |
| Data(s) de vencimento | |
| Pagamentos parciais (datas e valores) | |
| Juros, multa e correção combinados no contrato (se houver) | |
| Já houve cobrança? Como e quando (mensagem, notificação, protesto, negativação) | |
| O devedor reconheceu a dívida por escrito (mensagem, e-mail, proposta de acordo)? | ( ) Sim ( ) Não |

## 4. Documentos (marque o que o cliente tem e envie)

| Documento | Tem | Enviado |
|---|---|---|
| Cheque (frente e verso) | ( ) | ( ) |
| Nota promissória | ( ) | ( ) |
| Duplicata + comprovante de entrega da mercadoria ou do serviço + protesto (se sem aceite) | ( ) | ( ) |
| Contrato ou confissão de dívida assinado pelo devedor | ( ) | ( ) |
| ... assinado também por 2 testemunhas (ou assinatura eletrônica válida) | ( ) | ( ) |
| Orçamento ou ordem de serviço assinada pelo devedor | ( ) | ( ) |
| Nota fiscal e canhoto assinado / comprovante de entrega | ( ) | ( ) |
| Conversas de WhatsApp ou e-mails sobre a dívida (prints com data e número) | ( ) | ( ) |
| Boletos emitidos e não pagos | ( ) | ( ) |
| Comprovantes de cobranças anteriores (notificação, protesto, negativação) | ( ) | ( ) |

## 5. O que o cliente quer

| Item | Resposta |
|---|---|
| Tentar acordo antes ou judicializar direto? | |
| Desconto máximo autorizado para acordo | |
| Número máximo de parcelas aceito | |
| Quem paga as custas iniciais (cliente paga a guia ou escritório adianta com reembolso) | `[A CONFIRMAR política]` |

## 6. Análise (preenche a Dra. Larissa)

| Item | Resposta |
|---|---|
| Prescrição conferida (data-limite) | |
| Via | ( ) Execução ( ) Monitória ( ) Cobrança ( ) Juizado ( ) Só extrajudicial |
| Valor atualizado e critério | |
| Pedidos de pesquisa e bloqueio de bens na inicial | |
| Prazo para protocolo | |

Salvar em: antes da ação, `CLIENTES/{{cliente}}/03_EXTRAJUDICIAL/AAAA-MM-DD - Cobrança {{devedor}}/`; depois de distribuída, `02_JUDICIAL/{{nº}} - {{devedor}} - {{via}}/`.
