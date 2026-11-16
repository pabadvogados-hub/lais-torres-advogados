# 02 — Procuração ad judicia et extra — pessoa jurídica (com representante legal)

> **Bloco de preenchimento — não faz parte do documento.** O texto a ser gerado é apenas o que está entre
> os marcadores (comentários HTML) `INICIO_DOCUMENTO` e `FIM_DOCUMENTO`. Convenções: ver `README.md`.

| Campo | O que é | De onde vem |
|---|---|---|
| `{{cliente_razao_social}}` | Razão social exata | Comprovante de inscrição no CNPJ / contrato social |
| `{{cliente_nome_fantasia}}` | Opcional | Comprovante do CNPJ |
| `{{cliente_cnpj}}` | CNPJ | Comprovante do CNPJ |
| `{{cliente_endereco}}` | Endereço da sede com CEP | Comprovante do CNPJ / contrato social |
| `{{cliente_email}}` | E-mail da empresa | Ficha de cadastro |
| `{{representante_nome}}` | Nome do(s) administrador(es) com poderes de representação | Contrato social / última alteração consolidada / ata de eleição |
| `{{representante_qualificacao}}` | Nacionalidade, estado civil, profissão | Ficha de cadastro do representante |
| `{{representante_cargo}}` | Ex.: sócio-administrador, diretor-presidente | Contrato social / estatuto |
| `{{representante_cpf}}` / `{{representante_rg}}` | Documentos do representante | Documento de identidade |
| `{{representacao_conjunta}}` | Opcional: segundo administrador, quando o contrato social exigir assinatura conjunta | Contrato social (cláusula de administração) |
| `{{escritorio_*}}`, `{{lais_*}}`, `{{alex_*}}`, `{{advogados_adicionais}}` | Dados fixos do escritório | `README.md` |
| `{{finalidade_especifica}}` | Opcional | Ficha de atendimento / ADVBOX |
| `{{cidade_assinatura}}` / `{{data_assinatura}}` | Local e data | Gerado na emissão |
| Bloco `{{#poderes_tributarios}}` | Incluir em todo cliente com serviço tributário | Tipo de contrato (modelo 06) |
| Bloco `{{#poderes_trabalhistas}}` | Incluir em cliente de assessoria com passivo trabalhista | Tipo de contrato (modelo 05) |

**Notas de uso**

1. Conferir **sempre** a cláusula de administração do contrato social: quem representa a sociedade, se a assinatura é isolada ou conjunta e se há limitação de poderes (art. 75, VIII, do CPC — a pessoa jurídica é representada por quem os atos constitutivos designarem). Arquivar cópia do contrato social e da última alteração na pasta do cliente; o juízo pode exigi-los.
2. Mesmos fundamentos do modelo 01 (art. 105 do CPC; arts. 5º, § 2º, e 15, § 3º, do EAOAB).
3. A procuração **não** substitui a carta de preposição (modelo 04): o advogado não pode ser, no mesmo processo, patrono e preposto (art. 25 do Código de Ética e Disciplina da OAB).
4. Não incluímos "assinar declaração de hipossuficiência" por padrão: para pessoa jurídica a gratuidade exige prova da impossibilidade de arcar com os encargos processuais. Se for o caso, acrescentar o poder manualmente.

---

<!-- INICIO_DOCUMENTO -->

# PROCURAÇÃO AD JUDICIA ET EXTRA

