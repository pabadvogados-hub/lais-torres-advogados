# MSG-02 — Cobrança de documentos (cadência)

Versão 1 — 16/11/2026 · Usado no POP-ATD-03 (onboarding), POP-OP-03 (trabalhista) e POP-OP-04 (cobrança)

## Variáveis

| Variável | O que é |
|---|---|
| `{{nome_cliente}}` | Primeiro nome do cliente |
| `{{nome_escritorio}}` | Nome comercial do escritório `[A CONFIRMAR]` |
| `{{nome_atendente}}` | Quem envia |
| `{{advogado_area}}` | Dr(a). responsável |
| `{{demanda}}` | Ex.: "a cobrança do cliente Fulano", "a defesa na reclamação trabalhista", "o diagnóstico da assessoria" |
| `{{lista_documentos}}` | Lista numerada do que falta |
| `{{lista_recebidos}}` | O que já chegou |
| `{{data_limite}}` | Data até quando precisamos dos documentos |
| `{{link_envio}}` | Link de envio, se houver (pasta ou formulário) `[A CONFIRMAR se haverá]` |
| `{{numero_processo}}`, `{{data_prazo}}` | Processo e prazo fatal (modelo 6) |
| `{{prazo_retorno}}` | Quando o cliente terá a próxima atualização (modelo 7) |

## Cadência

| Dia | Modelo | Canal |
|---|---|---|
| D1 | 1 — Pedido inicial | WhatsApp e e-mail |
| D3 | 2 — Lembrete com o que chegou e o que falta | WhatsApp |
| D5 | 3 — Lembrete curto | WhatsApp |
| D8 | Ligação do atendimento; se não atender, modelo 4 | Telefone + WhatsApp |
| D12 | 5 — Demanda parada | WhatsApp e e-mail |
| D15 | Advogado(a) liga. Se houver prazo processual, modelo 6 | Telefone + WhatsApp e e-mail |

Com prazo processual curto (audiência, prazo de defesa), **comprimir a cadência**: lembrete todo dia útil e ligação a partir do 2º dia.
Parar a cadência assim que a lista estiver completa e enviar o modelo 7.

---

## Modelo 1 — Pedido inicial (D1)

**WhatsApp**
> {{nome_cliente}}, para darmos andamento a {{demanda}}, precisamos dos documentos abaixo:
>
> {{lista_documentos}}
>
> Pode enviar por aqui mesmo (foto legível ou PDF) {{link_envio}}. Se algum item não existir, é só nos avisar que a empresa não tem. Precisamos de tudo até {{data_limite}}.

**E-mail** — Assunto: `Documentos para {{demanda}}`
> Prezado(a) {{nome_cliente}},
>
> Para darmos andamento a {{demanda}}, solicitamos o envio dos documentos abaixo até {{data_limite}}:
>
> {{lista_documentos}}
>
> Caso algum documento não exista, basta nos informar. Ficamos à disposição para qualquer dúvida.
>
> Atenciosamente,
> {{nome_atendente}}
> {{nome_escritorio}}

## Modelo 2 — Lembrete com o que chegou (D3)

> {{nome_cliente}}, obrigado pelo envio. Já recebemos:
> {{lista_recebidos}}
>
> Ainda faltam:
> {{lista_documentos}}

(Se nada chegou: "{{nome_cliente}}, passando para lembrar dos documentos de {{demanda}}. Ainda precisamos de: {{lista_documentos}}.")

## Modelo 3 — Lembrete curto (D5)

> {{nome_cliente}}, conseguiu separar os documentos de {{demanda}}? Se tiver dificuldade com algum item, me diga qual que eu te ajudo.

## Modelo 4 — Depois da ligação sem resposta (D8)

> {{nome_cliente}}, tentei te ligar agora sobre os documentos de {{demanda}}. Quando puder, me retorne ou envie por aqui. Faltam: {{lista_documentos}}.

## Modelo 5 — Demanda parada (D12)

> {{nome_cliente}}, {{demanda}} está parada aguardando os documentos abaixo. Sem eles não conseguimos avançar:
> {{lista_documentos}}
> O(a) {{advogado_area}} vai entrar em contato com você nos próximos dias.

## Modelo 6 — Ciência de risco quando há prazo (D15 ou antes, se o prazo apertar)

**Enviar por WhatsApp e por e-mail, e guardar no Drive.**
> Prezado(a) {{nome_cliente}},
>
> Informamos que, até esta data, não recebemos os documentos abaixo, necessários para {{demanda}}:
> {{lista_documentos}}
>
> O prazo no processo nº {{numero_processo}} vence em {{data_prazo}}. Sem esses documentos, a peça será apresentada apenas com as informações disponíveis, o que pode prejudicar a defesa dos interesses da empresa.
>
> Seguimos à disposição para recebê-los o quanto antes.
>
> Atenciosamente,
> {{advogado_area}}
> {{nome_escritorio}}

## Modelo 7 — Documentos completos

> {{nome_cliente}}, recebemos todos os documentos, obrigado. Agora o(a) {{advogado_area}} segue com {{demanda}} e te atualizamos até {{prazo_retorno}}.
