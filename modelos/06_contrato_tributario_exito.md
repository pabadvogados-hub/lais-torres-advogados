# 06 — Contrato de honorários — tributário, com êxito sobre o proveito econômico

> **Bloco de preenchimento — não faz parte do documento.** O texto a ser gerado é apenas o que está entre
> os marcadores (comentários HTML) `INICIO_DOCUMENTO` e `FIM_DOCUMENTO`. Convenções: ver `README.md`.

| Campo | O que é | De onde vem |
|---|---|---|
| `{{cliente_razao_social}}`, `{{cliente_cnpj}}`, `{{cliente_endereco}}`, `{{cliente_email}}` | Contratante (pessoa jurídica) | Comprovante do CNPJ / contrato social |
| `{{representante_nome}}`, `{{representante_cargo}}`, `{{representante_cpf}}` | Representante legal | Contrato social |
| `{{escritorio_*}}`, `{{lais_*}}`, `{{alex_*}}` | Dados fixos do escritório | `README.md` |
| `{{esferas_abrangidas}}` | Ex.: "União (Receita Federal e PGFN), Estado de [UF] e Município de [cidade]" | Diagnóstico / proposta |
| `{{percentual_exito}}` | Número + extenso, sem o símbolo %. **Padrão para cliente novo: 25 (vinte e cinco).** Clientes antigos: 10 (dez) | Proposta comercial |
| Bloco `{{#honorarios_fixos}}` | Pró-labore fixo (opcional) | Proposta comercial |
| `{{valor_fixo}}`, `{{parcelas_fixo}}`, `{{valor_parcela_fixo}}` | Valor total, número de parcelas e valor de cada parcela (com extenso) | Proposta comercial |
| `{{parcelas_exito}}` | Número máximo de parcelas do êxito. Sugestão: 12 (doze) | Proposta comercial |
| Bloco `{{#desconto_avista}}` / `{{percentual_desconto_avista}}` | Desconto para pagamento do êxito à vista (opcional) | Proposta comercial |
| `{{percentual_creditos_pf}}` | Percentual do valor amortizado com prejuízo fiscal/base negativa/precatório que integra o proveito. Sugestão: 100 (cem) | Decisão do escritório — ver README |
| `{{meses_vigencia}}` | Vigência mínima. Sugestão: 24 (vinte e quatro) | Proposta comercial |
| `{{meses_protecao}}` | Prazo da cláusula de proteção do diagnóstico (item 3.5). Sugestão: 12 (doze) | Decisão do escritório |
| `{{foro_comarca}}`, `{{cidade_assinatura}}`, `{{data_assinatura}}` | Foro, local e data | `README.md` / emissão |
| `{{testemunha1_*}}`, `{{testemunha2_*}}` | Testemunhas | Equipe |
| `{{svc_diagnostico}}`, `{{svc_capag}}`, `{{svc_transacao}}`, `{{svc_parcelamento}}`, `{{svc_defesa_adm}}`, `{{svc_execucao_fiscal}}`, `{{svc_judicial}}`, `{{svc_recuperacao}}` | Anexo I: "X" para contratado, espaço em branco para não contratado | Proposta comercial |
| `{{svc_judicial_descricao}}` | Descrição da medida judicial (tese e tributo) ou "não se aplica" | Proposta comercial / parecer do Dr. Alex |

**Notas de uso**

1. Para contratante pessoa física, trocar a qualificação pela do modelo 01; o restante se aplica (o art. 11, § 3º, da Lei nº 13.988/2020 dá à pessoa natural, à ME e à EPP limites maiores de desconto e prazo — 70% e 145 meses, contra 65% e 120 meses da regra geral do § 2º, conferido no texto vigente em 16/11/2026).
2. O ponto mais sensível do contrato é a **definição de proveito econômico** (Cláusula Terceira). Ela foi escrita para fechar as discussões típicas: "o desconto era do edital, qualquer um conseguia"; "a dívida ainda não foi extinta, só parcelada"; "o desconto foi sobre juros que eu nem ia pagar"; "usei meu próprio prejuízo fiscal". Ver "Pontos para a Dra. Laís decidir" no README.
3. Limite ético: honorários de êxito em pecúnia e, somados à sucumbência, não superiores à vantagem do cliente (art. 50 do CED). Com 25% sobre a redução, o limite está atendido em qualquer cenário realista.
4. Antes de qualquer adesão, colher **aprovação escrita** do cliente (item 5.3) — protege o escritório e o cliente.
5. Procuração: modelo 02 com o bloco `{{#poderes_tributarios}}` + procuração eletrônica no e-CAC.

