# POP-ATD-01 — Atendimento do cliente de assessoria

Versão 1 — 16/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Laís |
| **Quem executa** | Estagiário(a) do atendimento `[A CONFIRMAR quem, manhã e tarde]`; advogado(a) da área quando houver escalonamento |
| **Gatilho** | Mensagem de cliente de assessoria no WhatsApp dos clientes da casa ou e-mail de atendimento |
| **Termina quando** | O cliente recebeu resposta, a demanda está registrada no ADVBOX e os arquivos estão no Drive |
| **Prazo máximo de primeira resposta** | **1 hora útil** (meta: 30 minutos) |

## Objetivo

Nenhum cliente de assessoria fica sem resposta. Hoje há mensagens que passam 1 a 2 dias sem retorno;
a partir deste POP, **nenhuma conversa termina o dia útil sem resposta**. O padrão da casa, nas
palavras da Laís: "responder os clientes no mesmo dia, dar retorno rápido, dar um suporte realmente
todo o dia a dia das empresas".

## Canais

| Canal | Endereço | Observação |
|---|---|---|
| WhatsApp dos clientes da casa | `{{numero_clientes_casa}}` `[A CONFIRMAR]` | Número exclusivo dos ~15 clientes de assessoria, conectado ao Infinitum |
| E-mail | `{{email_atendimento}}` `[A CONFIRMAR]` | Alguns clientes pedem demandas por e-mail. Responder **pelo mesmo canal** em que o cliente escreveu |

Se um cliente da casa escrever no número comercial ou no WhatsApp pessoal da Laís ou do Alex, quem
recebeu encaminha a conversa para o atendimento e o atendimento responde pelo número dos clientes da casa.

## Prazos (SLA)

| Etapa | Prazo |
|---|---|
| Confirmação de recebimento | Imediata pela automação. Sem automação: até 30 minutos úteis |
| Primeira resposta humana (com triagem ou resposta) | Até **1 hora útil** |
| Mensagem recebida fora do horário ou no fim de semana | Respondida até **9h do próximo dia útil** |
| Retorno com posição (resposta, encaminhamento ou prazo para resolver) | **No mesmo dia útil** |
| Urgência (ver item 4) | Advogado(a) avisado(a) por **ligação** em até 15 minutos |
| Ronda das conversas sem resposta | **11h30 e 17h30**, todo dia útil |

## Automação x pessoa

| A automação faz (Infinitum, Módulo 1) | A pessoa faz |
|---|---|
| Responde na hora com a confirmação de recebimento (MSG-01, modelo 1) | Lê, classifica e dá a primeira resposta humana |
| Identifica o cliente pelo número e mostra o histórico | Faz as perguntas do checklist da demanda |
| Responde "como está meu processo?": busca no ADVBOX, traduz o andamento e envia | Confere a resposta automática quando o andamento for decisão, sentença ou prazo |
| Salva no Drive os arquivos que o cliente manda e cria a tarefa no ADVBOX | Confere se o arquivo foi para a pasta certa |
| Avisa o atendimento das conversas paradas há mais de 1 hora | Responde as conversas paradas |

Enquanto a automação não estiver no ar, a pessoa faz todos os passos manualmente.

## Passo a passo

1. **Ler a mensagem inteira e identificar o cliente** (empresa e quem está falando). — *até 30 min*
2. **Responder confirmando o recebimento**, se a automação ainda não respondeu (MSG-01, modelo 1). — *até 30 min*
3. **Classificar a mensagem** em um dos tipos abaixo. — *junto com a primeira resposta*

   | Tipo | Exemplos | Quem resolve |
   |---|---|---|
   | **A. Andamento de processo** | "Como está meu processo?", "Saiu alguma coisa?" | Atendimento, consultando o ADVBOX. Se o andamento for decisão, sentença ou prazo, confirmar com o advogado(a) da área antes de explicar |
   | **B. Pedido administrativo** | Segunda via de boleto, nota fiscal, cópia de contrato, documento do processo | Atendimento (financeiro: Dra. Laís) |
   | **C. Demanda nova** | Devedor que não paga, funcionário que entrou na Justiça, cliente da oficina que recusou serviço, notificação recebida | Atendimento coleta as informações (passo 5) e abre a demanda para o advogado(a) da área |
   | **D. Urgência** | Ver passo 4 | Advogado(a) da área, imediatamente |
   | **E. Dúvida jurídica / consulta** | "Posso demitir?", "Como faço esse contrato?", "Preciso pagar isso?" | Advogado(a) da área. O atendimento **não** dá opinião jurídica: informa ao cliente quem vai responder e até quando |

