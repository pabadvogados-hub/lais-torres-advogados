# 05 — Contrato de honorários — assessoria jurídica mensal para empresa

> **Bloco de preenchimento — não faz parte do documento.** O texto a ser gerado é apenas o que está entre
> os marcadores (comentários HTML) `INICIO_DOCUMENTO` e `FIM_DOCUMENTO`. Convenções: ver `README.md`.

| Campo | O que é | De onde vem |
|---|---|---|
| `{{cliente_razao_social}}`, `{{cliente_cnpj}}`, `{{cliente_endereco}}`, `{{cliente_email}}` | Dados da empresa contratante | Comprovante do CNPJ / contrato social |
| `{{representante_nome}}`, `{{representante_cargo}}`, `{{representante_cpf}}` | Representante legal | Contrato social |
| `{{cliente_interlocutor}}` | Nome, cargo e contato de quem pode demandar o escritório em nome da empresa | Reunião de início da assessoria |
| `{{escritorio_*}}`, `{{lais_*}}` | Dados fixos do escritório | `README.md` |
| `{{areas_assessoria}}` | Áreas cobertas. Padrão: "direito empresarial e societário consultivo, contratos, direito do trabalho consultivo, direito do consumidor e direito bancário consultivo" | Proposta comercial |
| `{{valor_mensal}}` | Mensalidade com extenso | Proposta comercial — observar o mínimo da tabela da OAB do local do serviço (art. 48, § 6º, CED) |
| `{{dia_vencimento}}` | Dia do vencimento mensal | Proposta comercial |
| `{{data_inicio}}` | Início da vigência / primeira mensalidade | Proposta comercial |
| `{{canais_oficiais}}` | Ex.: "WhatsApp (xx) xxxxx-xxxx e e-mail xxxx@xxxx" | `README.md` — número de cliente da casa `[A CONFIRMAR]` |
| `{{horario_atendimento}}` | Ex.: "dias úteis, das 8h às 18h (horário de Brasília)" | Decisão do escritório |
| `{{prazo_primeiro_retorno}}` | Prazo para o primeiro retorno. Sugestão: "1 (um) dia útil" | Decisão do escritório |
| `{{comarca_atendimento}}` | Comarca sem cobrança de deslocamento | Proposta comercial |
| `{{dias_suspensao}}` | Dias de atraso que autorizam suspender o atendimento. Sugestão: 15 (quinze) | Decisão do escritório |
| `{{meses_permanencia}}` / `{{multa_resilicao}}` | Período mínimo e multa por resilição antecipada (bloco opcional `{{#clausula_permanencia}}`) | Decisão do escritório — ver "Pontos para a Dra. Laís decidir" |
| `{{desconto_servicos_extras}}` | Desconto sobre a tabela do escritório para serviços fora do escopo (bloco opcional `{{#clausula_desconto}}`) | Proposta comercial |
| `{{horas_demanda_extraordinaria}}` | Bloco opcional `{{#clausula_demanda_extraordinaria}}` | Decisão do escritório |
| `{{foro_comarca}}` | Foro de eleição | `README.md` (decisão pendente: Goiânia/GO ou Imperatriz/MA) |
| `{{cidade_assinatura}}`, `{{data_assinatura}}` | Local e data | Gerado na emissão |
| `{{testemunha1_*}}`, `{{testemunha2_*}}` | Nome e CPF | Equipe do escritório |

**Notas de uso**

1. Este contrato cobre o **consultivo contínuo** ("atendimento sem limite de consultas"). Processos judiciais e serviços tributários são contratados à parte (modelos 06 e 07), mesmo para clientes de assessoria.
2. O quadro do Anexo I é o que evita discussão futura sobre escopo: revisar com o cliente na assinatura.
3. Base: arts. 22 a 24 do EAOAB; arts. 48 a 54 do Código de Ética e Disciplina (CED); Lei nº 10.192/2001, art. 2º, § 1º (periodicidade anual mínima do reajuste); Lei nº 13.709/2018 (LGPD).
4. Não emitir duplicata nem levar fatura a protesto (art. 52 do CED). Boleto bancário ou Pix como meio de pagamento é permitido.
5. Se for preciso cobrar judicialmente o cliente, o advogado deve antes renunciar aos mandatos recebidos desse cliente (art. 54 do CED).

