# Modelos jurídicos padrão — Laís Torres Sociedade Individual de Advocacia

Versão 1 — 16/11/2026. **Minutas para validação da Dra. Laís antes do primeiro uso.** Sem papel timbrado (o
timbrado do escritório ainda não chegou; quando chegar, o texto é aplicado sobre ele sem alteração).

## 1. Índice e quando usar

| Nº | Arquivo | Documento | Quando usar | Quem assina |
|---|---|---|---|---|
| 01 | `01_procuracao_pf.md` | Procuração *ad judicia et extra* — pessoa física | Todo cliente pessoa física, em qualquer área | Cliente |
| 02 | `02_procuracao_pj.md` | Procuração *ad judicia et extra* — pessoa jurídica | Toda empresa cliente (assessoria, tributário, causa). Ligar os blocos de poderes tributários e/ou trabalhistas conforme o caso | Representante legal conforme contrato social |
| 03 | `03_substabelecimento.md` | Substabelecimento com reserva (versão A) e sem reserva (versão B) | A: correspondente, audiência por outro advogado, inclusão de associada. B: saída do escritório do processo, com ciência prévia do cliente | Advogado(a) do escritório |
| 04 | `04_carta_preposicao_trabalhista.md` | Carta de preposição — Justiça do Trabalho | Toda audiência trabalhista de cliente empregador | Representante legal da empresa + preposto |
| 05 | `05_contrato_assessoria_mensal.md` | Contrato de assessoria jurídica mensal | Fechamento de assessoria para empresa ("atendimento sem limite" do consultivo) | Empresa + escritório + 2 testemunhas |
| 06 | `06_contrato_tributario_exito.md` | Contrato tributário com êxito sobre o proveito econômico | Transação, CAPAG, PGFN, defesa fiscal, recuperação de créditos — inclusive para clientes de assessoria e oficinas | Empresa + escritório + 2 testemunhas |
| 07 | `07_contrato_causa_avulsa.md` | Contrato de causa avulsa (fixo + êxito opcional) | Execução, monitória, cobrança, defesa trabalhista e qualquer processo pontual | Cliente + escritório + 2 testemunhas |
| 08 | `08_contrato_associacao_advogado.md` | Contrato de associação de advogada | Dra. Larissa, Dra. Jaqueline e futuras associadas. **Ler a nota de risco do arquivo antes** | Escritório + associada + 2 testemunhas; averbar na OAB |
| 09 | `09_termo_compromisso_estagio.md` | Termo de compromisso de estágio (tripartite) | Os 5 estagiários atuais e os futuros | Escritório + estagiário + instituição de ensino |
| 10 | `10_oficina_termo_recusa_servico.md` | Termo de recusa de serviço e ciência de riscos | Entregue às oficinas clientes, para uso no balcão quando o consumidor recusa serviço/peça | Consumidor + oficina |
| 11 | `11_oficina_contrato_servicos_consumidor.md` | Condições gerais de serviço e termo de garantia (oficina x consumidor) | Entregue às oficinas clientes, impresso no verso ou anexo à ordem de serviço | Consumidor + oficina |
| 12 | `12_notificacao_extrajudicial_cobranca.md` | Notificação extrajudicial de cobrança | Antes da execução/monitória; cobrança dos devedores dos clientes de assessoria | Advogado(a) do escritório |

**Combinações usuais**

- Nova assessoria: 02 + 05 (e checklist de diagnóstico inicial).
- Tributário: 02 com `{{#poderes_tributarios}}` + 06 + procuração eletrônica no e-CAC.
- Cobrança de devedor do cliente de assessoria: 12 (dentro da mensalidade) → se não pagar, 07 (contrato da ação) + 02.
- Reclamação trabalhista contra cliente: 07 + 02 com `{{#poderes_trabalhistas}}` + 04 a cada audiência.
- Contratação de equipe: 08 (advogadas) / 09 (estagiários).
- Produto oficina: 10 + 11 personalizados por oficina, no pacote de documentos preventivos de consumidor.