---

<!-- INICIO_DOCUMENTO -->

# CONTRATO DE PRESTAÇÃO DE SERVIÇOS ADVOCATÍCIOS EM MATÉRIA TRIBUTÁRIA

**Honorários de êxito sobre o proveito econômico**

Pelo presente instrumento particular, as partes abaixo qualificadas celebram contrato de prestação de serviços advocatícios, que se regerá pelas cláusulas seguintes e pela Lei nº 8.906/1994 (Estatuto da Advocacia e da OAB), pelo Regulamento Geral e pelo Código de Ética e Disciplina da OAB.

**CONTRATANTE:** **{{cliente_razao_social}}**, pessoa jurídica de direito privado, inscrita no CNPJ sob o nº {{cliente_cnpj}}, com sede em {{cliente_endereco}}, endereço eletrônico {{cliente_email}}, neste ato representada por seu(sua) {{representante_cargo}}, **{{representante_nome}}**, inscrito(a) no CPF sob o nº {{representante_cpf}}.

**CONTRATADA:** **{{escritorio_razao_social}}**, sociedade de advocacia inscrita no CNPJ sob o nº {{escritorio_cnpj}} e registrada na OAB/GO sob o nº {{escritorio_registro_oab}}, com sede em {{escritorio_endereco}}, endereço eletrônico {{escritorio_email}}, neste ato representada por sua titular, **{{lais_nome}}**, advogada inscrita na {{lais_oab}}.

## CLÁUSULA PRIMEIRA — DO OBJETO

1.1. O objeto deste contrato é a prestação, pela CONTRATADA, dos serviços advocatícios em matéria tributária assinalados no Anexo I, relativos aos **débitos abrangidos**.

1.2. Consideram-se **débitos abrangidos** todos os créditos tributários e não tributários exigidos ou exigíveis da CONTRATANTE, de sua matriz e de suas filiais, por {{esferas_abrangidas}}, constituídos ou não, inscritos ou não em dívida ativa, ajuizados ou não, cujos fatos geradores tenham ocorrido até a data de assinatura deste contrato, ainda que identificados posteriormente.

1.3. Os serviços serão prestados com base nos documentos e nas informações fornecidos pela CONTRATANTE e nos extratos obtidos nos sistemas dos órgãos fazendários, cuja veracidade e completude a CONTRATANTE garante quanto ao que lhe compete.

1.4. Nas medidas judiciais compreendidas no Anexo I, o patrocínio abrange todas as instâncias, até o trânsito em julgado, e o cumprimento de sentença.

1.5. Não estão compreendidos no objeto, e correrão por conta da CONTRATANTE, mediante aprovação prévia: custas, depósitos judiciais, garantias, emolumentos, honorários de peritos e assistentes técnicos e honorários de profissional contábil, inclusive para elaboração de laudo de viabilidade ou de demonstrações exigidas em transação individual (art. 48, § 3º, do Código de Ética e Disciplina da OAB).

1.6. Serviços não assinalados no Anexo I dependerão de aditivo ou de contrato próprio.

## CLÁUSULA SEGUNDA — DOS HONORÁRIOS

