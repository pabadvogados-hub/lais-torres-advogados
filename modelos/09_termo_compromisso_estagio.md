# 09 — Termo de compromisso de estágio (tripartite)

> **Bloco de preenchimento e notas — não faz parte do documento.** O texto a ser gerado é apenas o que está entre
> os marcadores (comentários HTML) `INICIO_DOCUMENTO` e `FIM_DOCUMENTO`. Convenções: ver `README.md`.

## Antes de usar

1. **Tripartite é obrigatório.** O termo é assinado pelo estagiário, pela concedente (o escritório) e pela **instituição de ensino** (arts. 3º, II, e 16 da Lei nº 11.788/2008). Agente de integração não pode assinar como representante de nenhuma das partes (art. 16). Sem a assinatura da instituição, o estágio é irregular e o art. 15 da Lei manda reconhecer **vínculo de emprego** para todos os fins trabalhistas e previdenciários.
2. **Muitas faculdades exigem o modelo próprio.** Se a instituição tiver termo próprio, use o dela e anexe a este as cláusulas que faltarem (sigilo, LGPD, atos privativos). Este modelo serve quando a instituição aceita o da concedente.
3. **Credenciamento na OAB.** Para que o estágio conte como estágio profissional de advocacia e permita a inscrição do estudante como estagiário na OAB, o escritório precisa estar credenciado como unidade concedente no Conselho Seccional (art. 9º, § 1º, do EAOAB; Provimento CFOAB nº 217/2023, arts. 4º a 9º). Requisitos do Provimento 217/2023, art. 6º, entre outros: advogado supervisor com **mais de 5 anos de inscrição** e efetiva atividade (inciso V); demais supervisores com mais de 3 anos (inciso VI); certidão de regularidade; instalações, acervo e computador à disposição do estagiário no turno; relatório anual à Seccional até 31/12 (art. 15). Havendo conflito sobre a Seccional, prevalece o local onde o estágio é realizado (art. 2º, § 3º). `[CONFERIR]` data de inscrição da Dra. Laís e do Dr. Alex para o requisito de 5 anos, e se o credenciamento deve ser pedido à OAB/MA (estágio em Imperatriz) ou à OAB/GO.
4. **Jornada.** Ensino superior: até **6 horas diárias e 30 semanais** (art. 10, II), compatível com o horário das aulas; até 40 semanais só em períodos sem aula presencial e se o projeto pedagógico do curso previr (art. 10, § 1º); **redução de pelo menos metade** nos períodos de avaliação informados pela instituição (art. 10, § 2º). O horário 8h–18h dos advogados **não** pode ser aplicado a estagiário.
5. **Bolsa e auxílio-transporte** são **compulsórios** no estágio não obrigatório (art. 12). Benefícios como alimentação e saúde não geram vínculo (art. 12, § 1º).
6. **Recesso** de 30 dias a cada 12 meses, remunerado se houver bolsa, proporcional se o estágio durar menos de um ano (art. 13). **Duração máxima** de 2 anos na mesma concedente, salvo estagiário com deficiência (art. 11).
7. **Seguro contra acidentes pessoais** é obrigação da concedente, com apólice compatível com valores de mercado e indicada no termo (art. 9º, IV); no estágio obrigatório, a instituição pode assumi-lo (art. 9º, parágrafo único). Contratar **antes** do primeiro dia.
8. **Supervisor**: profissional do quadro da concedente com formação ou experiência na área, até 10 estagiários simultâneos (art. 9º, III). Relatório de atividades à instituição a cada 6 meses, no máximo, com vista ao estagiário (art. 9º, VII). Ao desligar: **termo de realização do estágio** com atividades, períodos e avaliação (art. 9º, V).
9. **Atos privativos.** Estagiário inscrito na OAB só subscreve atos de advocacia **em conjunto** com advogado; isoladamente, sob responsabilidade do advogado, apenas retirar e devolver autos, obter certidões e assinar petição de juntada de documentos; em atos extrajudiciais, pode comparecer isoladamente com autorização ou substabelecimento (art. 3º, § 2º, do EAOAB; art. 29 do Regulamento Geral). **Estudante aprovado no Exame de Ordem que ainda não colou grau continua estagiário** — só se inscreve como advogado após a graduação (art. 8º, II, do EAOAB).
10. É vedado cobrar do estagiário pela orientação ou pela inclusão no quadro (Provimento 217/2023, art. 16, § 3º).

## Campos