## 2. Convenções de preenchimento

- `{{chave}}` — campo simples. Valores em dinheiro e percentuais **sempre com número e extenso** ("R$ 1.500,00 (mil e quinhentos reais)"; "25 (vinte e cinco)" — os textos já trazem "por cento").
- `{{#chave}} ... {{/chave}}` — bloco opcional: entra no documento se a chave estiver ligada/preenchida; sai inteiro se não estiver. Ao retirar um bloco numerado, **revisar a numeração** dos itens seguintes (não é refeita automaticamente).
- O documento a gerar é só o trecho entre os marcadores (comentários HTML) `INICIO_DOCUMENTO` e `FIM_DOCUMENTO` (no modelo 03, `_A` ou `_B`). O que está acima é instrução interna.
- `[A CONFIRMAR]` — dado do escritório que não temos; **nunca preencher por suposição**.
- `[CONFERIR]` — ponto jurídico que não consegui confirmar em fonte oficial; está listado na seção 6.
- Cada modelo traz, no topo, a tabela de campos com **a origem** de cada dado (ficha do cliente, contrato social, ADVBOX, proposta comercial, ordem de serviço da oficina etc.).

## 3. Campos fixos do escritório

| Campo | Valor | Situação |
|---|---|---|
| `{{escritorio_razao_social}}` | LAÍS TORRES SOCIEDADE INDIVIDUAL DE ADVOCACIA | Confirmado (contrato Casal da IA) |
| `{{escritorio_cnpj}}` | 58.232.242/0001-90 | Confirmado |
| `{{escritorio_registro_oab}}` | Número de registro da sociedade na OAB/GO | `[A CONFIRMAR]` |
| `{{escritorio_endereco}}` | Av. D, nº 419, Qd. G11, Lt. 01, Ed. Comercial Marista, sala 401, Goiânia/GO, CEP 74.150-040 | Confirmado (sede registrada) |
| `{{escritorio_email}}` | laistorresadvogados@gmail.com | Confirmado |
| `{{lais_nome}}` | Laís Borges Torres Araújo Viana | Confirmado |
| `{{lais_oab}}` | OAB/GO sob o nº 62.226 | Confirmado |
| `{{lais_oab_suplementar}}` | Inscrição suplementar na OAB/MA, se houver | `[A CONFIRMAR]` |
| `{{alex_nome}}` | Alex Brunno — nome completo | `[A CONFIRMAR]` |
| `{{alex_oab}}` | OAB/MA nº | `[A CONFIRMAR]` |
| `{{alex_vinculo}}` | Forma de vínculo do Dr. Alex com a sociedade (ver seção 4, item 1) | `[A CONFIRMAR]` |
| Endereço de Imperatriz/MA | Unidade onde o escritório funciona de fato | `[A CONFIRMAR]` (e ver seção 4, item 2) |
| `{{canais_oficiais}}` | Número de WhatsApp de clientes da casa + e-mail de atendimento | `[A CONFIRMAR]` (decisão de qual número fica com quem está pendente) |
| `{{foro_comarca}}` | Goiânia/GO ou Imperatriz/MA | Decisão pendente (seção 5) |

## 4. Achados que pedem providência (além dos modelos)