{{#honorarios_fixos}}2.1. **Honorários fixos.** A CONTRATANTE pagará à CONTRATADA honorários fixos de **{{valor_fixo}}**, em {{parcelas_fixo}} parcelas mensais e sucessivas de {{valor_parcela_fixo}}, vencendo a primeira na data de assinatura deste contrato e as demais no mesmo dia dos meses subsequentes. Os honorários fixos remuneram o trabalho técnico independentemente de resultado, não são restituíveis e não se compensam com os honorários de êxito.{{/honorarios_fixos}}

2.2. **Honorários de êxito.** A CONTRATANTE pagará à CONTRATADA honorários de êxito correspondentes a **{{percentual_exito}} por cento** do **proveito econômico** obtido, definido e apurado na forma da Cláusula Terceira, pagos na forma da Cláusula Quarta.

2.3. Os honorários de sucumbência fixados em qualquer processo pertencem à CONTRATADA, nos termos dos arts. 22 e 23 da Lei nº 8.906/1994, e não reduzem nem compensam os honorários contratuais, observado o limite do art. 50 do Código de Ética e Disciplina da OAB.

2.4. Os pagamentos serão feitos por boleto bancário ou Pix emitido pela CONTRATADA, que emitirá a correspondente nota fiscal de serviços. Não será emitida duplicata nem levada a protesto fatura relativa a honorários (art. 52 do Código de Ética e Disciplina da OAB).

## CLÁUSULA TERCEIRA — DO PROVEITO ECONÔMICO

3.1. **Conceito.** Considera-se proveito econômico, para os fins deste contrato, toda redução, exclusão, cancelamento, extinção, compensação, restituição ou ressarcimento de valores exigidos ou exigíveis da CONTRATANTE, ou a ela devidos pela Fazenda Pública, que decorra dos serviços prestados pela CONTRATADA em relação aos débitos abrangidos, apurado conforme os critérios abaixo.

3.2. **Critérios de apuração.**

a) **Transação tributária** (por adesão, individual ou individual simplificada) **e demais modalidades de negociação com redução de valores**, inclusive parcelamentos especiais com redução de multas, juros ou encargos: a diferença entre (i) o valor consolidado dos débitos incluídos na negociação, compreendendo principal, multas, juros, encargos legais e demais acréscimos, conforme extrato oficial do órgão competente na data da formalização, e (ii) o valor total a pagar após a aplicação das reduções, na mesma data, desconsiderada a atualização futura das prestações. Para os fins desta alínea, os valores amortizados na forma da alínea "b" integram a parcela (i) e não integram a parcela (ii).

b) **Utilização de créditos de prejuízo fiscal, de base de cálculo negativa da CSLL, de precatórios ou de direitos creditórios** para amortização do saldo devedor (art. 11, IV e V, da Lei nº 13.988/2020, ou norma equivalente): {{percentual_creditos_pf}} por cento do valor do saldo devedor efetivamente amortizado por esses meios.

c) **Decisão administrativa ou judicial** que cancele, anule, reduza, declare extinto ou inexigível débito, inclusive por decadência, prescrição, revisão de dívida inscrita, exclusão de responsabilidade, impugnação, recurso, exceção de pré-executividade, embargos ou ação própria: o valor do débito cancelado, reduzido ou declarado extinto ou inexigível, com todos os acréscimos, atualizado até a data da decisão.

d) **Restituição, ressarcimento ou compensação** de tributos pagos indevidamente ou a maior, ou de créditos reconhecidos em favor da CONTRATANTE: o valor efetivamente restituído, ressarcido ou compensado, com a atualização aplicada pelo órgão ou fixada na decisão.

e) **Redução de base de cálculo, de alíquota ou de multa** reconhecida para fatos já ocorridos: a diferença entre o valor exigido e o valor efetivamente devido após a redução.

3.3. **Regras comuns de apuração.**

a) O proveito econômico existe ainda que o benefício decorra de edital, ato normativo ou programa de aplicação geral, desde que a adesão, o requerimento ou a medida tenha sido formalizada pela CONTRATADA ou com base no diagnóstico, na orientação ou nos cálculos por ela fornecidos.

b) A melhoria na classificação da capacidade de pagamento da CONTRATANTE obtida pela CONTRATADA não constitui proveito autônomo; seu efeito é apurado pelo aumento das reduções na forma da alínea "a" do item 3.2.

c) Não constituem, por si sós, proveito econômico: a suspensão da exigibilidade do crédito, a obtenção de certidão de regularidade fiscal, a liberação de constrições ou a substituição de garantias e o parcelamento sem qualquer redução de valores. Esses serviços são remunerados pelos honorários fixos, quando contratados.

