# 12 — Notificação extrajudicial de cobrança (pré-execução / pré-monitória)

> **Bloco de preenchimento e notas — não faz parte do documento.** O texto a ser gerado é apenas o que está entre
> os marcadores (comentários HTML) `INICIO_DOCUMENTO` e `FIM_DOCUMENTO`. Convenções: ver `README.md`.

## Notas de uso

1. **Para que serve.** Constituir o devedor em mora quando a obrigação não tem termo certo (art. 397, parágrafo único, do Código Civil); documentar a tentativa de solução amigável; abrir canal de acordo antes da execução (título executivo — art. 784 do CPC) ou da monitória (prova escrita sem eficácia de título executivo — art. 700 do CPC). Cliente de assessoria: notificação e negociação estão **dentro** da mensalidade; a ação é contratada à parte (modelo 07).
2. **Prescrição.** A notificação extrajudicial **não interrompe** a prescrição. As hipóteses são as do art. 202 do Código Civil (interrupção uma única vez): entre elas, o protesto judicial (inciso II), o protesto cambial (inciso III) e o ato inequívoco, ainda que extrajudicial, de reconhecimento do direito pelo devedor (inciso VI). Conferir o prazo prescricional antes de enviar (ex.: 5 anos para dívida líquida constante de instrumento público ou particular — art. 206, § 5º, I) e, se estiver próximo do fim, ajuizar ou protestar em vez de notificar. Se o devedor responder reconhecendo a dívida, guardar a resposta: ela interrompe a prescrição.
3. **Atualização.** Se o contrato não previr índice e juros: atualização pelo **IPCA** (art. 389, parágrafo único, do Código Civil) e juros pela **taxa legal** (Selic deduzido o IPCA — art. 406, § 1º, do Código Civil), na redação da Lei nº 14.905/2024. Se o contrato previr, aplicar o contrato. Juntar planilha.
4. **Multa e honorários de cobrança.** Só cobrar multa e honorários advocatícios extrajudiciais se o **contrato** os previr. Em relação de consumo: multa de mora limitada a 2% (art. 52, § 1º, do CDC, nos contratos de fornecimento de crédito/financiamento) e cláusula que obrigue o consumidor a ressarcir custos de cobrança sem igual direito a ele é nula (art. 51, XII, do CDC).
5. **Tom.** Devedor consumidor não pode ser exposto a ridículo nem submetido a constrangimento ou ameaça (art. 42 do CDC). Mencionar as medidas cabíveis é lícito; ameaçar com medidas que não serão tomadas ou que não cabem, não. Enviar apenas ao devedor (nunca a familiares, empregador ou grupo), por respeito também à LGPD.
6. **Negativação.** Só mencionar inclusão em cadastro de inadimplentes se o credor for associado ao órgão e o fizer na forma da lei (a comunicação prévia ao consumidor do art. 43, § 2º, do CDC cabe ao órgão mantenedor). Por padrão, o bloco `{{#mencionar_negativacao}}` vem desligado.
7. **Envio.** Preferir meio com prova de entrega: carta com aviso de recebimento, e-mail com confirmação de leitura, WhatsApp com confirmação de leitura, ou notificação pelo Registro de Títulos e Documentos (art. 160 da Lei nº 6.015/1973). Guardar o comprovante na pasta do caso.
8. **Pagamento.** Por padrão, o pagamento é feito **diretamente ao credor**. Se for indicado recebimento em conta do escritório, a procuração deve ter poderes para receber e dar quitação e o escritório deve prestar contas.

## Campos