---

<!-- INICIO_DOCUMENTO -->

# CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE ASSESSORIA JURÍDICA EMPRESARIAL

Pelo presente instrumento particular, as partes abaixo qualificadas celebram contrato de prestação de serviços advocatícios de assessoria jurídica, que se regerá pelas cláusulas seguintes e pela Lei nº 8.906/1994 (Estatuto da Advocacia e da OAB), pelo Regulamento Geral e pelo Código de Ética e Disciplina da OAB.

**CONTRATANTE:** **{{cliente_razao_social}}**, pessoa jurídica de direito privado, inscrita no CNPJ sob o nº {{cliente_cnpj}}, com sede em {{cliente_endereco}}, endereço eletrônico {{cliente_email}}, neste ato representada por seu(sua) {{representante_cargo}}, **{{representante_nome}}**, inscrito(a) no CPF sob o nº {{representante_cpf}}.

**CONTRATADA:** **{{escritorio_razao_social}}**, sociedade de advocacia inscrita no CNPJ sob o nº {{escritorio_cnpj}} e registrada na OAB/GO sob o nº {{escritorio_registro_oab}}, com sede em {{escritorio_endereco}}, endereço eletrônico {{escritorio_email}}, neste ato representada por sua titular, **{{lais_nome}}**, advogada inscrita na {{lais_oab}}.

## CLÁUSULA PRIMEIRA — DO OBJETO

1.1. O objeto deste contrato é a prestação, pela CONTRATADA, de serviços contínuos de assessoria e consultoria jurídica preventiva à CONTRATANTE, nas áreas de {{areas_assessoria}}.

1.2. Compreendem-se no objeto, sem limite quantitativo de demandas, os seguintes serviços:

a) atendimento a consultas e esclarecimento de dúvidas jurídicas relacionadas à atividade empresarial da CONTRATANTE, por escrito, por telefone, por videoconferência ou presencialmente;

b) análise, elaboração e revisão de contratos, aditivos, distratos, termos, declarações, notificações e demais instrumentos relativos às operações ordinárias da CONTRATANTE;

c) elaboração de notificações e contranotificações extrajudiciais, e condução de negociações extrajudiciais, inclusive de cobrança, antes do ajuizamento de qualquer medida;

d) orientação preventiva na gestão de pessoal, incluindo admissões, advertências, suspensões, desligamentos, jornada, benefícios e procedimentos internos, e análise pontual de documentos trabalhistas;

e) orientação no relacionamento com consumidores, incluindo respostas a reclamações diretas e em plataformas privadas de atendimento;

f) emissão de pareceres e orientações escritas sobre questões jurídicas do cotidiano da empresa, ressalvado o disposto no item 1.4;

g) participação em reuniões com a administração da CONTRATANTE, com terceiros ou com a sua contabilidade, na comarca de {{comarca_atendimento}} ou por videoconferência; e

h) triagem preliminar de questões tributárias, judiciais ou de outra natureza não compreendidas no objeto, com indicação da providência cabível e, se for o caso, apresentação de proposta específica.

1.3. A ausência de limite quantitativo de consultas não implica dedicação exclusiva nem disponibilidade fora do horário de atendimento previsto na Cláusula Terceira, ressalvadas as urgências nela tratadas.

