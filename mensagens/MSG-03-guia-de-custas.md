# MSG-03 — Guia de custas processuais

Versão 1 — 16/11/2026 · Usado no POP-OP-01

## Variáveis

| Variável | O que é |
|---|---|
| `{{nome_cliente}}` | Primeiro nome do cliente |
| `{{nome_escritorio}}` | Nome comercial do escritório `[A CONFIRMAR]` |
| `{{numero_processo}}` | Número do processo |
| `{{parte_contraria}}` | Nome da outra parte (ajuda o cliente a saber de qual processo se trata) |
| `{{tipo_custa}}` | Ex.: "custas iniciais", "preparo do recurso", "diligência do oficial de justiça" |
| `{{valor}}` | Valor da guia |
| `{{data_limite}}` | Prazo interno para o cliente pagar (prazo fatal menos 3 dias úteis) |
| `{{consequencia}}` | O que acontece se não pagar (ex.: "a ação é cancelada", "o recurso não é analisado") |
| `{{advogado_area}}` | Dr(a). responsável |
| `{{data_prazo}}` | Prazo fatal fixado pelo juízo (modelo 4) |

---

## Modelo 1 — Envio da guia

**WhatsApp** (anexar o PDF da guia)
> {{nome_cliente}}, o juiz determinou o recolhimento de {{tipo_custa}} no processo nº {{numero_processo}} (contra {{parte_contraria}}).
>
> Segue a guia em anexo:
> Valor: R$ {{valor}}
> Pagar até: {{data_limite}}
>
> Depois de pagar, envie por aqui o **comprovante de pagamento** (não serve comprovante de agendamento), para juntarmos no processo. Se não for paga a tempo, {{consequencia}}.

**E-mail** — Assunto: `Guia de custas — processo nº {{numero_processo}} — pagar até {{data_limite}}`
> Prezado(a) {{nome_cliente}},
>
> No processo nº {{numero_processo}}, em que a empresa litiga com {{parte_contraria}}, foi determinado o recolhimento de {{tipo_custa}}, no valor de R$ {{valor}}.
>
> Encaminhamos a guia em anexo, que deve ser paga até {{data_limite}}. Após o pagamento, pedimos o envio do comprovante de pagamento efetivado, para juntada no processo dentro do prazo.
>
> Ressaltamos que, sem o recolhimento no prazo, {{consequencia}}.
>
> Atenciosamente,
> {{nome_escritorio}}

## Modelo 2 — Lembrete (2 dias úteis depois do envio)

> {{nome_cliente}}, conseguiu pagar a guia de {{tipo_custa}} do processo nº {{numero_processo}} (R$ {{valor}})? O prazo para pagamento é {{data_limite}}. Assim que pagar, manda o comprovante por aqui.

## Modelo 3 — Lembrete no dia limite

> {{nome_cliente}}, hoje é o último dia combinado para o pagamento da guia de {{tipo_custa}} do processo nº {{numero_processo}} (R$ {{valor}}). Precisamos do comprovante para juntar no processo antes do prazo do juiz. Se houver alguma dificuldade, me avise agora que eu passo para o(a) {{advogado_area}}.

## Modelo 4 — Ciência de risco (prazo fatal menos 1 dia útil, após ligação do advogado)

**Enviar por WhatsApp e e-mail, e guardar no Drive.**
> Prezado(a) {{nome_cliente}},
>
> Até o momento não recebemos o comprovante de pagamento da guia de {{tipo_custa}} do processo nº {{numero_processo}}, no valor de R$ {{valor}}. O prazo determinado pelo juízo vence em {{data_prazo}}.
>
> Reforçamos que, sem o recolhimento e a comprovação no prazo, {{consequencia}}.
>
> Pedimos que nos envie o comprovante ainda hoje ou nos informe como deseja proceder.
>
> Atenciosamente,
> {{advogado_area}}
> {{nome_escritorio}}

## Modelo 5 — Comprovante recebido e juntado

> {{nome_cliente}}, recebemos o comprovante e já juntamos no processo nº {{numero_processo}}. Obrigado!