| Campo | O que é | De onde vem |
|---|---|---|
| `{{estagiario_nome}}`, `{{estagiario_nacionalidade}}`, `{{estagiario_estado_civil}}` | Qualificação | Documento de identidade / ficha de RH |
| `{{estagiario_rg}}`, `{{estagiario_cpf}}`, `{{estagiario_nascimento}}` | Documentos e data de nascimento (seguro) | Documento de identidade |
| `{{estagiario_endereco}}`, `{{estagiario_email}}`, `{{estagiario_telefone}}` | Contato | Comprovante de endereço / ficha de RH |
| `{{estagiario_curso}}`, `{{estagiario_periodo}}`, `{{estagiario_matricula}}` | Curso, período e matrícula | Declaração de matrícula atualizada |
| `{{estagiario_oab}}` | Inscrição como estagiário na OAB, se houver, ou "não inscrito(a)" | Carteira de estagiário |
| `{{ies_nome}}`, `{{ies_cnpj}}`, `{{ies_endereco}}` | Instituição de ensino | Declaração de matrícula / setor de estágios da IES |
| `{{ies_representante}}`, `{{ies_representante_cargo}}` | Quem assina pela IES | Setor de estágios da IES |
| `{{ies_orientador}}` | Professor orientador (art. 7º, III) | IES |
| `{{modalidade_estagio}}` | "obrigatório" ou "não obrigatório" | Projeto pedagógico do curso / IES |
| `{{escritorio_*}}`, `{{lais_*}}` | Concedente | `README.md` |
| `{{supervisor_nome}}`, `{{supervisor_oab}}` | Advogado(a) supervisor(a) | Decisão do escritório (ver nota 3) |
| `{{local_estagio}}` | Endereço onde o estágio é realizado | `README.md` (unidade de Imperatriz `[A CONFIRMAR]`) |
| `{{data_inicio}}`, `{{data_termino}}` | Vigência (máximo 2 anos somados na mesma concedente) | Decisão do escritório |
| `{{horario_estagio}}` | Ex.: "de segunda a sexta-feira, das 8h às 12h" — máximo 6h/dia e 30h/semana | Decisão do escritório + grade de aulas |
| `{{carga_semanal}}` | Total semanal em horas | Calculado |
| `{{valor_bolsa}}`, `{{valor_auxilio_transporte}}` | Valores mensais com extenso | Decisão do escritório |
| `{{dia_pagamento}}` | Dia do pagamento | Decisão do escritório |
| `{{seguradora}}`, `{{apolice_numero}}`, `{{capital_segurado}}` | Seguro contra acidentes pessoais | Apólice contratada |
| `{{atividades_estagio}}` | Plano de atividades (Anexo I) | Decisão do supervisor |
| `{{cidade_assinatura}}`, `{{data_assinatura}}` | — | Emissão |

---

<!-- INICIO_DOCUMENTO -->

# TERMO DE COMPROMISSO DE ESTÁGIO

Termo de compromisso celebrado com fundamento na Lei nº 11.788/2008, no art. 9º da Lei nº 8.906/1994 (Estatuto da Advocacia e da OAB) e nos arts. 27 a 31 do Regulamento Geral do Estatuto da Advocacia, entre as partes abaixo qualificadas.

**CONCEDENTE:** **{{escritorio_razao_social}}**, sociedade de advocacia inscrita no CNPJ sob o nº {{escritorio_cnpj}}, com sede em {{escritorio_endereco}}, neste ato representada por sua titular, **{{lais_nome}}**, advogada inscrita na {{lais_oab}}.

**ESTAGIÁRIO(A):** **{{estagiario_nome}}**, {{estagiario_nacionalidade}}, {{estagiario_estado_civil}}, nascido(a) em {{estagiario_nascimento}}, portador(a) do RG nº {{estagiario_rg}}, inscrito(a) no CPF sob o nº {{estagiario_cpf}}, residente em {{estagiario_endereco}}, endereço eletrônico {{estagiario_email}}, telefone {{estagiario_telefone}}, regularmente matriculado(a) no {{estagiario_periodo}} período do curso de {{estagiario_curso}}, matrícula nº {{estagiario_matricula}}, inscrição na OAB como estagiário(a): {{estagiario_oab}}.

**INSTITUIÇÃO DE ENSINO:** **{{ies_nome}}**, inscrita no CNPJ sob o nº {{ies_cnpj}}, com sede em {{ies_endereco}}, neste ato representada por {{ies_representante}}, {{ies_representante_cargo}}.

## CLÁUSULA PRIMEIRA — DO OBJETO

