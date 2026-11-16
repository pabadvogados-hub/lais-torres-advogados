# 07 — Contrato de honorários — causa avulsa (valor fixo + êxito opcional)

> **Bloco de preenchimento — não faz parte do documento.** O texto a ser gerado é apenas o que está entre
> os marcadores (comentários HTML) `INICIO_DOCUMENTO` e `FIM_DOCUMENTO`. Convenções: ver `README.md`.

| Campo | O que é | De onde vem |
|---|---|---|
| `{{cliente_nome}}` | Nome ou razão social | Ficha do cliente |
| `{{cliente_qualificacao}}` | Qualificação completa, no formato do modelo 01 (pessoa física) ou 02 (pessoa jurídica, com representante) | Ficha do cliente / contrato social |
| `{{escritorio_*}}`, `{{lais_*}}` | Dados fixos | `README.md` |
| `{{objeto_causa}}` | Descrição precisa da medida. Ex.: "ajuizamento de ação de execução de título extrajudicial em face de [devedor], para cobrança do crédito representado por [título]" ou "defesa na reclamação trabalhista nº [número], ajuizada por [reclamante]" | Ficha de atendimento / ADVBOX |
| `{{polo}}` | "autor(a)/exequente" ou "réu(ré)/reclamada" — define a base do êxito | Ficha de atendimento |
| `{{extensao_patrocinio}}` | Uma das opções da nota 2 | Proposta comercial |
| `{{valor_fixo}}`, `{{forma_pagamento_fixo}}` | Valor total com extenso; forma (ex.: "à vista, na assinatura" ou "em 3 parcelas mensais de R$ ...") | Proposta comercial |
| Bloco `{{#exito}}` | Honorários de êxito (opcional) | Proposta comercial |
| `{{percentual_exito}}` | Número + extenso, sem % | Proposta comercial |
| `{{base_exito}}` | Ver nota 3 | Proposta comercial |
| Bloco `{{#recurso_superior_excluido}}` / `{{valor_recurso_superior}}` | Usar quando a extensão for a opção (a) ou (c): honorários adicionais por recurso a tribunal superior | Proposta comercial |
| `{{valor_diligencia}}` | Valor por audiência/diligência fora da comarca de {{comarca_atendimento}} | Proposta comercial — observar a tabela da OAB |
| `{{comarca_atendimento}}`, `{{foro_comarca}}`, `{{cidade_assinatura}}`, `{{data_assinatura}}`, `{{testemunha*}}` | — | `README.md` / emissão |

**Notas de uso**

1. Use para: execução, monitória e cobrança de clientes de assessoria; defesa trabalhista; qualquer causa avulsa. O art. 48, § 1º, do Código de Ética e Disciplina (CED) exige que o contrato diga com clareza o objeto, os honorários, a forma de pagamento, a **extensão do patrocínio** (todos os atos ou só determinado grau) e **o que acontece se a causa terminar em acordo**. Este modelo cobre os quatro pontos.
2. `{{extensao_patrocinio}}` — opções:
   (a) "todos os atos do processo em primeiro grau de jurisdição, incluídos os recursos ao tribunal local e as contrarrazões, até o trânsito em julgado, e o cumprimento de sentença";
   (b) "todos os atos do processo em todas as instâncias, inclusive tribunais superiores, até o trânsito em julgado, e o cumprimento de sentença";
   (c) "exclusivamente a [ato específico]".
3. `{{base_exito}}` — sugestões:
   - Autor/exequente: "sobre o valor efetivamente recebido pelo(a) CONTRATANTE, em dinheiro ou bens, por pagamento, acordo, adjudicação, arrematação ou qualquer outra forma de satisfação do crédito".
   - Réu/reclamada: "sobre a diferença entre o valor total pretendido pela parte contrária na petição inicial, atualizado, e o valor efetivamente pago ou devido pelo(a) CONTRATANTE ao final, por decisão ou acordo". Atenção: pedidos iniciais inflados geram êxito alto — ver "Pontos para a Dra. Laís decidir".
4. Em causa trabalhista do lado do empregador, o êxito pela "economia" é aceito, mas deve ser explicado ao cliente na proposta.

---

<!-- INICIO_DOCUMENTO -->

# CONTRATO DE PRESTAÇÃO DE SERVIÇOS ADVOCATÍCIOS

Pelo presente instrumento particular, as partes abaixo qualificadas celebram contrato de prestação de serviços advocatícios, que se regerá pelas cláusulas seguintes e pela Lei nº 8.906/1994 (Estatuto da Advocacia e da OAB), pelo Regulamento Geral e pelo Código de Ética e Disciplina da OAB.