d) O mesmo valor não será computado duas vezes. Se um débito for parcialmente cancelado e o saldo for depois objeto de transação, o proveito será a soma do valor cancelado (alínea "c") e da redução incidente sobre o saldo (alínea "a").

e) Os valores serão apurados com base em extratos, termos, recibos, decisões e demais documentos oficiais, que a CONTRATADA juntará a uma memória de cálculo enviada à CONTRATANTE.

3.4. **Conferência.** A CONTRATANTE terá 5 (cinco) dias úteis do recebimento da memória de cálculo para apontar, por escrito e de forma fundamentada, eventual divergência. Não havendo manifestação, a memória considera-se aceita. A divergência sobre parte do valor não suspende o pagamento da parte incontroversa.

3.5. **Proteção do diagnóstico.** Se, no prazo de {{meses_protecao}} meses contados da entrega do diagnóstico ou da proposta de estratégia pela CONTRATADA, ou da extinção deste contrato por iniciativa da CONTRATANTE sem justa causa, a CONTRATANTE obtiver, diretamente ou por intermédio de terceiros, proveito econômico por meio de medida identificada no diagnóstico ou na proposta da CONTRATADA, os honorários de êxito serão devidos como se a medida tivesse sido formalizada pela CONTRATADA.

## CLÁUSULA QUARTA — DO MOMENTO DO PAGAMENTO E DO PARCELAMENTO DOS HONORÁRIOS DE ÊXITO

4.1. **Momento em que os honorários de êxito são devidos.** O direito aos honorários de êxito nasce:

a) nas hipóteses das alíneas "a" e "b" do item 3.2, na data da formalização da transação ou da negociação, assim entendida a confirmação da adesão ou a assinatura do termo perante o órgão competente, o que ocorrer primeiro, ainda que a extinção dos créditos dependa do cumprimento integral das condições ajustadas (art. 3º, § 3º, da Lei nº 13.988/2020);

b) nas hipóteses das alíneas "c" e "e" do item 3.2, na data em que a decisão se tornar definitiva na esfera administrativa ou transitar em julgado, ou antes disso, se a Fazenda Pública cancelar ou reduzir o débito em cumprimento da decisão; e

c) na hipótese da alínea "d" do item 3.2, a cada restituição ou ressarcimento recebido e a cada compensação efetivamente realizada, na proporção do valor restituído, ressarcido ou compensado.

4.2. **Forma de pagamento.** Os honorários de êxito serão pagos em até {{parcelas_exito}} parcelas mensais e sucessivas, vencendo a primeira 30 (trinta) dias após o nascimento do direito, conforme o item 4.1. O número de parcelas dos honorários de êxito não excederá o número de prestações da própria transação ou do parcelamento obtido.