1.1. Este termo formaliza o estágio **{{modalidade_estagio}}** do(a) ESTAGIÁRIO(A) junto à CONCEDENTE, como ato educativo escolar supervisionado, destinado à preparação para o trabalho e à aprendizagem prática da advocacia, sem vínculo de emprego de qualquer natureza (art. 3º da Lei nº 11.788/2008).

1.2. As atividades serão compatíveis com o curso e constam do plano de atividades do Anexo I, que será atualizado por aditivos à medida que o desempenho do(a) ESTAGIÁRIO(A) for avaliado (art. 7º, parágrafo único, da Lei nº 11.788/2008).

## CLÁUSULA SEGUNDA — DA VIGÊNCIA

2.1. O estágio terá início em {{data_inicio}} e término em {{data_termino}}, podendo ser prorrogado por aditivo, respeitado o limite de 2 (dois) anos na mesma concedente, salvo se o(a) ESTAGIÁRIO(A) for pessoa com deficiência (art. 11 da Lei nº 11.788/2008).

2.2. O termo extingue-se automaticamente com a conclusão ou a interrupção do curso, o trancamento ou o cancelamento da matrícula, a colação de grau, ou o descumprimento das condições deste termo, e poderá ser rescindido por qualquer das partes, a qualquer tempo, mediante comunicação escrita com 5 (cinco) dias de antecedência.

## CLÁUSULA TERCEIRA — DA JORNADA

3.1. A jornada será de {{horario_estagio}}, totalizando {{carga_semanal}} horas semanais, não excedendo 6 (seis) horas diárias e 30 (trinta) horas semanais, e compatível com as atividades escolares (art. 10, II, da Lei nº 11.788/2008).

3.2. Nos períodos de avaliação informados pela INSTITUIÇÃO DE ENSINO, a jornada será reduzida pelo menos à metade (art. 10, § 2º, da Lei nº 11.788/2008), cabendo ao(à) ESTAGIÁRIO(A) apresentar o calendário de provas com antecedência.

3.3. É vedada a realização de atividades em horário que exceda o previsto nesta cláusula.

## CLÁUSULA QUARTA — DA BOLSA, DO AUXÍLIO-TRANSPORTE E DO RECESSO

4.1. A CONCEDENTE pagará ao(à) ESTAGIÁRIO(A) bolsa mensal de **{{valor_bolsa}}** e auxílio-transporte mensal de **{{valor_auxilio_transporte}}**, até o dia {{dia_pagamento}} do mês seguinte ao de referência, proporcionais aos dias de estágio no mês (art. 12 da Lei nº 11.788/2008).

4.2. A concessão de outros benefícios não caracteriza vínculo de emprego (art. 12, § 1º, da Lei nº 11.788/2008).

4.3. O(A) ESTAGIÁRIO(A) terá direito a recesso de 30 (trinta) dias a cada 12 (doze) meses de estágio, ou proporcional, se o estágio durar menos de um ano, gozado preferencialmente nas férias escolares, com manutenção da bolsa (art. 13 da Lei nº 11.788/2008).

4.4. O(A) ESTAGIÁRIO(A) poderá inscrever-se e contribuir como segurado(a) facultativo(a) do Regime Geral de Previdência Social (art. 12, § 2º, da Lei nº 11.788/2008).

## CLÁUSULA QUINTA — DO SEGURO

5.1. A CONCEDENTE contratou, em favor do(a) ESTAGIÁRIO(A), seguro contra acidentes pessoais junto a {{seguradora}}, apólice nº {{apolice_numero}}, com capital segurado de {{capital_segurado}}, vigente durante todo o período do estágio (art. 9º, IV, da Lei nº 11.788/2008).

## CLÁUSULA SEXTA — DAS OBRIGAÇÕES DA CONCEDENTE

6.1. São obrigações da CONCEDENTE:

a) ofertar instalações com condições adequadas ao aprendizado e observar a legislação de saúde e segurança no trabalho (arts. 9º, II, e 14 da Lei nº 11.788/2008);

b) designar como supervisor(a) **{{supervisor_nome}}**, advogado(a) inscrito(a) na {{supervisor_oab}}, para orientar e supervisionar o(a) ESTAGIÁRIO(A) (art. 9º, III, da Lei nº 11.788/2008);

c) enviar à INSTITUIÇÃO DE ENSINO, com periodicidade mínima de 6 (seis) meses, relatório de atividades, com vista obrigatória ao(à) ESTAGIÁRIO(A) (art. 9º, VII);

