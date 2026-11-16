# Projeto de Implantação — Escritório Laís Torres & Alex Brunno

**Casal da IA** · Proposta 004/2026 · Kickoff em 12/11/2026 · Implantação a partir de 16/11/2026

---

## 1. O diagnóstico (o que vocês nos contaram)

| Área | Como está hoje | O que dói |
|---|---|---|
| **Atendimento** | Dois WhatsApps (62 da Laís, 99 do Alex), sem software e sem POP | Mensagem de cliente fica 1 a 2 dias sem resposta; cliente da casa e lead novo misturados |
| **Financeiro** | App do Asaas e do Nubank, sem controle | Ninguém sabe quanto entra e quanto sai; NF depende do contador no dia 20 (atrasa recebimento de quem só paga com nota); integração Asaas–ADVBOX disparou 12 avisos para um cliente |
| **Pagamentos** | Pix um a um, caçando a chave no WhatsApp | Trabalho manual todo mês |
| **Equipe / RH** | 5 estagiários + 2 advogadas integrais, **ninguém com contrato** | Risco trabalhista e documentos espalhados no celular |
| **Documentos** | Tudo salvo **dentro do ADVBOX**; Drive bagunçado; arquivos em Downloads | Se o ADVBOX sair, o escritório perde o acervo |
| **Modelos e checklists** | Não existem (nem procuração) | Cada contratação e cada demanda recomeça do zero |
| **Controladoria** | Camila faz; dúvida recorrente entre embargos, agravo ou apelação | Antes da Camila, prazos se perderam |
| **Peças** | Sem modelos nem base de teses; Laís e Alex corrigem tudo | Sócios presos na correção em vez de vender e atender os melhores clientes |
| **WhatsApp** | Sem backup | Todas as conversas perdidas em maio/2026 |
| **Comercial** | ~1 cliente novo por semana; site sem conteúdo; Instagram parado | Produto tributário do Alex vai gerar fluxo que hoje não teria estrutura para absorver |

**A dor nº 1 escolhida por vocês: atendimento.** É por ele que a implantação começa.

---

## 2. Como vai funcionar: o escritório virtual

Trabalhamos com o que vocês já têm, com o **menor custo de manutenção possível**:

```
 WhatsApp 62 e 99 ──► INFINITUM (atendimento + fluxos) ──► ADVBOX (processos, tarefas, prazos)
                              │                                   ▲
                              ▼                                   │
                        GOOGLE DRIVE  ◄──── agentes Claude ───────┘
                    (acervo do escritório)   (RH, financeiro, controladoria, peças)
                              ▲                    │
                              │                    ▼
                         VPS ~R$ 50/mês ◄──── ASAAS (cobrança, NF, Pix da equipe)
                     (banco + backup semanal)
```

Custo novo: **só a VPS (~R$ 50/mês)**. Infinitum, ADVBOX, Asaas e Google vocês já têm.

---

## 3. Os módulos, na ordem de implantação

### Módulo 1 — Atendimento (hoje, 16/11)
- Os **dois WhatsApps no Infinitum**, com separação:
  - **número comercial**: leads e clientes novos. Para campanhas fora do Maranhão, identidade de
    Goiás (DDD 62, CNPJ e endereço de Goiânia); público local fica com o 99;
  - **número de clientes da casa**: os ~15 clientes fixos de assessoria, com aviso de mudança de número.
- **POP de atendimento** com prazo máximo de primeira resposta e triagem da demanda nova.
- **Modelos de mensagem** (primeira resposta, pedido de informações, cobrança de documentos, boas-vindas).
- Fluxo "como está meu processo?": o cliente pergunta, a automação busca no ADVBOX, traduz o andamento e responde.

### Módulo 2 — Financeiro (Asaas)
- **Régua de cobrança própria**: 10, 5 e 3 dias antes e no dia do vencimento, com o link de
  pagamento, **pelo WhatsApp do escritório**. Os avisos pagos do Asaas ficam desligados, o que
  resolve o problema dos 12 disparos.
- **Os 12 boletos da assessoria registrados**, aparecendo no DDA do cliente.
- **Nota fiscal pelo Asaas**, sem depender do dia 20 do contador: emitida **antes do pagamento**
  para quem só paga com nota e **após o pagamento** para os demais.
- **Relatório diário**: o que entrou, o que saiu, quem está atrasado, margem e custo da equipe.
- **Pagamento da equipe e das despesas fixas por Pix agendado**: vocês só aprovam o token de manhã.
- Contrato avulso: vocês passam os dados e a forma de pagamento; o agente cadastra, gera a cobrança e envia o link.

### Módulo 3 — RH e contratos da equipe
- **Contratos para todos**: termo de compromisso de estágio (tripartite, com a faculdade) e
  contrato de associação para as advogadas, **com averbação na OAB**.
- **Agente de RH**: checklist por tipo de vínculo, pasta do colaborador no Drive, contrato gerado,
  assinatura coletada e comprovantes de pagamento arquivados na pasta de cada um.

### Módulo 4 — Drive organizado e documentos fora do ADVBOX
- Estrutura única do Drive: **Escritório (POPs, modelos) · RH · Financeiro · Clientes**.
  Dentro de cada cliente: **Contrato e documentos · Judicial (por processo) · Extrajudicial (por
  demanda) · Diagnóstico da assessoria**. Isso resolve o cliente de assessoria que traz demanda nova toda semana.
