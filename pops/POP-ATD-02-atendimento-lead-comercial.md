# POP-ATD-02 — Atendimento de lead e comercial

Versão 1 — 16/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Laís (assessoria e demais áreas) e Dr. Alex (produto tributário) |
| **Quem executa** | Responsável pelo comercial `[A CONFIRMAR quem]`; automação de primeiro contato no Infinitum |
| **Gatilho** | Mensagem de pessoa que ainda não é cliente no número comercial, formulário do site ou campanha |
| **Termina quando** | Reunião marcada com a Laís ou o Alex, lead encaminhado ao POP-TRIB-01, lead descartado com motivo, ou lead em nutrição após o último toque |
| **Prazo máximo de primeira resposta** | **5 minutos** pela automação; **15 minutos úteis** pela pessoa |

## Objetivo

Separar o lead do cliente da casa (números diferentes, atendimento diferente) e responder rápido.
Hoje chega cerca de um cliente novo por semana, quase sempre por indicação. Com o tráfego do produto
tributário do Alex esse volume vai crescer, e este POP evita que o comercial vire bagunça.

## Qual número e qual identidade usar

| Origem do lead | Número | Identidade apresentada |
|---|---|---|
| Campanha ou contato **de fora do Maranhão** | WhatsApp 62 `{{numero_comercial_62}}` `[A CONFIRMAR]` | Laís Torres Advogados, Goiânia/GO: CNPJ 58.232.242/0001-90, Av. D nº 419, Qd. G11, Lt. 01, Ed. Comercial Marista, sala 401, Goiânia/GO |
| Público **local** (Imperatriz e região: MA, PA, TO) | WhatsApp 99 do Dr. Alex, (99) 9114-2002 | Escritório de Imperatriz/MA `[A CONFIRMAR CNPJ e endereço de Imperatriz]` |

Regra de honestidade: a sede de Goiânia é a que aparece nas campanhas nacionais. Se o lead perguntar
onde a equipe trabalha, a resposta é a verdade: atendimento digital para todo o Brasil, com sede em
Goiânia/GO e equipe também em Imperatriz/MA.

## Prazos (SLA)

| Etapa | Prazo |
|---|---|
| Primeira mensagem ao lead | 5 minutos (automação). Sem automação: 15 minutos úteis |
| Qualificação (perguntas básicas respondidas) | Até 24 horas |
| Reunião com o sócio | Oferecida em até 2 dias úteis |
| Cadência de follow-up | Até 15 dias corridos (tabela no passo 5) |

## Automação x pessoa

| A automação faz | A pessoa faz |
|---|---|
| Primeira resposta em até 5 minutos (MSG-05, modelo 1) | Assume a conversa e faz a qualificação |
| Cria o card do lead no Infinitum com origem e número | Preenche os campos do card |
| Dispara os toques de follow-up nos dias da cadência | Faz as ligações da cadência e personaliza as mensagens |
| Lembra a reunião na véspera e 1 hora antes | Confirma presença e recupera quem faltou |

## Passo a passo

1. **Responder em até 5 minutos** dizendo quem somos e perguntando como podemos ajudar (MSG-05, modelo 1). — *5 min*
2. **Qualificar o lead.** Perguntar, sem parecer interrogatório: — *até 24h*
   1. Nome e, se for empresa, nome da empresa e CNPJ.
   2. Cidade e estado.
   3. O que está precisando (em uma frase).
   4. É uma demanda pontual ou a empresa quer um jurídico mensal (assessoria)?
   5. Tem prazo correndo ou documento recebido (citação, notificação, cobrança)?
   6. Quem decide a contratação.
3. **Classificar e encaminhar.** — *no mesmo dia*

   | O lead quer | Encaminhamento |
   |---|---|
   | Dívida com a Receita ou a PGFN, parcelamento, transação, CAPAG | **POP-TRIB-01** (Dr. Alex) |
   | Assessoria jurídica mensal para empresa | Reunião de diagnóstico com a **Dra. Laís** |
   | Defesa trabalhista, cobrança, contrato, consumidor | Reunião com a Dra. Laís; caso pontual pode virar contrato de causa única |
   | Previdenciário | Dra. Larissa `[A CONFIRMAR se o produto já está ativo]` |
   | Área que o escritório não atende | Agradecer e encerrar com cordialidade; registrar o motivo no card |
   | Urgência (prazo vencendo, audiência marcada) | Avisar a Dra. Laís por ligação no mesmo momento |

4. **Marcar a reunião.** Oferecer duas opções de horário ("hoje à tarde ou amanhã de manhã?"),
   mandar o convite e confirmar três vezes: ao agendar, na véspera e 1 hora antes. Se o lead faltar,
   recuperar no mesmo dia perguntando o melhor dia e período. — *reunião em até 2 dias úteis*
5. **Seguir a cadência de follow-up** enquanto o lead não marcar ou não responder (MSG-05, modelos 2 a 6):

   | Dia | Toque |
   |---|---|
   | D0 | Primeira mensagem |
   | D1 | Mensagem curta retomando a necessidade dele |
   | D3 | Ligação; se não atender, mensagem avisando que ligou |
   | D5 | Conteúdo útil sobre o problema dele (sem promessa de resultado) |
   | D8 | Ligação |
   | D11 | Mensagem de honestidade: "ainda faz sentido conversarmos?" |
   | D15 | Despedida cordial; lead vai para nutrição |

6. **Registrar tudo no Infinitum**: origem, qualificação, ligações, motivo de perda. — *a cada contato*
7. **Fechou contrato**: mover o card para "Fechado" e iniciar o **POP-ATD-03** (onboarding). — *no mesmo dia*

## Regras

- Nada de promessa de resultado, de percentual de desconto ou de prazo de êxito. No tributário,
  desconto só se fala depois do diagnóstico (POP-TRIB-03).
- Valor de honorário só é informado pela Dra. Laís ou pelo Dr. Alex.
- A comunicação segue as regras de publicidade da advocacia (Código de Ética e Disciplina da OAB e
  Provimento 205/2021 do CFOAB) **(conferir)**: sem mercantilização, sem oferta de preço ou desconto
  como chamariz.
- Lead nunca é atendido pelo número dos clientes da casa.

## O que vira tarefa no ADVBOX

O lead fica no **Infinitum** (CRM), não no ADVBOX. Só entra no ADVBOX quando fechar contrato
(POP-ATD-03). Exceção: lead com urgência processual que já contratou verbalmente: `[URGENTE] {{assunto}} - {{lead}}` para o advogado(a) da área.

## Onde salva no Drive

`05 COMERCIAL/{{AAAA-MM}}/{{nome do lead}}/` — documentos que o lead mandar antes de fechar e a proposta enviada.
Ao fechar, a pasta é movida para `04 CLIENTES/{{nome do cliente}}/01 CONTRATO E DOCUMENTOS/`.

## Pendências `[A CONFIRMAR]`
- Qual número fica comercial (sugestão do projeto: 62) e confirmação de que o 99 segue com o público local.
- CNPJ e endereço do escritório de Imperatriz/MA.
- Quem executa o comercial.
- Se o previdenciário já é oferecido.