{{#clausula_demanda_extraordinaria}}1.4. Demandas consultivas que, por sua extensão ou complexidade, exijam mais de {{horas_demanda_extraordinaria}} horas de trabalho técnico, ou que consistam em pareceres formais com pesquisa doutrinária e jurisprudencial aprofundada, serão previamente informadas à CONTRATANTE, que poderá optar entre a sua execução mediante proposta específica ou a sua execução dentro da mensalidade em cronograma compatível com as demais demandas.{{/clausula_demanda_extraordinaria}}

## CLÁUSULA SEGUNDA — DOS SERVIÇOS NÃO INCLUÍDOS

2.1. Não estão compreendidos no objeto deste contrato, e dependerão de contratação própria, por escrito, com honorários específicos:

a) o ajuizamento, a defesa e o acompanhamento de processos judiciais e arbitrais de qualquer natureza, incluindo reclamações trabalhistas, execuções, ações monitórias e de cobrança, cumprimento de sentença, medidas cautelares e recursos, bem como a preparação e o comparecimento a audiências judiciais;

b) os serviços de natureza tributária, incluindo diagnóstico de passivo fiscal, transação tributária, parcelamentos, revisão da capacidade de pagamento, defesas e recursos administrativos e judiciais em matéria tributária, recuperação de créditos e planejamento tributário;

c) a defesa e o acompanhamento de processos e procedimentos administrativos contenciosos, tais como autos de infração, processos perante órgãos de proteção e defesa do consumidor, órgãos de fiscalização do trabalho, agências reguladoras e tribunais administrativos;

d) projetos de implantação ou reestruturação documental, assim entendida a elaboração ou revisão do conjunto de documentos da empresa (entre outros: regulamento interno, código de conduta, modelos de contrato de trabalho e aditivos, termos de entrega de equipamento de proteção individual, políticas internas e documentos de adequação à proteção de dados);

e) operações societárias, reorganizações, auditorias jurídicas (*due diligence*), recuperação judicial ou extrajudicial e falência;

f) demandas de interesse pessoal de sócios, administradores, empregados ou familiares destes, ainda que relacionadas à empresa; e

g) deslocamentos para fora da comarca de {{comarca_atendimento}}.

2.2. Os serviços do item 2.1 serão executados somente após a aprovação, pela CONTRATANTE, de proposta escrita da CONTRATADA com escopo, honorários e forma de pagamento.

{{#clausula_desconto}}2.3. Enquanto vigente este contrato, a CONTRATANTE terá desconto de {{desconto_servicos_extras}} sobre os valores de referência praticados pela CONTRATADA para os serviços do item 2.1, salvo quanto aos honorários de êxito.{{/clausula_desconto}}

## CLÁUSULA TERCEIRA — DA FORMA DE ATENDIMENTO

3.1. As demandas serão encaminhadas pela CONTRATANTE exclusivamente pelos canais oficiais {{canais_oficiais}}, por {{cliente_interlocutor}} ou por outra pessoa que a CONTRATANTE indicar por escrito.

3.2. O atendimento ocorrerá em {{horario_atendimento}}. A CONTRATADA dará o primeiro retorno a cada demanda em até {{prazo_primeiro_retorno}}, informando a providência e o prazo estimado de conclusão, que variará conforme a complexidade.

3.3. Demandas urgentes, assim entendidas as que envolvam prazo legal ou judicial iminente, risco de perecimento de direito ou situação de fiscalização em curso, serão sinalizadas como tais pela CONTRATANTE e tratadas com prioridade, inclusive fora do horário de atendimento, na medida do possível.

3.4. A CONTRATANTE encaminhará à CONTRATADA, **no mesmo dia do recebimento**, toda citação, intimação, notificação judicial ou extrajudicial, auto de infração ou comunicação de órgão público que receber. A CONTRATADA não responde por prazos perdidos em razão de documento que lhe tenha sido entregue tardiamente ou não tenha sido entregue.

3.5. Mensagens enviadas a canais pessoais dos advogados ou colaboradores, fora dos canais oficiais, somente serão consideradas recebidas quando registradas pela CONTRATADA em seus canais oficiais.

## CLÁUSULA QUARTA — DAS OBRIGAÇÕES DA CONTRATADA

4.1. A CONTRATADA obriga-se a prestar os serviços com zelo, diligência, independência técnica e observância das normas legais e éticas da advocacia, por meio de advogados regularmente inscritos na OAB, auxiliados por estagiários e colaboradores sob sua supervisão.

4.2. A obrigação da CONTRATADA é de meio, e não de resultado. A orientação jurídica é prestada com base nas informações e documentos fornecidos pela CONTRATANTE e na legislação e jurisprudência vigentes à época, não havendo garantia de êxito em negociações, procedimentos ou litígios.

4.3. A CONTRATADA manterá registro das demandas recebidas e concluídas e, mediante solicitação, fornecerá à CONTRATANTE relatório das demandas atendidas no período.

## CLÁUSULA QUINTA — DAS OBRIGAÇÕES DA CONTRATANTE

5.1. São obrigações da CONTRATANTE:

a) fornecer informações verdadeiras, completas e tempestivas, e os documentos necessários a cada demanda, respondendo pelas consequências de omissões ou inexatidões;

b) encaminhar as demandas com antecedência compatível com a sua complexidade e com os prazos envolvidos;