- **Documento que chega pelo WhatsApp vai sozinho** para a pasta certa do cliente e **vira tarefa
  com prazo no ADVBOX**.
- Migração do acervo que hoje está só dentro do ADVBOX.

### Módulo 5 — Modelos, POPs e checklists
- **Modelos do escritório**: procuração (PF e PJ), substabelecimento, carta de preposição,
  contratos de honorários (assessoria mensal; tributário com êxito; causa avulsa), notificação de
  cobrança, termo de recusa da oficina e contrato da oficina com o consumidor.
- **Checklists de diagnóstico de entrada da assessoria**: trabalhista preventivo, tributário,
  cobrança/inadimplência, consumidor e oficina. O que o cliente não tem vira **pacote de implantação vendável**.
- **Checklists do dia a dia**: cobrança/execução/monitória, reclamação trabalhista, termo de recusa.
- **POPs**: atendimento, onboarding do cliente, custas, controladoria, contestação trabalhista,
  execução/cobrança/monitória, correção de peças, contratação e pagamento da equipe.

### Módulo 6 — Controladoria e peças
- **Agente de controladoria**: lê as intimações pelas OABs, classifica (mero andamento, embargos,
  agravo, apelação, recurso ordinário), **marca o prazo e cria a tarefa no ADVBOX**. Quando cabe
  peça, já traz a **minuta pronta**. A dúvida recorrente da Camila passa a ter resposta com critério.
- **Primeira correção pela IA**: a peça chega ao advogado da área (Larissa no cível, Kathle no
  trabalhista, Alex no tributário) já revisada; ele só faz a revisão final antes do protocolo.
  Até a Kathle se formar e se inscrever na OAB, a peça trabalhista sai assinada por um advogado inscrito.
- **DNA e base de teses do próprio escritório**, montados a partir das peças reais de vocês.

### Módulo 7 — VPS e backup
- VPS (~R$ 50/mês) com o banco de dados e **backup semanal automático** das conversas e arquivos.

### Módulo 8 — Tributário do Alex e captação
- **CAPAG automática**: com a procuração do cliente no Regularize/e-CAC, o extrato vai para o
  Claude, que devolve a categoria (A a D) e o desconto possível na transação. Várias CAPAGs de uma vez.
- POPs comerciais e operacionais do produto (primeiro contato → diagnóstico → proposta → adesão → acompanhamento).
- **Checklist tributário para os clientes atuais** (oficinas e autopeças com passivo alto): receita que hoje está parada dentro da casa.
- **Bônus do contrato**: estruturação e gestão do tráfego pago por 90 dias, e treinamento para
  **extrair e enriquecer listas** de prospecção sem depender de agência.

### Módulo 9 — Assistente pessoal dos sócios
- Um assistente para a Laís e outro para o Alex: agenda, compromissos e lembretes integrados.

**Incluso no contrato também**: treinamento da equipe, acompanhamento por 90 dias e portal de suporte do Casal da IA.

---

## 4. Cronograma

| Quando | O quê |
|---|---|
| **16/11 (hoje)** | Módulo 1: WhatsApps no Infinitum, POP e mensagens de atendimento |
| **17 a 19/11** | Módulo 2 (financeiro) e Módulo 5 (modelos e checklists) |
| **19 a 21/11** | Módulos 3 (RH), 4 (Drive) e 7 (VPS) |
| **até 24/11** | Módulo 6 (controladoria e peças); entrega da implantação no prazo do contrato |
| **a partir de 24/11** | Módulos 8 e 9, treinamento da equipe e acompanhamento de 90 dias |

(Prazo contratual: 7 dias úteis a partir do briefing de 12/11, o que dá **24/11**, já que 20/11 é feriado nacional.)

---

## 5. O que precisamos de vocês

**Para hoje:**
- [ ] Acesso de administrador ao **Infinitum** do escritório
- [ ] Os dois celulares à mão para ler o QR Code (62 e 99)
- [ ] Decisão: **qual número fica comercial e qual fica para os clientes da casa?** (sugestão: o
      62 comercial, por causa das campanhas nacionais, e um número só para os ~15 clientes de assessoria)

**Até 18/11:**
- [ ] **ADVBOX**: token da API (Configurações > API)
- [ ] **Asaas**: chave de API (Integrações > Chave de API) e a lista de clientes de assessoria com
      valor, dia de vencimento e regra de nota (antes ou depois do pagamento)
- [ ] **Equipe**: nome, função, vínculo, valor, dia de pagamento e chave Pix de cada pessoa
- [ ] **Google Drive**: acesso à conta do escritório
- [ ] **OABs** para monitorar intimações: Laís (GO 62.226), Alex (MA nº ?), Larissa e Kathle
- [ ] **CNPJ e endereço do escritório de Imperatriz** (Alex)
- [ ] **Papel timbrado** do escritório (se houver)
- [ ] **5 a 10 peças reais por área** (cível, trabalhista, tributário, execução/monitória), que viram o DNA e a base de teses
- [ ] Ferramenta de **assinatura eletrônica** que usam (se não tiverem, indicamos a opção de menor custo)
- [ ] **Contratar a VPS** (passamos o passo a passo)