**CONTRATANTE:** {{cliente_qualificacao}}.

**CONTRATADA:** **{{escritorio_razao_social}}**, sociedade de advocacia inscrita no CNPJ sob o nº {{escritorio_cnpj}} e registrada na OAB/GO sob o nº {{escritorio_registro_oab}}, com sede em {{escritorio_endereco}}, endereço eletrônico {{escritorio_email}}, neste ato representada por sua titular, **{{lais_nome}}**, advogada inscrita na {{lais_oab}}.

## CLÁUSULA PRIMEIRA — DO OBJETO E DA EXTENSÃO DO PATROCÍNIO

1.1. O objeto deste contrato é a prestação, pela CONTRATADA, dos serviços advocatícios de {{objeto_causa}}, figurando o(a) CONTRATANTE como {{polo}}.

1.2. O patrocínio compreende {{extensao_patrocinio}}.

1.3. Não estão compreendidos no objeto, e dependerão de contratação própria:

a) ações conexas, incidentais ou autônomas não mencionadas no item 1.1, inclusive embargos de terceiro, ações rescisórias e ações de outra natureza propostas pela parte contrária ou por terceiros;

b) a defesa em processos administrativos; e

c) atos não compreendidos na extensão do patrocínio definida no item 1.2.

{{#recurso_superior_excluido}}1.3.1. Se a extensão do patrocínio não abranger os tribunais superiores e o(a) CONTRATANTE optar pela interposição ou resposta a recurso especial, extraordinário, de revista ou respectivos agravos, os honorários serão de {{valor_recurso_superior}} por recurso.{{/recurso_superior_excluido}}

1.4. A obrigação da CONTRATADA é de meio, e não de resultado. A CONTRATADA não garante o êxito da demanda, o seu prazo de duração nem o recebimento efetivo de valores, que depende, entre outros fatores, da existência de patrimônio da parte contrária.

## CLÁUSULA SEGUNDA — DOS HONORÁRIOS

2.1. **Honorários fixos.** O(A) CONTRATANTE pagará à CONTRATADA honorários fixos de **{{valor_fixo}}**, {{forma_pagamento_fixo}}. Os honorários fixos remuneram o trabalho técnico independentemente do resultado e não são restituíveis após o protocolo da primeira peça ou a prática do primeiro ato.

{{#exito}}2.2. **Honorários de êxito.** Além dos honorários fixos, o(a) CONTRATANTE pagará à CONTRATADA honorários de êxito de **{{percentual_exito}} por cento**, calculados {{base_exito}}.

2.3. Os honorários de êxito serão pagos no prazo de 5 (cinco) dias úteis a contar do recebimento dos valores pelo(a) CONTRATANTE ou, na hipótese de economia obtida pelo(a) CONTRATANTE no polo passivo, da homologação do acordo ou do trânsito em julgado da decisão. Se o recebimento ou o pagamento ocorrer em parcelas, os honorários serão devidos na mesma proporção, a cada parcela.

2.4. Os honorários de êxito são devidos também na hipótese de acordo, judicial ou extrajudicial, celebrado a qualquer tempo, inclusive antes do ajuizamento ou diretamente entre as partes, sendo vedada a sua redução em razão de a solução ter sido alcançada por meio consensual (art. 48, § 5º, do Código de Ética e Disciplina da OAB).{{/exito}}

2.5. **Honorários de sucumbência.** Os honorários de sucumbência pertencem exclusivamente à CONTRATADA (arts. 22 e 23 da Lei nº 8.906/1994), não se compensam com os honorários contratuais e, somados a estes, não poderão superar o proveito obtido pelo(a) CONTRATANTE (art. 50 do Código de Ética e Disciplina da OAB). Em caso de acordo, o(a) CONTRATANTE não poderá dispor dos honorários de sucumbência sem a anuência da CONTRATADA.

2.6. **Retenção.** O(A) CONTRATANTE autoriza expressamente a CONTRATADA a reter, de valores que receber em seu nome, inclusive por alvará, os honorários contratuais vencidos e as despesas por ela antecipadas, mediante prestação de contas documentada (art. 48, §§ 2º e 3º, do Código de Ética e Disciplina da OAB), e a requerer a reserva dos honorários contratuais nos autos (art. 22, § 4º, da Lei nº 8.906/1994).

2.7. **Forma de pagamento e atraso.** Os pagamentos serão feitos por boleto bancário ou Pix emitido pela CONTRATADA. Não será emitida duplicata nem levada a protesto fatura relativa a honorários (art. 52 do Código de Ética e Disciplina da OAB). O atraso sujeitará o valor devido a multa de 2% (dois por cento), juros de mora de 1% (um por cento) ao mês e atualização monetária pela variação do IPCA/IBGE.

## CLÁUSULA TERCEIRA — DAS DESPESAS

3.1. Custas, preparo de recursos, depósitos recursais, emolumentos, honorários periciais, despesas de citação, intimação, publicação de editais, certidões, pesquisas patrimoniais pagas, cópias e postagens correrão por conta do(a) CONTRATANTE, mediante aprovação prévia, e não estão incluídos nos honorários (art. 48, § 3º, do Código de Ética e Disciplina da OAB).

3.2. Audiências e diligências fora da comarca de {{comarca_atendimento}} serão remuneradas à parte, no valor de {{valor_diligencia}} por ato, acrescido das despesas de deslocamento, hospedagem e alimentação, salvo se realizadas por meio telepresencial.

3.3. O(A) CONTRATANTE responde pelos honorários de sucumbência devidos à parte contrária e pelas multas processuais que vierem a ser impostas, salvo as decorrentes de culpa da CONTRATADA.

## CLÁUSULA QUARTA — DAS OBRIGAÇÕES DO(A) CONTRATANTE

4.1. O(A) CONTRATANTE obriga-se a fornecer informações verdadeiras e completas e os documentos solicitados, nos prazos indicados; a comparecer ou fazer-se representar nas audiências e perícias para as quais for convocado(a); a comunicar imediatamente qualquer alteração de endereço, telefone ou e-mail; a informar à CONTRATADA qualquer contato, proposta ou pagamento feito diretamente pela ou à parte contrária; e a não celebrar acordo sem a participação da CONTRATADA.

## CLÁUSULA QUINTA — DA EXTINÇÃO

5.1. A revogação do mandato pelo(a) CONTRATANTE não o(a) desobriga do pagamento dos honorários contratados (art. 17 do Código de Ética e Disciplina da OAB). Revogado o mandato: (i) os honorários fixos tornam-se integralmente exigíveis; e (ii) os honorários de êxito, se previstos, serão devidos sobre o proveito que vier a ser obtido na causa, de forma proporcional ao trabalho realizado até a revogação, sem prejuízo dos honorários de sucumbência proporcionais.

5.2. A CONTRATADA poderá renunciar ao mandato, observados o art. 112 do Código de Processo Civil e o art. 5º, § 3º, da Lei nº 8.906/1994, fazendo jus aos honorários proporcionais aos serviços prestados.

5.3. O inadimplemento dos honorários por mais de 30 (trinta) dias autoriza a CONTRATADA a renunciar ao mandato, mediante comunicação escrita, permanecendo devidos os valores vencidos.

## CLÁUSULA SEXTA — DO SIGILO E DA PROTEÇÃO DE DADOS

6.1. A CONTRATADA guardará sigilo profissional sobre as informações recebidas, nos termos dos arts. 7º, II, e 34, VII, da Lei nº 8.906/1994 e dos arts. 35 a 38 do Código de Ética e Disciplina da OAB.

6.2. Os dados pessoais do(a) CONTRATANTE e de terceiros serão tratados para a execução deste contrato e para o exercício regular de direitos em processo judicial, administrativo ou arbitral (arts. 7º, V e VI, e 11, II, "d", da Lei nº 13.709/2018), com medidas de segurança adequadas, e conservados após o encerramento apenas pelo prazo necessário ao cumprimento de obrigações legais e ao exercício regular de direitos.

## CLÁUSULA SÉTIMA — DISPOSIÇÕES FINAIS

7.1. As partes reconhecem a validade da assinatura deste instrumento por meio eletrônico, nos termos do art. 10, § 2º, da Medida Provisória nº 2.200-2/2001, e reconhecem-no como título executivo extrajudicial, nos termos do art. 24 da Lei nº 8.906/1994 e do art. 784, § 4º, do Código de Processo Civil.

7.2. Fica eleito o foro da comarca de {{foro_comarca}} para dirimir as controvérsias oriundas deste contrato.

E, por estarem justas e contratadas, as partes assinam este instrumento, juntamente com duas testemunhas.

{{cidade_assinatura}}, {{data_assinatura}}.

&nbsp;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**CONTRATANTE** — {{cliente_nome}}

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**CONTRATADA** — {{escritorio_razao_social}}
p. {{lais_nome}} — {{lais_oab}}

**Testemunhas:**

1. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Nome: {{testemunha1_nome}} — CPF: {{testemunha1_cpf}}
2. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Nome: {{testemunha2_nome}} — CPF: {{testemunha2_cpf}}

<!-- FIM_DOCUMENTO -->