**OUTORGANTE:** **{{cliente_razao_social}}**{{#cliente_nome_fantasia}} ({{cliente_nome_fantasia}}){{/cliente_nome_fantasia}}, pessoa jurídica de direito privado, inscrita no CNPJ sob o nº {{cliente_cnpj}}, com sede em {{cliente_endereco}}, endereço eletrônico {{cliente_email}}, neste ato representada, na forma de seus atos constitutivos, por seu(sua) {{representante_cargo}}, **{{representante_nome}}**, {{representante_qualificacao}}, portador(a) do RG nº {{representante_rg}} e inscrito(a) no CPF sob o nº {{representante_cpf}}{{#representacao_conjunta}}, em conjunto com {{representacao_conjunta}}{{/representacao_conjunta}}.

**OUTORGADOS:** **{{lais_nome}}**, advogada inscrita na {{lais_oab}}{{#lais_oab_suplementar}} e, por inscrição suplementar, na {{lais_oab_suplementar}}{{/lais_oab_suplementar}}, e **{{alex_nome}}**, advogado inscrito na {{alex_oab}}, {{alex_vinculo}}{{#advogados_adicionais}}, e {{advogados_adicionais}}{{/advogados_adicionais}}, integrantes de **{{escritorio_razao_social}}**, sociedade de advocacia inscrita no CNPJ sob o nº {{escritorio_cnpj}} e registrada na OAB/GO sob o nº {{escritorio_registro_oab}}, com sede em {{escritorio_endereco}}, endereço eletrônico {{escritorio_email}}, onde recebem intimações e notificações.

**PODERES:** Pelo presente instrumento particular de mandato, a OUTORGANTE nomeia e constitui seus procuradores os OUTORGADOS, a quem confere os poderes da cláusula *ad judicia et extra*, para o foro em geral, em qualquer juízo, instância ou tribunal, inclusive juizados especiais, Justiça do Trabalho, Justiça Federal e tribunais superiores, podendo propor as ações competentes e defendê-la nas contrárias, seguindo umas e outras até decisão final, interpor e acompanhar recursos, requerer o cumprimento de sentença, promover execuções, ações monitórias e de cobrança, habilitar créditos em recuperação judicial e falência, e praticar todos os atos necessários ao fiel desempenho deste mandato.

Confere-lhes, ainda, poderes para representá-la perante quaisquer órgãos e entidades da administração pública direta e indireta, federal, estadual e municipal, juntas comerciais, cartórios e serventias extrajudiciais, órgãos de proteção e defesa do consumidor e instituições financeiras, podendo requerer, protocolar, apresentar defesas, impugnações e recursos administrativos, obter certidões, cópias, extratos e informações, e assinar requerimentos e termos.

{{#poderes_tributarios}}Em especial, confere-lhes poderes para representá-la perante a Secretaria Especial da Receita Federal do Brasil, a Procuradoria-Geral da Fazenda Nacional, inclusive no portal Regularize, as Fazendas estaduais e municipais e respectivas Procuradorias, podendo consultar débitos, situação fiscal e classificação de capacidade de pagamento; apresentar impugnações, manifestações de inconformidade, recursos administrativos, pedidos de revisão de dívida inscrita e de revisão da capacidade de pagamento; aderir a transação tributária, por adesão ou individual, a parcelamentos e a negócio jurídico processual; propor, negociar e assinar termos de transação; e oferecer, substituir ou requerer a liberação de garantias, observada a prévia aprovação da OUTORGANTE quanto aos atos que importem assunção de obrigações.{{/poderes_tributarios}}

{{#poderes_trabalhistas}}Em especial, confere-lhes poderes para representá-la perante a Justiça do Trabalho, o Ministério do Trabalho e Emprego e o Ministério Público do Trabalho, inclusive em procedimentos de fiscalização, mediações e inquéritos civis, podendo apresentar defesas a autos de infração e firmar termos, observada a prévia aprovação da OUTORGANTE quanto a compromissos de ajustamento de conduta.{{/poderes_trabalhistas}}

**PODERES ESPECIAIS:** Nos termos do art. 105 do Código de Processo Civil e do art. 661, § 1º, do Código Civil, confere-lhes, em cláusula específica, poderes especiais para receber citação, confessar, reconhecer a procedência do pedido, transigir, desistir, renunciar ao direito sobre o qual se funda a ação, firmar compromisso, celebrar acordos judiciais e extrajudiciais, receber e dar quitação, levantar alvarás e requerer a expedição de requisições de pequeno valor e precatórios.

Os OUTORGADOS poderão agir em conjunto ou separadamente, independentemente da ordem de nomeação, e substabelecer, no todo ou em parte, com ou sem reserva de iguais poderes.

{{#finalidade_especifica}}**FINALIDADE ESPECÍFICA:** sem prejuízo dos poderes gerais acima, o presente mandato é outorgado especialmente para {{finalidade_especifica}}.{{/finalidade_especifica}}

{{cidade_assinatura}}, {{data_assinatura}}.

&nbsp;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**{{cliente_razao_social}}**
CNPJ nº {{cliente_cnpj}}
p. {{representante_nome}} — {{representante_cargo}} — CPF nº {{representante_cpf}}

{{#representacao_conjunta}}
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

p. {{representacao_conjunta}}
{{/representacao_conjunta}}

<!-- FIM_DOCUMENTO -->