d) entregar ao(à) ESTAGIÁRIO(A), no desligamento, termo de realização do estágio, com indicação resumida das atividades, dos períodos e da avaliação de desempenho (art. 9º, V);

e) manter à disposição da fiscalização os documentos que comprovem a relação de estágio (art. 9º, VI);

f) assegurar que as atividades contemplem o estudo do Estatuto da Advocacia e do Código de Ética e Disciplina da OAB (art. 9º, § 1º, do Estatuto da Advocacia); e

g) não atribuir ao(à) ESTAGIÁRIO(A) atividades estranhas ao plano de atividades nem a prática isolada de atos privativos de advogado.

## CLÁUSULA SÉTIMA — DAS OBRIGAÇÕES DO(A) ESTAGIÁRIO(A)

7.1. São obrigações do(a) ESTAGIÁRIO(A):

a) cumprir o plano de atividades, a jornada e as orientações do(a) supervisor(a);

b) manter-se regularmente matriculado(a) e frequente, e comunicar imediatamente à CONCEDENTE a conclusão, o trancamento, o abandono ou a transferência do curso;

c) praticar atos de advocacia apenas em conjunto com advogado(a) e, isoladamente, somente os permitidos pelo art. 29 do Regulamento Geral do Estatuto da Advocacia, sob a responsabilidade do(a) advogado(a);

d) guardar **sigilo profissional** sobre todos os fatos, documentos e informações de clientes e da CONCEDENTE de que tomar conhecimento, durante e após o estágio, sujeitando-se às normas éticas da advocacia;

e) tratar dados pessoais de clientes e de terceiros somente para as atividades do estágio e nos sistemas indicados pela CONCEDENTE, observada a Lei nº 13.709/2018, vedados o armazenamento em dispositivos ou contas pessoais sem autorização e o compartilhamento com terceiros;

f) não atender clientes da CONCEDENTE em caráter particular nem receber deles qualquer valor; e

g) elaborar os relatórios de atividades solicitados pela CONCEDENTE ou pela INSTITUIÇÃO DE ENSINO.

## CLÁUSULA OITAVA — DAS OBRIGAÇÕES DA INSTITUIÇÃO DE ENSINO

8.1. Cabe à INSTITUIÇÃO DE ENSINO, nos termos do art. 7º da Lei nº 11.788/2008: avaliar as instalações da CONCEDENTE; indicar como professor(a) orientador(a) {{ies_orientador}}; exigir do(a) ESTAGIÁRIO(A) relatório de atividades em prazo não superior a 6 (seis) meses; zelar pelo cumprimento deste termo; e comunicar à CONCEDENTE, no início do período letivo, as datas das avaliações acadêmicas.

## CLÁUSULA NONA — DISPOSIÇÕES FINAIS

9.1. O descumprimento das obrigações deste termo ou da Lei nº 11.788/2008 pela CONCEDENTE caracteriza vínculo de emprego (art. 15 da Lei nº 11.788/2008); o descumprimento pelo(a) ESTAGIÁRIO(A) autoriza o seu desligamento imediato.

9.2. As partes admitem a assinatura deste termo por meio eletrônico, nos termos do art. 10, § 2º, da Medida Provisória nº 2.200-2/2001.

E, por estarem de acordo, as partes assinam este termo.

{{cidade_assinatura}}, {{data_assinatura}}.

&nbsp;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**CONCEDENTE** — {{escritorio_razao_social}}
p. {{lais_nome}} — {{lais_oab}}

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**ESTAGIÁRIO(A)** — {{estagiario_nome}}

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**INSTITUIÇÃO DE ENSINO** — {{ies_nome}}
p. {{ies_representante}} — {{ies_representante_cargo}}

&nbsp;

## ANEXO I — PLANO DE ATIVIDADES

**Local do estágio:** {{local_estagio}}
**Supervisor(a):** {{supervisor_nome}} — {{supervisor_oab}}
**Professor(a) orientador(a):** {{ies_orientador}}

**Atividades:** {{atividades_estagio}}

Sugestão de base (ajustar ao estagiário): pesquisa de legislação, doutrina e jurisprudência; elaboração de minutas de peças e documentos para revisão do(a) advogado(a); acompanhamento de prazos, publicações e intimações; acompanhamento de audiências e atendimentos ao lado do(a) advogado(a); obtenção de certidões e cópias; organização de documentos e cadastro de processos no sistema de gestão; estudo dirigido do Estatuto da Advocacia, do Regulamento Geral e do Código de Ética e Disciplina da OAB.

<!-- FIM_DOCUMENTO -->
