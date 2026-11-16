# 03 — Substabelecimento (com reserva e sem reserva de poderes)

> **Bloco de preenchimento — não faz parte do documento.** Este arquivo tem **duas versões**. Gerar apenas uma:
> - **Versão A — COM reserva** (marcadores `INICIO_DOCUMENTO_A` / `FIM_DOCUMENTO_A`): o escritório continua no processo e
>   acrescenta outro advogado (correspondente, associado, advogado em audiência).
> - **Versão B — SEM reserva** (marcadores `INICIO_DOCUMENTO_B` / `FIM_DOCUMENTO_B`): o escritório sai do processo e
>   transfere o mandato.

| Campo | O que é | De onde vem |
|---|---|---|
| `{{substabelecente_nome}}` / `{{substabelecente_oab}}` | Advogado(a) do escritório que assina | `README.md` (campos fixos) |
| `{{substabelecido_nome}}` / `{{substabelecido_oab}}` | Advogado(a) que recebe os poderes | Cadastro do correspondente / associado |
| `{{substabelecido_endereco}}` / `{{substabelecido_email}}` | Endereço profissional e eletrônico | Idem |
| `{{substabelecido_sociedade}}` | Opcional: sociedade a que pertence o substabelecido (art. 15, § 3º, EAOAB) | Idem |
| `{{cliente_nome}}` | Nome ou razão social do cliente (outorgante original) | ADVBOX / ficha do cliente |
| `{{processo_numero}}` / `{{processo_juizo}}` | Número CNJ e juízo | ADVBOX |
| `{{parte_contraria}}` | Nome da parte contrária | ADVBOX |
| `{{escopo_substabelecimento}}` | Versão A: "todos os atos do processo" ou ato específico (ex.: "comparecer à audiência de {{data}}") | Preenchimento manual |
| `{{honorarios_substabelecido}}` | Versão A: ajuste de honorários entre substabelecente e substabelecido | Preenchimento manual — art. 26, § 2º, do CED exige ajuste prévio |
| `{{ciencia_cliente_data}}` / `{{ciencia_cliente_meio}}` | Versão B: data e meio pelo qual o cliente tomou ciência prévia | Registro da comunicação (e-mail/WhatsApp) — guardar na pasta do cliente |
| `{{cidade_assinatura}}` / `{{data_assinatura}}` | Local e data | Gerado na emissão |

**Notas de uso**

1. Base: art. 667 do Código Civil; art. 26 do Código de Ética e Disciplina da OAB — o substabelecimento **com** reserva é ato pessoal do advogado (caput); o **sem** reserva exige "prévio e inequívoco conhecimento do cliente" (§ 1º); o substabelecido com reserva deve ajustar antecipadamente seus honorários com o substabelecente (§ 2º).
2. Antes de substabelecer, conferir se a procuração original admite substabelecimento (os modelos 01 e 02 admitem).
3. Para estagiário inscrito na OAB praticar atos extrajudiciais isoladamente, basta autorização ou substabelecimento (art. 29, § 2º, do Regulamento Geral do EAOAB). Atos judiciais do estagiário são sempre em conjunto com advogado (art. 29, caput), salvo os do art. 29, § 1º.
4. Na versão B, o cliente deve ser comunicado **antes** da assinatura; a comunicação fica arquivada. Se a saída decorrer de renúncia, observar o art. 112 do CPC e o art. 5º, § 3º, do EAOAB (10 dias), e não usar este modelo — usar comunicação de renúncia.

---

<!-- INICIO_DOCUMENTO_A -->

# SUBSTABELECIMENTO COM RESERVA DE PODERES

Pelo presente instrumento, **{{substabelecente_nome}}**, advogado(a) inscrito(a) na {{substabelecente_oab}}, integrante de {{escritorio_razao_social}}, CNPJ nº {{escritorio_cnpj}}, com escritório em {{escritorio_endereco}}, na qualidade de procurador(a) de **{{cliente_nome}}**, **SUBSTABELECE, COM RESERVA DE IGUAIS PODERES**, na pessoa de **{{substabelecido_nome}}**, advogado(a) inscrito(a) na {{substabelecido_oab}}{{#substabelecido_sociedade}}, integrante de {{substabelecido_sociedade}}{{/substabelecido_sociedade}}, com endereço profissional em {{substabelecido_endereco}}, endereço eletrônico {{substabelecido_email}}, os poderes que lhe foram conferidos pelo(a) outorgante, para {{escopo_substabelecimento}}, nos autos do processo nº {{processo_numero}}, em trâmite perante {{processo_juizo}}, em que figura como parte contrária {{parte_contraria}}.

O(A) substabelecente permanece constituído(a) nos autos e continua responsável pelo patrocínio da causa perante o(a) cliente. As intimações devem continuar a ser publicadas também em nome do(a) substabelecente.

Os honorários do(a) substabelecido(a) foram previamente ajustados com o(a) substabelecente, nos termos do art. 26, § 2º, do Código de Ética e Disciplina da OAB, e não acarretam ônus adicional ao(à) cliente.

{{cidade_assinatura}}, {{data_assinatura}}.

&nbsp;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**{{substabelecente_nome}}**
{{substabelecente_oab}}

<!-- FIM_DOCUMENTO_A -->

> Registro interno (não vai no documento A): honorários ajustados com o substabelecido — `{{honorarios_substabelecido}}`.

---

<!-- INICIO_DOCUMENTO_B -->

# SUBSTABELECIMENTO SEM RESERVA DE PODERES

Pelo presente instrumento, **{{substabelecente_nome}}**, advogado(a) inscrito(a) na {{substabelecente_oab}}, integrante de {{escritorio_razao_social}}, CNPJ nº {{escritorio_cnpj}}, com escritório em {{escritorio_endereco}}, na qualidade de procurador(a) de **{{cliente_nome}}**, **SUBSTABELECE, SEM RESERVA DE PODERES**, na pessoa de **{{substabelecido_nome}}**, advogado(a) inscrito(a) na {{substabelecido_oab}}{{#substabelecido_sociedade}}, integrante de {{substabelecido_sociedade}}{{/substabelecido_sociedade}}, com endereço profissional em {{substabelecido_endereco}}, endereço eletrônico {{substabelecido_email}}, todos os poderes que lhe foram conferidos pelo(a) outorgante nos autos do processo nº {{processo_numero}}, em trâmite perante {{processo_juizo}}, em que figura como parte contrária {{parte_contraria}}.

Declara o(a) substabelecente que o(a) cliente teve prévio e inequívoco conhecimento deste substabelecimento em {{ciencia_cliente_data}}, por {{ciencia_cliente_meio}}, nos termos do art. 26, § 1º, do Código de Ética e Disciplina da OAB.

Requer-se que, a partir da juntada deste instrumento, as intimações sejam publicadas exclusivamente em nome do(a) substabelecido(a), com a exclusão do nome do(a) substabelecente e dos demais advogados de {{escritorio_razao_social}} do cadastro do processo.

Ficam ressalvados os honorários contratuais e de sucumbência devidos ao(à) substabelecente e à sociedade de que faz parte, proporcionais ao trabalho realizado até esta data.

{{cidade_assinatura}}, {{data_assinatura}}.

&nbsp;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**{{substabelecente_nome}}**
{{substabelecente_oab}}

<!-- FIM_DOCUMENTO_B -->