c) não adotar, sem consulta prévia, medidas que dependam de orientação jurídica já solicitada à CONTRATADA;

d) pagar pontualmente os honorários e reembolsar as despesas na forma deste contrato; e

e) assegurar que o compartilhamento, com a CONTRATADA, de dados pessoais de seus empregados, clientes, fornecedores e demais titulares tenha base legal e seja informado aos titulares, nos termos da Cláusula Décima.

## CLÁUSULA SEXTA — DOS HONORÁRIOS E DAS DESPESAS

6.1. Pelos serviços objeto deste contrato, a CONTRATANTE pagará à CONTRATADA honorários mensais de **{{valor_mensal}}**, com vencimento no dia {{dia_vencimento}} de cada mês, sendo a primeira mensalidade devida em {{data_inicio}}.

6.2. Os honorários mensais remuneram a disponibilidade técnica da CONTRATADA e são devidos integralmente em cada mês de vigência, independentemente do número de demandas encaminhadas.

6.3. O pagamento será feito por boleto bancário ou Pix emitido pela CONTRATADA, que emitirá a correspondente nota fiscal de serviços. Não será emitida duplicata nem levada a protesto fatura relativa a honorários, nos termos do art. 52 do Código de Ética e Disciplina da OAB.

6.4. O atraso no pagamento sujeitará o valor devido a multa de 2% (dois por cento), juros de mora de 1% (um por cento) ao mês, *pro rata die*, e atualização monetária pela variação do IPCA/IBGE.

6.5. Atraso superior a {{dias_suspensao}} dias autoriza a CONTRATADA a suspender o atendimento das novas demandas, mediante comunicação prévia por escrito, ressalvadas as providências indispensáveis para evitar o perecimento de direito da CONTRATANTE em demandas já em curso.

6.6. Custas, emolumentos, taxas, despesas de cartório, postagem, cópias autenticadas, honorários de peritos, assistentes técnicos, contadores e correspondentes, bem como despesas de deslocamento, hospedagem e alimentação fora da comarca de {{comarca_atendimento}}, correrão por conta da CONTRATANTE, mediante aprovação prévia, e não estão incluídos nos honorários (art. 48, § 3º, do Código de Ética e Disciplina da OAB).

6.7. Os honorários de sucumbência fixados em qualquer processo em que a CONTRATADA atue pertencem a ela, nos termos dos arts. 22 e 23 da Lei nº 8.906/1994, e não compensam nem reduzem os honorários contratuais.

## CLÁUSULA SÉTIMA — DO REAJUSTE

7.1. Os honorários mensais serão reajustados anualmente, a cada aniversário da data de início deste contrato, pela variação acumulada do IPCA/IBGE nos 12 (doze) meses anteriores, observado o art. 2º, § 1º, da Lei nº 10.192/2001. Em caso de extinção do índice, será adotado o que oficialmente o substituir.

7.2. Independentemente do reajuste anual, as partes poderão repactuar o valor dos honorários, por aditivo escrito, se houver alteração relevante no porte da CONTRATANTE, no número de estabelecimentos ou de empregados, ou nas áreas de atuação cobertas.

## CLÁUSULA OITAVA — DA VIGÊNCIA E DA EXTINÇÃO

