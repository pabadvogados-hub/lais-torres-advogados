# MSG-06 — Aviso de mudança de número aos clientes da casa

Versão 1 — 16/11/2026 · Usado na implantação do Módulo 1 (migração dos ~15 clientes fixos de assessoria para o número exclusivo)

## Variáveis

| Variável | O que é |
|---|---|
| `{{nome_cliente}}` | Primeiro nome do contato na empresa |
| `{{empresa}}` | Nome da empresa |
| `{{nome_escritorio}}` | Nome comercial `[A CONFIRMAR]` |
| `{{numero_novo}}` | Número exclusivo dos clientes da casa `[A CONFIRMAR]` |
| `{{numero_antigo}}` | Número pelo qual o cliente fala hoje (62 da Laís ou 99 do Alex) |
| `{{data_mudanca}}` | Data a partir da qual o atendimento passa para o número novo `[A CONFIRMAR]` |
| `{{remetente}}` | Dra. Laís (clientes de Goiânia, que a conhecem pelo 62) ou Dr. Alex (clientes do Maranhão, que o conhecem pelo 99) |
| `{{outro_socio}}` | O outro sócio ("Dr. Alex" quando quem assina é a Laís; "Dra. Laís" quando é o Alex) |

## Como fazer a migração

1. **Enviar do número antigo** (o que o cliente já conhece), assinado por quem o cliente conhece
   (Dra. Laís ou Dr. Alex). Mensagem de número desconhecido parece golpe.
2. **No mesmo dia, o número novo manda a primeira mensagem** (modelo 2), para o cliente salvar o contato.
3. **Durante 30 dias** `[A CONFIRMAR prazo]`, se o cliente escrever no número antigo, responder
   normalmente e lembrar do número novo (modelo 3). Não deixar sem resposta.
4. Depois de 30 dias, o número antigo responde automaticamente com o modelo 4.
5. Lista de controle: marcar cada cliente avisado e cada cliente que já escreveu no número novo `[A CONFIRMAR lista dos ~15 clientes]`.

---

## Modelo 1 — Aviso (enviado do número antigo, pela Laís ou pelo Alex)

> {{nome_cliente}}, tudo bem? Aqui é {{remetente}}.
>
> Para atender a {{empresa}} cada vez mais rápido, criamos um WhatsApp exclusivo para os nossos clientes de assessoria: **{{numero_novo}}**.
>
> A partir de {{data_mudanca}}, todas as demandas, dúvidas e documentos devem ser enviados por esse número. Ele é atendido pela nossa equipe todos os dias úteis, e eu e o(a) {{outro_socio}} continuamos acompanhando tudo de perto.
>
> Daqui a pouco você vai receber uma mensagem desse número: é só salvar o contato. Se tiver qualquer dúvida, me chama aqui.

## Modelo 2 — Primeira mensagem do número novo (mesmo dia)

> {{nome_cliente}}, aqui é o atendimento do {{nome_escritorio}}, no número exclusivo para os clientes de assessoria, como {{remetente}} avisou. Salve este contato. A partir de {{data_mudanca}}, é por aqui que a {{empresa}} fala com a gente. Estamos à disposição.

## Modelo 3 — Cliente escreveu no número antigo (durante a transição)

> {{nome_cliente}}, recebido! Já encaminhei para a equipe, que vai te responder pelo número de atendimento ({{numero_novo}}). Para as próximas demandas, chame direto por lá, que o retorno é mais rápido.

## Modelo 4 — Resposta automática do número antigo (depois da transição)

> Olá! O atendimento aos clientes de assessoria do {{nome_escritorio}} agora é feito pelo número {{numero_novo}}. Por favor, envie sua mensagem por lá para ser atendido(a) com mais rapidez. Obrigado!

## E-mail (para quem usa mais o e-mail)

Assunto: `Novo WhatsApp de atendimento — {{nome_escritorio}}`
> Prezado(a) {{nome_cliente}},
>
> Informamos que, a partir de {{data_mudanca}}, o atendimento da {{empresa}} pelo WhatsApp passa a ser feito pelo número exclusivo para clientes de assessoria: {{numero_novo}}.
>
> O atendimento por este e-mail continua normalmente.
>
> Atenciosamente,
> {{remetente}}
> {{nome_escritorio}}