{{#desconto_avista}}4.3. Se a CONTRATANTE optar pelo pagamento à vista, em até 10 (dez) dias do nascimento do direito, terá desconto de {{percentual_desconto_avista}} por cento sobre o valor dos honorários de êxito.{{/desconto_avista}}

4.4. **Atraso e vencimento antecipado.** O atraso no pagamento de qualquer parcela sujeitará o valor devido a multa de 2% (dois por cento), juros de mora de 1% (um por cento) ao mês, *pro rata die*, e atualização monetária pela variação do IPCA/IBGE. O atraso de 2 (duas) parcelas, consecutivas ou não, acarretará o vencimento antecipado de todo o saldo.

4.5. **Rescisão da transação ou do parcelamento.** A rescisão da transação, do parcelamento ou da negociação por inadimplemento da CONTRATANTE ou por qualquer outra causa a ela imputável, inclusive as hipóteses do art. 4º da Lei nº 13.988/2020, não afasta nem reduz os honorários de êxito, cujo saldo vencerá antecipadamente. A CONTRATANTE declara ciência de que a rescisão da transação a impede de celebrar nova transação pelo prazo de 2 (dois) anos (art. 4º, § 4º, da Lei nº 13.988/2020).

4.6. Se a transação ou a decisão favorável for desfeita por causa não imputável à CONTRATANTE nem à CONTRATADA, os honorários de êxito serão recalculados sobre o proveito econômico efetivamente usufruído, compensando-se ou restituindo-se a diferença, sem acréscimos. Se a compensação de que trata a alínea "d" do item 3.2 for definitivamente não homologada, o valor de honorários a ela correspondente será abatido dos honorários futuros ou restituído à CONTRATANTE, sem acréscimos.

4.7. **Compensação com valores recebidos.** A CONTRATANTE autoriza expressamente a CONTRATADA, nos termos do art. 48, § 2º, do Código de Ética e Disciplina da OAB, a reter os honorários vencidos de valores que receber em nome da CONTRATANTE, inclusive por alvará, mediante prestação de contas documentada.

## CLÁUSULA QUINTA — DAS OBRIGAÇÕES DAS PARTES

5.1. A CONTRATADA obriga-se a prestar os serviços com zelo, diligência e independência técnica; a manter a CONTRATANTE informada do andamento; e a apresentar, antes de cada adesão ou negociação, a simulação com os valores, as reduções, o número e o valor estimado das prestações e as condições de manutenção do acordo.

5.2. A CONTRATANTE obriga-se a:

a) fornecer, nos prazos solicitados, documentos, informações contábeis e fiscais, certificados e acessos necessários, e cadastrar procuração eletrônica em favor dos advogados da CONTRATADA no Centro Virtual de Atendimento da Receita Federal (e-CAC) e nos demais sistemas exigidos;

b) manter atualizados os seus dados cadastrais perante os órgãos fazendários e informar à CONTRATADA, no mesmo dia, toda intimação, notificação, citação ou constrição que receber;

c) pagar pontualmente as prestações e cumprir as demais obrigações assumidas na transação, no parcelamento ou na negociação, inclusive a regularidade dos tributos vincendos, ciente de que o seu descumprimento pode levar à rescisão do acordo; e

d) pagar os honorários e as despesas na forma deste contrato.

5.3. Nenhuma adesão, proposta, desistência de impugnação ou ação, renúncia, confissão de dívida, oferta de garantia ou assunção de compromisso perante a Fazenda Pública ou o Poder Judiciário será formalizada sem a aprovação prévia e escrita da CONTRATANTE, admitida a aprovação por mensagem eletrônica enviada pelos canais oficiais pelo representante legal ou por pessoa por ele indicada por escrito.

## CLÁUSULA SEXTA — DA NATUREZA DA OBRIGAÇÃO

6.1. A obrigação da CONTRATADA é de meio. A CONTRATADA não garante resultado, percentual de desconto, prazo de pagamento, classificação de capacidade de pagamento, deferimento de pedidos, nem aceitação de proposta pela Fazenda Pública ou pelo Poder Judiciário.

6.2. Os percentuais de redução, prazos, prestações mínimas e condições de adesão são definidos pela lei, pelos editais e pelos atos normativos vigentes na data da adesão, podendo ser alterados, suspensos ou encerrados pela Administração a qualquer tempo, sem ingerência da CONTRATADA.

## CLÁUSULA SÉTIMA — DA VIGÊNCIA E DA EXTINÇÃO

7.1. Este contrato vigorará pelo prazo mínimo de {{meses_vigencia}} meses e, depois, até a conclusão dos serviços assinalados no Anexo I, incluídos o acompanhamento das transações e parcelamentos formalizados e o trânsito em julgado das medidas judiciais propostas.

7.2. A CONTRATANTE poderá revogar o mandato a qualquer tempo, permanecendo obrigada (art. 17 do Código de Ética e Disciplina da OAB) ao pagamento: (i) dos honorários fixos vencidos e das parcelas vincendas relativas a serviços já executados; (ii) dos honorários de êxito sobre o proveito econômico já obtido; e (iii) dos honorários de êxito sobre o proveito econômico que vier a decorrer de requerimentos, adesões, defesas ou ações protocolados pela CONTRATADA até a data da revogação, observado ainda o item 3.5.