8.1. Este contrato vigorará por 12 (doze) meses a partir de {{data_inicio}}, renovando-se automaticamente por períodos iguais e sucessivos, salvo manifestação em contrário de qualquer das partes, por escrito, com antecedência mínima de 30 (trinta) dias do término do período em curso.

8.2. Qualquer das partes poderá resilir este contrato a qualquer tempo, mediante aviso prévio por escrito de 30 (trinta) dias, durante os quais os serviços continuarão a ser prestados e os honorários continuarão devidos.

{{#clausula_permanencia}}8.3. Se a resilição por iniciativa da CONTRATANTE ocorrer antes de completados {{meses_permanencia}} meses de vigência, será devida, além do aviso prévio, multa compensatória de {{multa_resilicao}}, reduzida proporcionalmente ao período já cumprido.{{/clausula_permanencia}}

8.4. O contrato poderá ser resolvido de imediato, mediante comunicação escrita, em caso de inadimplemento superior a 60 (sessenta) dias ou de descumprimento grave das obrigações contratuais, inclusive quebra da confiança indispensável à relação entre advogado e cliente.

8.5. A extinção deste contrato não afeta os contratos específicos firmados nos termos da Cláusula Segunda, que seguem regidos por seus próprios termos, nem os honorários vencidos até a data da extinção.

8.6. Extinto o contrato, a CONTRATADA concluirá as demandas consultivas cujo prazo vença nos 10 (dez) dias seguintes, salvo orientação diversa da CONTRATANTE, e devolverá ou disponibilizará os documentos originais que estejam em seu poder.

## CLÁUSULA NONA — DO SIGILO E DA PROPRIEDADE INTELECTUAL

9.1. A CONTRATADA guardará sigilo sobre todos os fatos e informações de que tomar conhecimento em razão deste contrato, nos termos dos arts. 7º, II, e 34, VII, da Lei nº 8.906/1994 e dos arts. 35 a 38 do Código de Ética e Disciplina da OAB, estendendo esse dever a seus advogados, estagiários e colaboradores. O sigilo subsiste após a extinção do contrato.

9.2. A CONTRATANTE manterá em sigilo as orientações, pareceres, estratégias e propostas recebidas da CONTRATADA, que se destinam ao seu uso interno.

9.3. Os documentos elaborados pela CONTRATADA para a CONTRATANTE podem ser por esta livremente utilizados em suas atividades. Os modelos, métodos e materiais de trabalho da CONTRATADA permanecem de sua titularidade, vedada a sua reprodução para comercialização ou cessão a terceiros.

## CLÁUSULA DÉCIMA — DA PROTEÇÃO DE DADOS PESSOAIS

10.1. As partes cumprirão a Lei nº 13.709/2018 (Lei Geral de Proteção de Dados Pessoais — LGPD) em relação aos dados pessoais tratados em razão deste contrato.

10.2. A CONTRATADA tratará os dados pessoais recebidos para a execução deste contrato, para o exercício regular de direitos em processos judiciais, administrativos e arbitrais e para o cumprimento de obrigações legais e regulatórias (art. 7º, II, V e VI, e art. 11, II, "a" e "d", da LGPD), e não os utilizará para finalidade diversa.

10.3. A CONTRATANTE declara que os dados pessoais que compartilhar com a CONTRATADA, inclusive dados de empregados e dados pessoais sensíveis, como atestados e informações de saúde ocupacional, foram coletados de forma lícita e que o seu compartilhamento para fins de assessoria jurídica é compatível com as finalidades informadas aos titulares.

10.4. A CONTRATADA adotará medidas técnicas e administrativas aptas a proteger os dados pessoais (art. 46 da LGPD), poderá utilizar serviços de armazenamento em nuvem e sistemas de gestão de processos de terceiros que ofereçam garantias adequadas de segurança, e comunicará à CONTRATANTE, em prazo razoável, incidente de segurança que possa acarretar risco ou dano relevante aos titulares cujos dados tenham sido por ela compartilhados.

10.5. Extinto o contrato, os dados pessoais serão conservados pelo prazo necessário ao cumprimento de obrigações legais e ao exercício regular de direitos, inclusive enquanto não prescritas as pretensões relacionadas aos serviços prestados (art. 16, I, da LGPD), e eliminados em seguida.

## CLÁUSULA DÉCIMA PRIMEIRA — DAS COMUNICAÇÕES E DA ASSINATURA ELETRÔNICA

11.1. As comunicações entre as partes serão feitas pelos canais oficiais e pelos endereços eletrônicos indicados neste contrato, cabendo a cada parte informar à outra, por escrito, qualquer alteração.

11.2. As partes reconhecem a validade da assinatura deste instrumento por meio eletrônico, nos termos do art. 10, § 2º, da Medida Provisória nº 2.200-2/2001, considerando-se firmado na data da última assinatura, e reconhecem-no como título executivo extrajudicial, nos termos do art. 24 da Lei nº 8.906/1994 e do art. 784, § 4º, do Código de Processo Civil.

## CLÁUSULA DÉCIMA SEGUNDA — DISPOSIÇÕES GERAIS

12.1. A tolerância de qualquer das partes quanto ao descumprimento de obrigação pela outra não importa novação nem renúncia ao direito de exigi-la.

12.2. Nenhuma das partes poderá ceder os direitos e obrigações deste contrato sem a anuência escrita da outra, ressalvada a cessão, pela CONTRATADA, dos créditos de honorários.

12.3. Se surgir conflito de interesses entre a CONTRATANTE e outro cliente da CONTRATADA em determinada demanda, a CONTRATADA poderá declinar do atendimento dessa demanda, sem prejuízo da continuidade deste contrato, observados os arts. 19 a 22 do Código de Ética e Disciplina da OAB.

12.4. Integra este contrato o Anexo I — Quadro de Escopo.

## CLÁUSULA DÉCIMA TERCEIRA — DO FORO

13.1. Fica eleito o foro da comarca de {{foro_comarca}} para dirimir as controvérsias oriundas deste contrato, com renúncia a qualquer outro, por mais privilegiado que seja.

E, por estarem justas e contratadas, as partes assinam este instrumento, juntamente com duas testemunhas.

{{cidade_assinatura}}, {{data_assinatura}}.

&nbsp;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**CONTRATANTE** — {{cliente_razao_social}}
p. {{representante_nome}} — CPF nº {{representante_cpf}}

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**CONTRATADA** — {{escritorio_razao_social}}
p. {{lais_nome}} — {{lais_oab}}

**Testemunhas:**

1. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Nome: {{testemunha1_nome}} — CPF: {{testemunha1_cpf}}
2. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Nome: {{testemunha2_nome}} — CPF: {{testemunha2_cpf}}

&nbsp;

## ANEXO I — QUADRO DE ESCOPO

| Situação | Incluída na mensalidade? | Como é tratada |
|---|---|---|
| Dúvida jurídica do dia a dia da empresa | Sim | Atendimento pelos canais oficiais |
| Elaboração e revisão de contratos e termos das operações ordinárias | Sim | Prazo conforme complexidade |
| Notificação extrajudicial e negociação de cobrança antes do processo | Sim | — |
| Orientação em admissão, advertência, suspensão e desligamento | Sim | — |
| Resposta a reclamação direta de consumidor | Sim | — |
| Reunião com a administração ou com a contabilidade | Sim | Na comarca de {{comarca_atendimento}} ou por vídeo |
| Ação de execução, monitória ou cobrança contra devedor | Não | Contrato de causa (modelo 07) |
| Defesa em reclamação trabalhista e audiência | Não | Contrato de causa (modelo 07) |
| Passivo tributário, transação, parcelamento, CAPAG, defesa fiscal | Não | Contrato tributário (modelo 06) |
| Defesa em auto de infração, processo no PROCON ou em órgão público | Não | Proposta específica |
| Pacote de documentos preventivos (regulamento interno, termos de EPI, modelos trabalhistas, LGPD) | Não | Proposta específica |
| Assunto pessoal de sócio, administrador ou empregado | Não | Proposta específica |

<!-- FIM_DOCUMENTO -->
