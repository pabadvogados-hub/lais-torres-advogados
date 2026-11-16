# 04 — Carta de preposição (Justiça do Trabalho)

> **Bloco de preenchimento — não faz parte do documento.** O texto a ser gerado é apenas o que está entre
> os marcadores (comentários HTML) `INICIO_DOCUMENTO` e `FIM_DOCUMENTO`. Convenções: ver `README.md`.

| Campo | O que é | De onde vem |
|---|---|---|
| `{{cliente_razao_social}}` / `{{cliente_cnpj}}` / `{{cliente_endereco}}` | Reclamada (empregador) | Ficha do cliente / contrato social |
| `{{representante_nome}}` / `{{representante_cargo}}` / `{{representante_cpf}}` | Quem assina pela empresa | Contrato social (cláusula de administração) |
| `{{preposto_nome}}` | Nome completo do preposto | Indicação do cliente |
| `{{preposto_cpf}}` / `{{preposto_rg}}` | Documentos do preposto | Documento de identidade (o preposto deve levá-lo à audiência) |
| `{{preposto_vinculo}}` | Ex.: "empregado(a) da Reclamada, no cargo de gerente administrativo" **ou** "não empregado(a), na qualidade de [contador(a) / sócio(a) / prestador(a) de serviços]" | Indicação do cliente |
| `{{processo_numero}}` | Número CNJ da reclamação trabalhista | ADVBOX / notificação |
| `{{processo_vara}}` | Ex.: "1ª Vara do Trabalho de Imperatriz/MA" | Notificação |
| `{{reclamante_nome}}` | Reclamante | Notificação / petição inicial |
| `{{audiencia_data}}` / `{{audiencia_hora}}` / `{{audiencia_tipo}}` | Data, hora e tipo (inicial, una, instrução, telepresencial) | ADVBOX / notificação |
| `{{limite_acordo}}` | Completa a frase "celebrar acordo ...": **ou** "até o limite de R$ [valor] ([extenso])" **ou** "nos limites previamente ajustados com os advogados constituídos" | Decisão do cliente, registrada por escrito antes da audiência |
| `{{cidade_assinatura}}` / `{{data_assinatura}}` | Local e data | Gerado na emissão |

**Notas de uso**

1. **Base legal.** Art. 843, § 1º, da CLT: o empregador pode fazer-se substituir pelo gerente ou por qualquer outro preposto **que tenha conhecimento do fato**, e as declarações do preposto **obrigam o proponente**. Art. 843, § 3º (incluído pela Lei nº 13.467/2017): o preposto **não precisa ser empregado** da reclamada. A exigência de preposto empregado da antiga Súmula 377 do TST ficou superada para as ações regidas pela Reforma Trabalhista.
2. **Conhecimento dos fatos é o ponto crítico.** Preposto que desconhece os fatos gera, na prática, confissão quanto à matéria de fato. Preparar o preposto antes da audiência (roteiro no checklist trabalhista) e escolher quem efetivamente acompanhou a relação de emprego.
3. **Ausência.** Art. 844 da CLT: o não comparecimento da reclamada importa revelia e confissão quanto à matéria de fato; pelo § 5º, presente o advogado, são aceitos a contestação e os documentos. Não dispensar o preposto por causa disso.
4. **Vedação ética.** O advogado não pode funcionar no mesmo processo, simultaneamente, como patrono e preposto (art. 25 do Código de Ética e Disciplina da OAB). Nenhum advogado ou estagiário do escritório deve ser indicado como preposto em processo patrocinado pelo escritório.
5. **Acordo.** O preposto só deve aceitar acordo dentro do limite autorizado por escrito pela empresa. O teto não precisa constar da carta; se o cliente preferir não expor o valor, usar a expressão alternativa do campo `{{limite_acordo}}`.
6. A carta é assinada pelo representante legal com poderes (conferir contrato social). Junta-se aos autos com os atos constitutivos, se o juízo exigir.

---

<!-- INICIO_DOCUMENTO -->

# CARTA DE PREPOSIÇÃO

**Ao Juízo da {{processo_vara}}**

**Processo nº:** {{processo_numero}}
**Reclamante:** {{reclamante_nome}}
**Reclamada:** {{cliente_razao_social}}

**{{cliente_razao_social}}**, pessoa jurídica de direito privado, inscrita no CNPJ sob o nº {{cliente_cnpj}}, com sede em {{cliente_endereco}}, neste ato representada por seu(sua) {{representante_cargo}}, **{{representante_nome}}**, inscrito(a) no CPF sob o nº {{representante_cpf}}, vem, com fundamento no art. 843, §§ 1º e 3º, da Consolidação das Leis do Trabalho, **CREDENCIAR** como sua preposta, nos autos em epígrafe, a pessoa de **{{preposto_nome}}**, portador(a) do RG nº {{preposto_rg}} e inscrito(a) no CPF sob o nº {{preposto_cpf}}, {{preposto_vinculo}}, que tem conhecimento dos fatos objeto da reclamação.

O(A) preposto(a) fica autorizado(a) a representar a Reclamada na audiência {{audiencia_tipo}} designada para {{audiencia_data}}, às {{audiencia_hora}}, e nas que se seguirem, inclusive por meio telepresencial, podendo prestar depoimento pessoal em nome da Reclamada, cujas declarações a obrigam, participar de tentativas de conciliação, celebrar acordo {{limite_acordo}}, e assinar termos e atas de audiência.

A Reclamada declara ciência de que as declarações prestadas pelo(a) preposto(a) obrigam a empresa, nos termos do art. 843, § 1º, da CLT.

{{cidade_assinatura}}, {{data_assinatura}}.

&nbsp;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**{{cliente_razao_social}}**
CNPJ nº {{cliente_cnpj}}
p. {{representante_nome}} — {{representante_cargo}}

&nbsp;

Ciente e de acordo:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**{{preposto_nome}}**
CPF nº {{preposto_cpf}}

<!-- FIM_DOCUMENTO -->