1. **Vínculo do Dr. Alex com a sociedade.** A sociedade é **individual** (unipessoal): por definição, só a Dra. Laís é titular, e o Dr. Alex não pode ser sócio dela. As procurações devem indicar a sociedade de que cada advogado faz parte (art. 15, § 3º, do EAOAB), e os atos privativos da sociedade unipessoal são praticados pela titular ou por advogados a ela **vinculados como associados ou empregados** (Provimento CFOAB nº 170/2016, art. 5º, parágrafo único). Hoje o Dr. Alex atua sem vínculo formal. Caminhos: (a) **transformar a sociedade em pluripessoal**, com os dois como sócios — a solução mais limpa, inclusive para dividir resultados; (b) **contrato de associação** do Dr. Alex com a sociedade (modelo 08 adaptado); ou (c) se ele tiver sociedade unipessoal própria no Maranhão, **associação entre sociedades** (Provimento 170/2016, art. 7º, II), averbada nas duas Seccionais (§ 3º). Até a definição, `{{alex_vinculo}}` fica `[A CONFIRMAR]`.
2. **Sede em Goiânia, operação em Imperatriz.** O art. 15, § 5º, do EAOAB exige averbação de filial e arquivamento no Conselho Seccional onde se instalar, com inscrição suplementar do titular; o art. 10, § 2º, exige inscrição suplementar de quem atua habitualmente (mais de cinco causas por ano) em outra Seccional. Confirmar a situação da Dra. Laís na OAB/MA e a da filial.
3. **Advogadas "integrais" com horário 8h–18h e salário fixo, sem contrato.** Risco alto de vínculo de emprego. Detalhes, consequências e as duas saídas (associação de verdade ou CLT) na nota de risco do modelo 08.
4. **Estagiários sem termo de compromisso.** Estágio sem termo tripartite é irregular, e o art. 15 da Lei nº 11.788/2008 manda reconhecer vínculo de emprego. Regularizar os cinco **antes** de qualquer outra coisa da área de RH, com seguro contratado. Jornada máxima de 6h/30h — o horário dos advogados não se aplica.
5. **Kathle (9º período, aprovada no Exame de Ordem).** Continua estagiária até colar grau (art. 8º, II, do EAOAB). Pode ser responsável interna pelo trabalhista, mas peças e atos judiciais devem ser subscritos em conjunto com advogado (art. 29 do Regulamento Geral).
6. **Credenciamento do estágio na OAB** (Provimento CFOAB nº 217/2023): necessário para o estágio valer como estágio profissional de advocacia. Exige supervisor com mais de 5 anos de inscrição (art. 6º, V) — ver `[CONFERIR]`.
7. **Tabela de honorários.** O art. 48, § 6º, do Código de Ética manda observar o mínimo da tabela do Conselho Seccional **onde o serviço é realizado** — conferir as tabelas vigentes da OAB/MA e da OAB/GO antes de fixar mensalidades e valores de causa.

## 5. Pontos para a Dra. Laís decidir

Escolhas que fiz na redação e que precisam do seu aval:

**Gerais**

1. **Foro de eleição** (`{{foro_comarca}}`): deixei em campo. Goiânia é a sede registrada; Imperatriz é onde estão os clientes e a operação. Sugestão: foro do domicílio do cliente da região (Imperatriz para o MA) e Goiânia para clientes captados por Goiás. Nos contratos da oficina com consumidor, o foro é sempre o do consumidor (art. 101, I, do CDC).
2. **Assinatura eletrônica.** Os contratos admitem assinatura eletrônica (MP 2.200-2/2001, art. 10, § 2º) e mantêm 2 testemunhas para garantir a força de título executivo. Para **procurações**, ver `[CONFERIR]` nº 5.
3. **Procurações amplas** (todos os foros e órgãos), com campo opcional de finalidade específica. Alternativa: procuração restrita por caso.
4. **Multa de 2%, juros de 1% ao mês e IPCA** em todos os contratos de honorários — padrão de mercado; ajustar se preferir.

**Assessoria mensal (05)**

5. **Fora da mensalidade:** processos judiciais, todo o tributário (fica só a triagem), contencioso administrativo (PROCON, autos de infração), pacote de documentos preventivos e assuntos pessoais de sócios. Confirme especialmente o **PROCON** e as **audiências trabalhistas**, que alguns escritórios incluem.
6. **Mensalidade devida mesmo sem demanda no mês** (item 6.2) e **primeiro retorno em 1 dia útil** (sugestão).
7. **Cláusulas opcionais desligadas por padrão:** permanência mínima com multa (8.3), desconto para serviços extras (2.3) e "demanda extraordinária" por horas (1.4). A última reduz o "sem limite" — use só se fizer sentido comercial.
8. **Suspensão do atendimento após 15 dias de atraso** (sugestão), preservadas as medidas urgentes.

