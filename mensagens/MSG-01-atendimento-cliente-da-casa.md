# MSG-01 — Atendimento do cliente da casa (assessoria)

Versão 1 — 16/11/2026 · Usado no POP-ATD-01

## Variáveis

| Variável | O que é |
|---|---|
| `{{nome_cliente}}` | Primeiro nome de quem escreveu |
| `{{empresa}}` | Nome da empresa cliente |
| `{{nome_atendente}}` | Nome de quem está atendendo |
| `{{nome_escritorio}}` | Nome comercial do escritório `[A CONFIRMAR: como os clientes conhecem o escritório]` |
| `{{advogado_area}}` | Dr(a). responsável pela área do assunto |
| `{{prazo_retorno}}` | Dia e horário em que o cliente terá o retorno (ex.: "hoje até as 17h") |
| `{{assunto}}` | Assunto em poucas palavras |
| `{{horario_atendimento}}` | Horário de atendimento `[A CONFIRMAR]` |
| `{{numero_processo}}`, `{{data}}` | Número do processo e data da movimentação (modelo 6) |
| `{{andamento_em_linguagem_simples}}`, `{{proximo_passo}}` | Tradução do andamento do ADVBOX, sem juridiquês (modelo 6) |

Regras: mensagens curtas, sem emoji, sem gíria. Sempre dizer **quem** vai cuidar e **até quando**.
Responder pelo mesmo canal em que o cliente escreveu (WhatsApp ou e-mail).

---

## Modelo 1 — Confirmação de recebimento (automática ou em até 30 minutos)

**WhatsApp**
> Olá, {{nome_cliente}}! Recebemos sua mensagem aqui no {{nome_escritorio}}. Já estamos verificando e em breve retornamos com a posição.

**Fora do horário**
> Olá, {{nome_cliente}}! Recebemos sua mensagem. Nosso atendimento funciona {{horario_atendimento}} e retornaremos no início do próximo expediente. Se for urgente (audiência, citação, fiscalização ou prazo vencendo), escreva "URGENTE" que avisamos o advogado responsável.

**E-mail** — Assunto: `Recebemos sua mensagem — {{assunto}}`
> Prezado(a) {{nome_cliente}},
>
> Confirmamos o recebimento da sua mensagem sobre {{assunto}}. Nossa equipe já está verificando e retornaremos até {{prazo_retorno}}.
>
> Atenciosamente,
> {{nome_atendente}}
> {{nome_escritorio}}

---

## Modelo 2 — Primeira resposta humana (até 1 hora útil)

> {{nome_cliente}}, aqui é {{nome_atendente}}, do atendimento do {{nome_escritorio}}. Vou cuidar da sua solicitação sobre {{assunto}}. [resposta direta, ou: "Para encaminhar ao(à) {{advogado_area}}, preciso de algumas informações:"]

---

## Modelo 3 — Pedido de informações de demanda nova

**WhatsApp**
> {{nome_cliente}}, para o(a) {{advogado_area}} analisar com segurança, me ajuda com estas informações:
>
> 1. O que aconteceu, em poucas palavras?
> 2. Quando aconteceu? Tem alguma data ou prazo envolvido?
> 3. Quem é a outra parte (nome e CPF/CNPJ, se tiver)?
> 4. Recebeu algum documento (notificação, citação, e-mail, carta)? Pode mandar foto ou PDF aqui mesmo.
> 5. Qual o valor envolvido, se houver?
> 6. O que a empresa espera que a gente faça?
>
> Se for mais fácil, pode responder por áudio que eu organizo aqui.

**Variações por tipo de demanda** (substituir a lista acima pela lista do checklist):
- Cobrança de cliente que não pagou: perguntas e documentos do `CK-DIA-01`.
- Reclamação trabalhista recebida: começar por "Me envie, por favor, a foto ou o PDF da notificação, com todas as páginas, e a data em que a empresa recebeu." Depois, `CK-DIA-02`.
- Cliente da oficina que recusou serviço: `CK-DIA-03`.

**E-mail** — Assunto: `{{assunto}} — informações para análise`
> Prezado(a) {{nome_cliente}},
>
> Para que o(a) {{advogado_area}} possa analisar a demanda com segurança, pedimos a gentileza de nos enviar as informações e documentos abaixo:
>
> [lista do checklist]
>
> Assim que recebermos, retornaremos com o encaminhamento em até 2 dias úteis.
>
> Atenciosamente,
> {{nome_atendente}}
> {{nome_escritorio}}

---

## Modelo 4 — Retorno com encaminhamento e prazo (no mesmo dia útil)

> {{nome_cliente}}, recebemos tudo, obrigado. Sua demanda sobre {{assunto}} já está com o(a) {{advogado_area}}, que vai retornar até {{prazo_retorno}}. Qualquer novidade antes disso, te aviso por aqui.

**Urgência**
> {{nome_cliente}}, já passei sua demanda para o(a) {{advogado_area}}, que vai te retornar até {{prazo_retorno}}. Enquanto isso, guarde todos os documentos que recebeu e não assine nada sem falar com a gente.

---

## Modelo 5 — Aviso antes de o prazo prometido passar

> {{nome_cliente}}, passando para dar posição sobre {{assunto}}: o(a) {{advogado_area}} ainda está finalizando a análise e o novo prazo de retorno é {{prazo_retorno}}. Obrigado pela compreensão.

---

## Modelo 6 — Andamento de processo ("como está meu processo?")

> {{nome_cliente}}, consultei o processo nº {{numero_processo}}. Última movimentação, em {{data}}: {{andamento_em_linguagem_simples}}. Próximo passo: {{proximo_passo}}. Não há nenhuma providência necessária da sua parte neste momento. [ou: "Precisamos de você para: ..."]

Se o andamento for decisão, sentença ou prazo: **não explicar antes de confirmar com o(a) advogado(a) da área.** Enviar:
> {{nome_cliente}}, saiu uma decisão no processo nº {{numero_processo}}. O(a) {{advogado_area}} está analisando e te explica o que muda até {{prazo_retorno}}.

---

## Modelo 7 — Encerramento

> {{nome_cliente}}, conseguimos resolver o que você precisava sobre {{assunto}}? Se ficou alguma dúvida, é só chamar por aqui.