7.3. A CONTRATADA poderá renunciar ao mandato, observado o art. 112 do Código de Processo Civil e o art. 5º, § 3º, da Lei nº 8.906/1994, fazendo jus aos honorários proporcionais aos serviços prestados e aos honorários de êxito sobre o proveito já obtido.

7.4. O inadimplemento de honorários por mais de 30 (trinta) dias autoriza a CONTRATADA, mediante comunicação escrita, a suspender a execução dos serviços não urgentes e, persistindo o inadimplemento, a resolver o contrato, sem prejuízo da cobrança dos valores devidos.

## CLÁUSULA OITAVA — DO SIGILO E DA PROTEÇÃO DE DADOS

8.1. A CONTRATADA guardará sigilo profissional sobre todas as informações recebidas, nos termos dos arts. 7º, II, e 34, VII, da Lei nº 8.906/1994 e dos arts. 35 a 38 do Código de Ética e Disciplina da OAB, estendendo esse dever a seus advogados, estagiários e colaboradores.

8.2. Os dados pessoais e fiscais recebidos serão tratados exclusivamente para a execução deste contrato, o exercício regular de direitos em processos administrativos e judiciais e o cumprimento de obrigações legais (arts. 7º, II, V e VI, e 11, II, "a" e "d", da Lei nº 13.709/2018), com medidas de segurança adequadas, admitido o armazenamento em serviços de nuvem e sistemas de gestão de terceiros com garantias de segurança, e conservados após a extinção do contrato apenas pelo prazo necessário ao cumprimento de obrigações legais e ao exercício regular de direitos.

## CLÁUSULA NONA — DISPOSIÇÕES FINAIS

9.1. As partes reconhecem a validade da assinatura deste instrumento por meio eletrônico, nos termos do art. 10, § 2º, da Medida Provisória nº 2.200-2/2001, e reconhecem-no como título executivo extrajudicial, nos termos do art. 24 da Lei nº 8.906/1994 e do art. 784, § 4º, do Código de Processo Civil.

9.2. A tolerância quanto ao descumprimento de qualquer obrigação não importa novação nem renúncia.

9.3. Integram este contrato o Anexo I — Serviços Contratados e o Anexo II — Modelo de Memória de Cálculo do Proveito Econômico.

9.4. Fica eleito o foro da comarca de {{foro_comarca}} para dirimir as controvérsias oriundas deste contrato, com renúncia a qualquer outro, por mais privilegiado que seja.

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

## ANEXO I — SERVIÇOS CONTRATADOS

Marcar com "X" os serviços compreendidos neste contrato:

- [{{svc_diagnostico}}] Diagnóstico do passivo fiscal, com levantamento dos débitos abrangidos e relatório de estratégia.
- [{{svc_capag}}] Análise da capacidade de pagamento e, se cabível, pedido de revisão.
- [{{svc_transacao}}] Transação tributária (por adesão, individual ou individual simplificada) e demais modalidades de negociação, com acompanhamento durante a vigência do acordo.
- [{{svc_parcelamento}}] Parcelamentos ordinários e especiais.
- [{{svc_defesa_adm}}] Defesas, impugnações, manifestações de inconformidade e recursos administrativos.
- [{{svc_execucao_fiscal}}] Defesa em execuções fiscais (exceção de pré-executividade, embargos e incidentes).
- [{{svc_judicial}}] Medidas judiciais próprias (mandado de segurança, ação anulatória, ação declaratória ou de repetição de indébito) relativas a: {{svc_judicial_descricao}}.
- [{{svc_recuperacao}}] Recuperação de créditos (restituição, ressarcimento e compensação).

## ANEXO II — MODELO DE MEMÓRIA DE CÁLCULO DO PROVEITO ECONÔMICO

| Débito / inscrição / processo | Critério (item 3.2) | Valor antes (data e fonte) | Valor depois (data e fonte) | Proveito | Honorários ({{percentual_exito}}%) | Data do direito (item 4.1) |
|---|---|---|---|---|---|---|
| | | | | | | |

Documentos anexos: extratos oficiais anteriores e posteriores, termo ou recibo de adesão, decisão ou comprovante de restituição/compensação.

<!-- FIM_DOCUMENTO -->