**Tributário (06)**

9. **Percentual:** 25% para clientes novos (campo); clientes antigos a 10% continuam nos contratos antigos ou migram — decisão comercial.
10. **Prejuízo fiscal, base negativa da CSLL e precatórios** usados para amortizar a dívida: sugeri que **100%** do valor amortizado conte como proveito (o cliente converte um crédito que, em regra, só usaria contra lucro futuro). É o ponto mais discutível com o cliente; alternativa: 50% ou excluir.
11. **Momento do êxito:** na **formalização** da transação, não na quitação — com cláusula expressa de que a rescisão por culpa do cliente não afasta os honorários. Parcelamento do êxito em até 12 vezes, **nunca em mais parcelas que a própria transação**.
12. **Parcelamento sem desconto, certidão e liberação de penhora não geram êxito** (3.3, "c"). Consequência: se o contrato não tiver pró-labore fixo, esses serviços saem de graça. Recomendo **sempre** cobrar um fixo, ainda que baixo.
13. **Cláusula de proteção do diagnóstico** (3.5, 12 meses): se o cliente usar o diagnóstico do escritório para aderir sozinho ou com outro advogado, paga o êxito. É defensável, mas pode ser contestada; mantenha se o diagnóstico for entregue por escrito.
14. **Revogação pelo cliente:** êxito integral sobre medidas já protocoladas. Um juiz pode reduzir ao proporcional; a alternativa conservadora é prever êxito proporcional desde já, como no modelo 07.
15. **Compensação não homologada:** previ devolução/abatimento dos honorários correspondentes, sem acréscimos.

**Causa avulsa (07)**

16. **Base do êxito no polo passivo** ("economia" sobre o pedido inicial): pedidos inflados geram honorário alto e atrito. Alternativas: êxito fixo por resultado (improcedência = R$ X) ou base no valor provável apurado na contestação.
17. **Fixo não restituível após o primeiro ato** e êxito **proporcional** em caso de revogação.

**Associação (08)**

18. **Remuneração:** participação nos honorários das causas sob responsabilidade da associada + sucumbência + indicação de clientes. A **antecipação mínima mensal** está como bloco opcional — ela aproxima a associação de salário e aumenta o risco trabalhista.
19. **Presença física** combinada por escrito, sem horário fixo e sem controle — é a mudança prática mais importante. Se o escritório precisa do 8h–18h, a resposta é CLT.
20. **Pós-contrato:** participação por 12 meses nas causas em que atuou (proporcional) e não aliciamento ativo de clientes por 12 meses, respeitada a escolha do cliente.

**Estágio (09)**

21. Valores de **bolsa, auxílio-transporte e capital segurado**; supervisor(a) indicado(a); aviso de 5 dias para rescisão.

**Oficinas (10 e 11)**

22. **Retenção do veículo até o pagamento** (item 7.2 do modelo 11): ver `[CONFERIR]` nº 6. Se preferir zero risco, retirar o item.
23. **Diagnóstico pago quando o orçamento é recusado** e **estadia diária** após o prazo de retirada: só valem se informados antes e em valor razoável — definir os valores com cada oficina.
24. **Garantia contratual** sugerida no campo (90 dias ou 5.000 km para mão de obra, após a legal) — definir com cada oficina.

**Notificação (12)**

25. Prazo de **10 dias** para pagamento; pagamento **direto ao credor** por padrão; protesto e negativação como blocos opcionais.

## 6. Pontos `[CONFERIR]`