| Campo | O que é | De onde vem |
|---|---|---|
| `{{notificado_nome}}`, `{{notificado_documento}}`, `{{notificado_endereco}}` | Devedor (nome/razão social, CPF/CNPJ, endereço) | Documentos do crédito / pesquisa cadastral |
| `{{notificante_nome}}`, `{{notificante_documento}}`, `{{notificante_endereco}}` | Credor (cliente do escritório) | Ficha do cliente |
| `{{escritorio_*}}`, `{{advogado_responsavel_nome}}`, `{{advogado_responsavel_oab}}` | Escritório e advogado que assina | `README.md` |
| `{{origem_debito}}` | Descrição precisa: contrato, nota fiscal, cheque, duplicata, confissão de dívida — com número e data | Documentos do crédito |
| `{{tipo_documento}}` | "título executivo extrajudicial" (contrato assinado com 2 testemunhas ou por assinatura eletrônica com integridade conferida, cheque, nota promissória, duplicata aceita/protestada) **ou** "prova escrita" (orçamento aprovado, NF sem aceite, conversas) | Análise do advogado — define se a ação será execução ou monitória |
| `{{vencimento_original}}` | Data(s) de vencimento | Documentos do crédito |
| `{{valor_original}}` | Valor principal | Documentos do crédito |
| `{{criterio_atualizacao}}` | Ex.: "atualização monetária pelo IPCA e juros de mora pela taxa legal (arts. 389 e 406 do Código Civil)" ou o índice/juros do contrato | Contrato / nota 3 |
| `{{multa_contratual}}` | Bloco opcional: multa prevista no contrato (cláusula e percentual) | Contrato |
| `{{valor_atualizado}}`, `{{data_calculo}}` | Total atualizado e data-base | Planilha de cálculo (anexo) |
| `{{prazo_pagamento}}` | Prazo para pagamento. Sugestão: 10 (dez) dias corridos do recebimento | Decisão do advogado |
| `{{dados_pagamento}}` | Conta/Pix do credor ou "mediante boleto a ser enviado" | Cliente |
| `{{contato_acordo}}` | Canal para proposta de acordo | Escritório |
| `{{medida_judicial}}` | "ação de execução de título extrajudicial (art. 784 do CPC)" ou "ação monitória (art. 700 do CPC)" ou "ação de cobrança" | Análise do advogado |
| Blocos opcionais | `{{#multa}}`, `{{#mencionar_protesto}}`, `{{#mencionar_negativacao}}`, `{{#proposta_acordo}}` (com `{{condicoes_acordo}}`) | Decisão do advogado |
| `{{cidade_assinatura}}`, `{{data_assinatura}}` | — | Emissão |

---

<!-- INICIO_DOCUMENTO -->

# NOTIFICAÇÃO EXTRAJUDICIAL

**NOTIFICANTE:** {{notificante_nome}}, inscrito(a) no CPF/CNPJ sob o nº {{notificante_documento}}, com endereço em {{notificante_endereco}}, por seus advogados ao final assinados.

**NOTIFICADO(A):** {{notificado_nome}}, inscrito(a) no CPF/CNPJ sob o nº {{notificado_documento}}, com endereço em {{notificado_endereco}}.

Prezado(a) Senhor(a),

**{{notificante_nome}}**, por intermédio de seus advogados, vem, pela presente, **NOTIFICÁ-LO(A)** extrajudicialmente nos termos seguintes.

**1. Do débito.** O(A) Notificado(a) é devedor(a) do(a) Notificante da quantia de **{{valor_original}}**, decorrente de {{origem_debito}}, com vencimento em {{vencimento_original}}, que não foi paga até a presente data, apesar de exigível.

**2. Do valor atualizado.** Aplicando-se {{criterio_atualizacao}}{{#multa}}, acrescida da multa prevista em {{multa_contratual}}{{/multa}}, o débito totaliza **{{valor_atualizado}}**, calculado até {{data_calculo}}, conforme demonstrativo anexo.

**3. Do prazo para pagamento.** Fica o(a) Notificado(a) **constituído(a) em mora** e notificado(a) para, no prazo de **{{prazo_pagamento}}** contados do recebimento desta, efetuar o pagamento do valor indicado, atualizado até a data do efetivo pagamento, por meio de {{dados_pagamento}}, encaminhando o comprovante pelo contato {{contato_acordo}}.

**4. Das medidas cabíveis.** Decorrido o prazo sem o pagamento ou sem a celebração de acordo, o(a) Notificante adotará as medidas judiciais cabíveis para a satisfação do seu crédito, em especial {{medida_judicial}}, com o acréscimo das custas processuais e dos honorários advocatícios fixados pelo juízo{{#mencionar_protesto}}, podendo ainda levar o título ou documento de dívida a protesto, nos termos da Lei nº 9.492/1997{{/mencionar_protesto}}{{#mencionar_negativacao}}, e requerer a inclusão do débito em cadastro de proteção ao crédito, na forma da lei{{/mencionar_negativacao}}.

{{#proposta_acordo}}**5. Da possibilidade de acordo.** Com o objetivo de solucionar a questão de forma amigável, o(a) Notificante admite receber o débito nas seguintes condições, válidas somente dentro do prazo do item 3: {{condicoes_acordo}}. Propostas diversas poderão ser apresentadas pelo mesmo contato e serão analisadas.{{/proposta_acordo}}

Caso o pagamento já tenha sido efetuado, solicita-se o envio do comprovante, desconsiderando-se esta notificação.

Esta notificação é feita para os fins dos arts. 394 e 397 do Código Civil, servindo como prova da ciência inequívoca do débito e da oportunidade de pagamento amigável.

{{cidade_assinatura}}, {{data_assinatura}}.

&nbsp;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**{{advogado_responsavel_nome}}**
{{advogado_responsavel_oab}}
{{escritorio_razao_social}} — {{escritorio_email}}

Anexo: demonstrativo de cálculo do débito; cópia de {{origem_debito}}.

<!-- FIM_DOCUMENTO -->
