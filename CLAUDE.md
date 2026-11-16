# Escritório Laís Torres & Alex Brunno — contexto para o Claude

Fonte: kickoff de 12/11/2026 (transcrição completa em `docs/KICKOFF_12-11_transcricao.txt`) e
contrato Casal da IA (proposta 004/2026, assinado 09/11/2026, pago em 10x).

## Quem é quem

| Pessoa | Papel |
|---|---|
| **Dra. Laís Borges Torres Araújo Viana** — OAB/GO 62.226 | Sócia. Gestão, atendimento das assessorias, contratos (é contratualista). Clientes de Goiânia a conhecem pelo WhatsApp **DDD 62**. |
| **Dr. Alex Brunno** — OAB/MA (nº a confirmar) | Sócio. Peticionamento, correção de peças, **produto tributário** (transação, CAPAG, PGFN). Clientes do Maranhão o conhecem pelo WhatsApp **(99) 9114-2002**. Ex-procurador do município. |
| **Dra. Larissa** | Advogada integral. Responsável pelo **cível** e corrige peças cíveis. Quer atuar em **previdenciário** (plano: dar a ela o produto previdenciário, com percentual). |
| **Kathle** (grafia a confirmar) | 9º período, já aprovada na OAB. Responsável pelo **trabalhista**. |
| **Dra. Jaqueline** | Advogada (citada como opção para assumir o cível se a Larissa for para o previdenciário). |
| **Camila** | Estagiária (~40 anos, formada em Administração, experiência em gestão). Faz a **controladoria** (prazos, intimações, audiências). Dúvida recorrente: decisão — é caso de embargos, agravo ou apelação? |
| **Leilane** | Estagiária, filha dos empresários do grupo de 11 CNPJs (móveis e colchões, Tocantins). Quer o **agro** (plano futuro: endividamento do produtor rural). |
| Equipe | 2 advogadas integrais + 5 estagiários (2 de manhã, 3 à tarde) + 1 pessoa de meio período (R$ 1.000). **Ninguém tem contrato formal.** |

Pessoa jurídica que contratou o Casal da IA: **LAÍS TORRES SOCIEDADE INDIVIDUAL DE ADVOCACIA**,
CNPJ **58.232.242/0001-90**, Av. D nº 419, Qd. G11, Lt. 01, Ed. Comercial Marista, sala 401,
Goiânia/GO, CEP 74.150-040 — e-mail `laistorresadvogados@gmail.com`.
O escritório físico do dia a dia fica em **Imperatriz/MA** ("bico do papagaio": MA, PA e TO).
O Alex tem CNPJ próprio no Maranhão (dados a pedir).

## Como o escritório ganha dinheiro

- **Assessorias jurídicas mensais para empresas** (~15 clientes fixos) = o sustento fixo. Atendimento
  "sem limite": o cliente chama para tudo, no dia a dia da empresa. Áreas que mais aparecem:
  **tributário e trabalhista**, depois consumidor, contratos e bancário.
- Demanda judicial recorrente das assessorias: **execução, cobrança e monitória** (o cliente passa
  o devedor para judicializar). Defesa **trabalhista** (contestação, quesitos, impugnação a laudo,
  preparo de audiência).
- **Nicho forte: oficinas mecânicas e autopeças** (produto da Laís). Todas têm passivo tributário
  milionário que o escritório nunca monetizou.
- **Tributário com êxito sobre proveito econômico**: era 10% nos clientes antigos (mantido), **25%
  para clientes novos**. Poucos processos tributários deram a melhor margem do escritório.
- Produto novo do Alex: **transação tributária / CAPAG / PGFN** (vai ter tráfego pago). A caixa de
  ferramentas está em `tributario/` (produto, método, 21 teses, banco de leis com busca, motor de leads,
  raio-x por CNPJ, avaliador da CAPAG). Os agentes `avaliador-capag` e `peca-tributaria` e a skill
  `triagem-tributaria` ficam em `.claude/`. Os POPs são os `pops/POP-TRIB-01` a `06`.

## Ferramentas que já têm

- **ADVBOX** (contratado no início do ano). Erro a corrigir: os documentos dos clientes estão sendo
  guardados **só dentro do ADVBOX** — se perderem o ADVBOX, perdem tudo.
- **Infinitum** — não pagam (acesso pela mentoria Éuro). Vai receber os 2 WhatsApps.
- **Asaas** (app) e **Nubank** (app). Nenhum controle financeiro, nenhum relatório.
- **Google Workspace** e um Google Drive do escritório "todo bagunçado".
- Site improvisado (feito no Claude), sem conteúdo. Instagram parado. Já tiveram agência de
  tráfego (Jonk) e cortaram.
- **Não têm**: software de atendimento, POPs, checklists, modelos (nem de procuração), base de
  teses, controle de demanda extrajudicial (estava "na cabeça da Laís"), agenda integrada,
  backup do WhatsApp (perderam todas as conversas em maio/2026).

## Regras de trabalho neste projeto

- **Menor custo de manutenção possível**: usar o que eles já têm (ADVBOX, Infinitum, Asaas, Drive,
  Claude). Não propor ferramenta paga nova sem dizer o custo. A única compra combinada é uma
  **VPS de ~R$ 50/mês** (banco de dados + backup semanal das conversas).
- **Nada de dado inventado.** O que não veio da reunião fica marcado `[A CONFIRMAR]` e entra na
  lista de pendências — nunca preencher OAB, CPF, CNPJ, chave Pix ou valor por suposição.
- Peça e documento jurídico: linguagem formal, sem emoji. Contrato e procuração com campos
  `{{chave}}` para preenchimento automático.
- Os clientes de assessoria e os leads são atendidos **separados**: lead/comercial em um número,
  cliente da casa em outro (decisão de qual número fica com quem está pendente — ver pendências).
- Leads de fora do Maranhão: usar CNPJ, endereço e número de **Goiás (62)** nas campanhas
  (o mercado tem resistência a escritório do Maranhão); público local usa o número do Alex (99).