| Nº | Ponto | Onde aparece | Como conferir |
|---|---|---|---|
| 1 | Se os Provimentos CFOAB nº 169/2015 e 170/2016 continuam vigentes (o Conselho Federal trabalha num provimento consolidado de sociedades; não localizei publicação) e qual o procedimento atual de averbação na OAB/GO (o Prov. 170/2016 fala em 3 vias, um contrato por associado) | 08 | Comissão de Sociedades de Advogados da OAB/GO; portal oab.org.br > Leis e Normas |
| 2 | Se o contrato de associação deve ser averbado também na OAB/MA, por causa da atuação em Imperatriz (filial) | 08 | OAB/MA |
| 3 | Piso salarial do advogado empregado em GO e no MA (se a opção for CLT) | 08 | Sindicato/Seccional; art. 19 do EAOAB |
| 4 | Data de inscrição da Dra. Laís e do Dr. Alex (supervisor de estágio precisa de mais de 5 anos — Prov. 217/2023, art. 6º, V) e qual Seccional credencia (local do estágio prevalece — art. 2º, § 3º) | 09 | Certidões da OAB |
| 5 | Aceitação, pelo TJMA, TJGO, TJTO, TRF1 e TRTs da 16ª e 18ª Regiões, de procuração com assinatura eletrônica de plataforma privada (sem ICP-Brasil) | 01, 02 | Normas e jurisprudência locais; na dúvida, assinatura gov.br ou ICP-Brasil |
| 6 | Retenção do veículo pela oficina até o pagamento (art. 476 do CC) — posição do TJMA, TJGO e TJTO e dos PROCONs locais | 11 | Pesquisa de jurisprudência |
| 7 | Lei estadual ou municipal (MA, PA, TO, GO) que obrigue a devolução das peças substituídas | 11 | Pesquisa legislativa local |
| 8 | Entendimento atual do STJ sobre a contagem do prazo da garantia legal após o término da garantia contratual | 11 | Pesquisa de jurisprudência (o modelo foi redigido para não depender disso) |
| 9 | Tratamento previdenciário e tributário dos repasses a associadas pessoa física x associada com sociedade própria | 08 | Contabilidade |
| 10 | Valores mínimos das tabelas de honorários da OAB/MA e da OAB/GO | 05, 06, 07 | Sites das Seccionais |

## 7. Dispositivos conferidos em fonte oficial em 16/11/2026

- **Lei nº 8.906/1994 (EAOAB)**, texto compilado do Planalto: arts. 5º, 9º, 10, § 2º, 15, 16, § 4º, 17, 17-A, 17-B, 18, 20 (jornada de 8h/40h e adicional de 100%, redação da Lei nº 14.365/2022), 22, § 4º, e 24.
- **Regulamento Geral do EAOAB** (PDF do CFOAB): arts. 27 a 31, 37 a 40.
- **Código de Ética e Disciplina da OAB** (Resolução CFOAB nº 02/2015): arts. 14 a 26, 35 a 38, 48 a 54.
- **Provimentos CFOAB** nº 169/2015, 170/2016 (site do CFOAB) e 217/2023 (estágio — publicação no Diário Eletrônico da OAB de 27/11/2023).
- **Lei nº 11.788/2008**: arts. 2º, 3º, 7º, 9º a 17.
- **Lei nº 8.078/1990 (CDC)**: arts. 6º, III, 14, § 3º, 20, 21, 24, 25, 26, 39, VI, 40, 42, 43, § 2º, 50, 51, I e XII, 52, § 1º, 54, §§ 3º e 4º.
- **Lei nº 13.988/2020**: arts. 3º, § 3º, 4º e § 4º, 11 (incisos I a V, §§ 1º-A, 2º e 3º — limites vigentes de 65%/120 meses e 70%/145 meses).
- Citados de memória profissional, sem conferência nesta data, por serem dispositivos estáveis: CPC (arts. 75, 105, 111, 112, 287, 700, 784), CLT (arts. 2º, 3º, 9º, 843, 844), Código Civil (arts. 202, 206, 389, 394, 397, 406 — redação da Lei nº 14.905/2024 —, 476, 654, 661, 667), LGPD (arts. 7º, 11, 16, 46), Lei nº 10.192/2001 (art. 2º, § 1º), Lei nº 6.015/1973 (art. 160), Lei nº 9.492/1997, MP nº 2.200-2/2001 (art. 10, § 2º), CDC (arts. 51, IV, e 101, I). Vale uma leitura rápida da Dra. Laís na revisão.
