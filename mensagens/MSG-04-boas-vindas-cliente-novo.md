# MSG-04 — Boas-vindas do cliente novo

Versão 1 — 16/11/2026 · Usado no POP-ATD-03, passo 1 (até 2 horas úteis depois do fechamento)

## Variáveis

| Variável | O que é |
|---|---|
| `{{nome_cliente}}` | Primeiro nome do cliente (ou do responsável na empresa) |
| `{{empresa}}` | Nome da empresa |
| `{{nome_escritorio}}` | Nome comercial do escritório `[A CONFIRMAR]` |
| `{{numero_clientes_casa}}` | WhatsApp exclusivo dos clientes `[A CONFIRMAR]` |
| `{{email_atendimento}}` | E-mail de atendimento `[A CONFIRMAR]` |
| `{{horario_atendimento}}` | Horário de atendimento `[A CONFIRMAR]` |
| `{{advogado_area}}` | Dr(a). responsável pelo caso |
| `{{lista_dados_contrato}}` | Dados para o contrato (`CK-DIA-04`) |
| `{{link_assinatura}}` | Link de assinatura eletrônica |

---

## Modelo 1 — Assessoria mensal (empresa)

**WhatsApp**
> {{nome_cliente}}, seja muito bem-vindo(a) ao {{nome_escritorio}}! É uma alegria ter a {{empresa}} com a gente.
>
> Como vai funcionar a partir de agora:
>
> 1. **Canal de atendimento**: este número ({{numero_clientes_casa}}) e o e-mail {{email_atendimento}}, {{horario_atendimento}}. Qualquer dúvida do dia a dia da empresa, é só chamar: é melhor perguntar antes do que resolver depois.
> 2. **Contrato**: para emitir o contrato, me envie, por favor:
> {{lista_dados_contrato}}
> 3. **Diagnóstico da empresa**: nos próximos dias vamos enviar uma lista de documentos das áreas trabalhista, tributária, de cobrança e de consumidor. Com ela fazemos o diagnóstico da {{empresa}} e o plano de trabalho dos próximos meses.
>
> Urgência (citação, audiência, fiscalização, prazo vencendo): escreva "URGENTE" que o advogado responsável é avisado na hora.

## Modelo 2 — Tributário (transação, CAPAG, PGFN)

> {{nome_cliente}}, seja muito bem-vindo(a) ao {{nome_escritorio}}! O Dr. Alex vai conduzir a regularização tributária da {{empresa}}.
>
> Próximos passos:
> 1. Contrato: segue o link para assinatura: {{link_assinatura}}
> 2. Procuração no e-CAC: se ainda não fez, te mando o passo a passo (leva cerca de 2 minutos com o gov.br).
> 3. Com a procuração, levantamos todo o passivo e voltamos com a estratégia e o cronograma.
>
> Qualquer dúvida, este é o nosso canal ({{numero_clientes_casa}}), {{horario_atendimento}}.

## Modelo 3 — Causa única (um processo ou demanda)

> {{nome_cliente}}, seja muito bem-vindo(a) ao {{nome_escritorio}}! O(a) {{advogado_area}} vai cuidar do seu caso.
>
> Próximos passos:
> 1. Contrato e procuração: segue o link para assinatura: {{link_assinatura}}
> 2. Documentos: em seguida te mando a lista do que precisamos para preparar a peça.
>
> Nosso canal de atendimento é este número ({{numero_clientes_casa}}), {{horario_atendimento}}.

## Modelo 4 — Contrato assinado

> {{nome_cliente}}, recebemos o contrato assinado, obrigado! A partir de agora a {{empresa}} já conta com a gente. Em seguida te mando a lista de documentos para começarmos.

## E-mail de boas-vindas (para os três tipos)

Assunto: `Bem-vindo(a) ao {{nome_escritorio}}`
> Prezado(a) {{nome_cliente}},
>
> Seja bem-vindo(a) ao {{nome_escritorio}}. Agradecemos a confiança.
>
> Seus canais de atendimento são o WhatsApp {{numero_clientes_casa}} e este e-mail, {{email_atendimento}}, {{horario_atendimento}}. O(a) {{advogado_area}} será o(a) responsável pelo seu atendimento técnico.
>
> Nos próximos dias enviaremos a lista de documentos necessários para iniciarmos o trabalho.
>
> Atenciosamente,
> {{nome_escritorio}}