4. **Urgência: escalar na hora.** É urgência quando o cliente fala de:
   - citação, intimação, notificação judicial ou de órgão público recebida;
   - audiência marcada;
   - fiscalização em andamento (Ministério do Trabalho, Receita, Sefaz, Procon, Vigilância, Bombeiros);
   - bloqueio de conta, penhora, protesto ou negativação;
   - acidente de trabalho, empregado demitido hoje, ameaça de greve ou paralisação;
   - prazo que vence hoje ou amanhã;
   - qualquer coisa que o cliente chame de urgente.

   Ação: **ligar** para o advogado(a) da área (ver tabela no README, item 4.7) e, se não atender em
   15 minutos, ligar para a Dra. Laís ou o Dr. Alex. Avisar o cliente: "Já passei para o(a) Dr(a).
   {{nome}}, que vai te retornar até {{horario}}". Registrar no ADVBOX como tarefa com prazo para hoje.

5. **Demanda nova: coletar as informações.** — *na mesma conversa, até 1 hora útil*
   - Usar a mensagem MSG-01, modelo 3, e o checklist do dia a dia correspondente:
     - cobrança, execução ou monitória: `CK-DIA-01`;
     - reclamação trabalhista recebida: `CK-DIA-02`;
     - cliente da oficina que recusou serviço: `CK-DIA-03`;
     - precisa de procuração, contrato ou carta de preposição: `CK-DIA-04`.
   - Se não existe checklist para o assunto, perguntar o básico:
     1. O que aconteceu, em poucas palavras?
     2. Quando aconteceu? Tem alguma data ou prazo envolvido?
     3. Quem é a outra parte (nome, CPF/CNPJ, se souber)?
     4. Recebeu algum documento (notificação, citação, e-mail, carta)? Mande foto ou PDF.
     5. Qual o valor envolvido, se houver?
     6. O que você espera que o escritório faça?
   - Não pedir tudo de uma vez se o cliente estiver no meio do expediente: priorizar documento e prazo.

6. **Registrar no ADVBOX e no Drive.** — *no mesmo dia*
   - Criar a tarefa `[DEMANDA NOVA] {{assunto}} - {{cliente}}` para o advogado(a) da área, com
     prazo de análise de **2 dias úteis** (urgência: hoje).
   - Criar a pasta da demanda no Drive (`CLIENTES/{{cliente}}/03_EXTRAJUDICIAL/AAAA-MM-DD - {{assunto}}`)
     ou, se já for processo, `02_JUDICIAL/{{nº do processo}} ...`. Salvar ali os arquivos e colar o link na tarefa.

7. **Dar o retorno com prazo ao cliente** (MSG-01, modelo 4): quem vai cuidar e até quando ele terá
   a resposta. Nunca prometer resultado. — *no mesmo dia útil*

8. **Acompanhar até o fim.** Se o advogado(a) não respondeu no prazo combinado, o atendimento cobra
   internamente e avisa o cliente antes de o prazo passar (MSG-01, modelo 5). — *no dia do prazo prometido*

9. **Encerrar a conversa** com a confirmação de que o cliente recebeu o que precisava e marcar a
   tarefa como concluída no ADVBOX.

## Quando escalar para advogado(a)

Sempre que houver: urgência (passo 4); dúvida jurídica (tipo E); decisão, sentença ou prazo no
andamento; cliente insatisfeito ou reclamando do escritório; pedido sobre honorários, valor ou
contrato; o mesmo assunto cobrado pela segunda vez; qualquer coisa que o atendimento não saiba
responder com segurança. **Na dúvida, escala.**

## O que vira tarefa no ADVBOX

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[DEMANDA NOVA] {{assunto}} - {{cliente}}` | Advogado(a) da área | 2 dias úteis (urgência: hoje) |
| `[RETORNO CLIENTE] {{assunto}} - {{cliente}}` | Atendimento | Data prometida ao cliente |
| `[URGENTE] {{assunto}} - {{cliente}}` | Advogado(a) da área | Hoje |

## Onde salva no Drive

- Demanda extrajudicial: `CLIENTES/{{cliente}}/03_EXTRAJUDICIAL/AAAA-MM-DD - {{assunto}}/`
- Processo: `CLIENTES/{{cliente}}/02_JUDICIAL/{{nº do processo}} - .../01_DOCUMENTOS_DO_CLIENTE/`

## Regras de conduta

- Tom cordial e profissional, sem gíria, sem emoji, sem áudio longo. Áudio do cliente: ouvir inteiro
  e responder por escrito.
- Não dar opinião jurídica, não prometer resultado, não informar valor de honorário sem autorização.
- Não discutir o caso de um cliente com outro.
- Toda conversa importante fica registrada: a decisão tomada vai para a tarefa no ADVBOX.

## Pendências `[A CONFIRMAR]`
- Número exclusivo dos clientes da casa e e-mail oficial de atendimento.
- Horário de atendimento ao cliente.
- Nome do(a) estagiário(a) responsável pelo atendimento em cada turno.
- Responsável pelo bancário.
