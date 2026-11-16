# 01 — Procuração ad judicia et extra — pessoa física

> **Bloco de preenchimento — não faz parte do documento.** O texto a ser gerado é apenas o que está entre
> os marcadores (comentários HTML) `INICIO_DOCUMENTO` e `FIM_DOCUMENTO`. Convenções de campos e blocos condicionais: ver `README.md`.

| Campo | O que é | De onde vem |
|---|---|---|
| `{{cliente_nome}}` | Nome completo do outorgante, sem abreviação | Documento de identidade (ficha de cadastro do cliente) |
| `{{cliente_nacionalidade}}` | Ex.: brasileiro(a) | Ficha de cadastro |
| `{{cliente_estado_civil}}` | Estado civil; se em união estável, escrever "convivente em união estável" | Ficha de cadastro |
| `{{cliente_profissao}}` | Profissão | Ficha de cadastro |
| `{{cliente_rg}}` / `{{cliente_rg_orgao}}` | RG e órgão expedidor/UF | Documento de identidade |
| `{{cliente_cpf}}` | CPF | Documento de identidade / CPF |
| `{{cliente_endereco}}` | Endereço completo com CEP | Comprovante de endereço |
| `{{cliente_email}}` | E-mail do cliente | Ficha de cadastro |
| `{{escritorio_*}}`, `{{lais_*}}`, `{{alex_*}}` | Dados fixos do escritório e dos advogados | `README.md` — seção "Campos fixos do escritório" |
| `{{advogados_adicionais}}` | Opcional: outros advogados outorgados (nome, OAB, vínculo com a sociedade) | Preenchimento manual; só incluir advogado(a) com contrato de associação averbado ou empregado(a) |
| `{{finalidade_especifica}}` | Opcional: descrição do caso (ex.: "ajuizar ação de indenização em face de Fulano") | Ficha de atendimento / ADVBOX |
| `{{cidade_assinatura}}` / `{{data_assinatura}}` | Local e data por extenso | Gerado na emissão |
| Bloco `{{#hipossuficiencia}}` | Incluir só se o cliente for requerer gratuidade de justiça | Decisão do advogado responsável |

**Notas de uso**

1. Fundamentos: art. 105 do CPC (poderes gerais e cláusula específica de poderes especiais; §§ 2º e 3º exigem nome, número de inscrição e endereço completo do advogado e, se integrar sociedade, nome, registro e endereço da sociedade); art. 287 do CPC (endereço eletrônico e não eletrônico do advogado); art. 5º, § 2º, e art. 15, § 3º, do EAOAB (procuração outorgada individualmente aos advogados, com indicação da sociedade); art. 654, § 1º, do Código Civil.
2. Pelo art. 105, § 4º, do CPC, a procuração outorgada na fase de conhecimento vale para o cumprimento de sentença, salvo ressalva expressa — este modelo não faz ressalva.
3. A redação é deliberadamente ampla (todos os foros e órgãos). Se o cliente pedir procuração restrita a um caso, preencher `{{finalidade_especifica}}` e manter os demais poderes.
4. Tributário federal: a procuração em papel **não substitui** a procuração eletrônica no e-CAC, que o cliente cadastra em nome do advogado.
5. Assinatura eletrônica: ver o ponto `[CONFERIR]` no `README.md` sobre aceitação, por juízos do TJGO, TJMA e TRTs da 16ª e 18ª Regiões, de procuração assinada em plataforma privada (sem certificado ICP-Brasil). Na dúvida, usar a assinatura gov.br ou ICP-Brasil.

---

<!-- INICIO_DOCUMENTO -->

# PROCURAÇÃO AD JUDICIA ET EXTRA

**OUTORGANTE:** {{cliente_nome}}, {{cliente_nacionalidade}}, {{cliente_estado_civil}}, {{cliente_profissao}}, portador(a) da cédula de identidade RG nº {{cliente_rg}} — {{cliente_rg_orgao}}, inscrito(a) no CPF sob o nº {{cliente_cpf}}, residente e domiciliado(a) em {{cliente_endereco}}, endereço eletrônico {{cliente_email}}.

**OUTORGADOS:** **{{lais_nome}}**, advogada inscrita na {{lais_oab}}{{#lais_oab_suplementar}} e, por inscrição suplementar, na {{lais_oab_suplementar}}{{/lais_oab_suplementar}}, e **{{alex_nome}}**, advogado inscrito na {{alex_oab}}, {{alex_vinculo}}{{#advogados_adicionais}}, e {{advogados_adicionais}}{{/advogados_adicionais}}, integrantes de **{{escritorio_razao_social}}**, sociedade de advocacia inscrita no CNPJ sob o nº {{escritorio_cnpj}} e registrada na OAB/GO sob o nº {{escritorio_registro_oab}}, com sede em {{escritorio_endereco}}, endereço eletrônico {{escritorio_email}}, onde recebem intimações e notificações.

**PODERES:** Pelo presente instrumento particular de mandato, o(a) OUTORGANTE nomeia e constitui seus procuradores os OUTORGADOS, a quem confere os poderes da cláusula *ad judicia et extra*, para o foro em geral, em qualquer juízo, instância ou tribunal, inclusive juizados especiais, Justiça do Trabalho, Justiça Federal e tribunais superiores, podendo propor as ações competentes e defendê-lo(a) nas contrárias, seguindo umas e outras até decisão final, interpor e acompanhar recursos, requerer o cumprimento de sentença e praticar todos os atos necessários ao fiel desempenho deste mandato.

Confere-lhes, ainda, poderes para representá-lo(a) perante quaisquer órgãos e entidades da administração pública direta e indireta, federal, estadual e municipal, inclusive Secretaria Especial da Receita Federal do Brasil, Procuradoria-Geral da Fazenda Nacional, Procuradorias estaduais e municipais, Secretarias de Fazenda, Instituto Nacional do Seguro Social, órgãos de proteção e defesa do consumidor, departamentos de trânsito, juntas comerciais, cartórios e serventias extrajudiciais e instituições financeiras, podendo requerer, protocolar, apresentar defesas, impugnações e recursos administrativos, obter certidões, cópias, extratos e informações, e assinar requerimentos e termos.

**PODERES ESPECIAIS:** Nos termos do art. 105 do Código de Processo Civil e do art. 661, § 1º, do Código Civil, confere-lhes, em cláusula específica, poderes especiais para receber citação, confessar, reconhecer a procedência do pedido, transigir, desistir, renunciar ao direito sobre o qual se funda a ação, firmar compromisso, celebrar acordos judiciais e extrajudiciais, receber e dar quitação, levantar alvarás, requerer a expedição de requisições de pequeno valor e precatórios{{#hipossuficiencia}} e assinar declaração de hipossuficiência econômica{{/hipossuficiencia}}.

Os OUTORGADOS poderão agir em conjunto ou separadamente, independentemente da ordem de nomeação, e substabelecer, no todo ou em parte, com ou sem reserva de iguais poderes.

{{#finalidade_especifica}}**FINALIDADE ESPECÍFICA:** sem prejuízo dos poderes gerais acima, o presente mandato é outorgado especialmente para {{finalidade_especifica}}.{{/finalidade_especifica}}

{{cidade_assinatura}}, {{data_assinatura}}.

&nbsp;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**{{cliente_nome}}**
CPF nº {{cliente_cpf}}

<!-- FIM_DOCUMENTO -->
