# 10 — Termo de recusa de serviço e assunção de responsabilidade (oficina mecânica)

> **Bloco de preenchimento e notas — não faz parte do documento.** O texto a ser gerado é apenas o que está entre
> os marcadores (comentários HTML) `INICIO_DOCUMENTO` e `FIM_DOCUMENTO`. Convenções: ver `README.md`.
>
> **Quem usa:** a oficina cliente do escritório, no balcão, quando o consumidor recusa (total ou parcialmente) um serviço
> ou a troca de peça recomendada. O escritório entrega este modelo já com os dados da oficina preenchidos.

## Para que serve e qual é o limite jurídico

1. **Função.** O termo é **prova**: demonstra que a oficina cumpriu o dever de informação clara sobre o risco (art. 6º, III, do CDC), que apresentou orçamento prévio (art. 40 do CDC) e que o consumidor, informado, escolheu não fazer o serviço. Se depois houver dano ligado ao defeito não reparado, o termo sustenta a excludente de **culpa exclusiva do consumidor** (art. 14, § 3º, II, do CDC).
2. **Limite.** O termo **não** isenta a oficina pelo serviço que ela **efetivamente executou**. Cláusula que exonere ou atenue a responsabilidade do fornecedor é nula (arts. 24, 25 e 51, I, do CDC). Por isso o texto diz expressamente que a garantia do serviço executado continua valendo — isso dá credibilidade ao documento perante PROCON e Judiciário.
3. **Qualidade da prova.** O termo vale o que valem os detalhes: queixa nas palavras do cliente, diagnóstico técnico com o método usado, consequência concreta, orçamento anexo, fotos/vídeo e assinatura. Termo genérico ("cliente ciente dos riscos") prova pouco.
4. **Item de segurança** (freios, direção, suspensão, pneus, sistema de arrefecimento com risco de incêndio etc.): marcar o campo de risco à segurança, recomendar por escrito que o veículo não circule e oferecer guincho. A oficina **não** pode reter o veículo para forçar o serviço.
5. **Recusa de assinatura.** Se o consumidor se recusar a assinar, a oficina preenche o quadro final com duas testemunhas e envia cópia do termo e do orçamento ao consumidor por WhatsApp ou e-mail, guardando o comprovante de envio.
6. **Contrato de adesão:** imprimir com **fonte não inferior a corpo 12** (art. 54, § 3º, do CDC).

## Campos

| Campo | O que é | De onde vem |
|---|---|---|
| `{{oficina_razao_social}}`, `{{oficina_nome_fantasia}}`, `{{oficina_cnpj}}`, `{{oficina_endereco}}`, `{{oficina_telefone}}` | Dados da oficina | Cadastro da oficina no escritório (fixos por cliente) |
| `{{os_numero}}`, `{{orcamento_numero}}`, `{{orcamento_data}}` | Ordem de serviço e orçamento | Sistema da oficina |
| `{{consumidor_nome}}`, `{{consumidor_cpf}}`, `{{consumidor_telefone}}`, `{{consumidor_email}}` | Consumidor | Ordem de serviço |
| `{{veiculo_marca_modelo}}`, `{{veiculo_ano}}`, `{{veiculo_placa}}`, `{{veiculo_chassi}}`, `{{veiculo_km}}` | Veículo | Documento do veículo / painel |
| `{{queixa_consumidor}}` | O que o cliente relatou, **com as palavras dele** | Ordem de serviço (recepção) |
| `{{diagnostico}}` | O que foi constatado e **como** (inspeção visual, scanner com código de falha, teste de rodagem, medição) | Mecânico responsável |
| `{{diagnostico_responsavel}}` | Nome e função do técnico | Oficina |
| `{{servico_recomendado}}` | Serviços e peças recomendados | Orçamento |
| `{{valor_orcamento}}` | Valor total do orçamento recusado (com extenso) | Orçamento |
| `{{consequencias}}` | Consequências e riscos concretos de não fazer (ex.: "desgaste das pastilhas até o metal; perda de eficiência de frenagem; dano aos discos") | Mecânico responsável |
| `{{risco_seguranca}}` | "SIM" ou "NÃO" | Mecânico responsável |
| `{{opcao_consumidor}}` | Marcar uma das opções do item 4 | Escolha do consumidor |
| `{{servico_executado}}` | Se houve execução parcial: o que foi feito | Ordem de serviço |
| `{{evidencias}}` | Fotos/vídeos/relatório de scanner anexados (descrição) | Oficina |
| `{{cidade}}`, `{{data}}`, `{{hora}}` | Local, data e hora | Emissão |
| `{{testemunha1_*}}`, `{{testemunha2_*}}` | Só se o consumidor recusar a assinatura | Funcionários ou terceiros presentes |

---

<!-- INICIO_DOCUMENTO -->

# TERMO DE RECUSA DE SERVIÇO E DE CIÊNCIA DE RISCOS

**Ordem de serviço nº** {{os_numero}} — **Orçamento nº** {{orcamento_numero}}, de {{orcamento_data}}

**FORNECEDOR:** {{oficina_razao_social}} ({{oficina_nome_fantasia}}), CNPJ nº {{oficina_cnpj}}, {{oficina_endereco}}, telefone {{oficina_telefone}}.

**CONSUMIDOR(A):** {{consumidor_nome}}, CPF nº {{consumidor_cpf}}, telefone {{consumidor_telefone}}, e-mail {{consumidor_email}}.

**VEÍCULO:** {{veiculo_marca_modelo}}, ano {{veiculo_ano}}, placa {{veiculo_placa}}, chassi {{veiculo_chassi}}, quilometragem na entrada: {{veiculo_km}} km.

## 1. Queixa apresentada pelo(a) consumidor(a)

{{queixa_consumidor}}

## 2. Diagnóstico técnico

{{diagnostico}}

Diagnóstico realizado por: {{diagnostico_responsavel}}.

Evidências anexas: {{evidencias}}.

## 3. Serviço recomendado, orçamento e consequências de não realizá-lo

**Serviço e peças recomendados:** {{servico_recomendado}}

**Valor do orçamento:** {{valor_orcamento}}, conforme orçamento nº {{orcamento_numero}}, que integra este termo.

**Consequências e riscos de não realizar o serviço recomendado:** {{consequencias}}

**O defeito constatado compromete a segurança do veículo?** {{risco_seguranca}}

> Se a resposta for SIM: o fornecedor recomenda que o veículo **não circule** até o reparo e oferece a remoção por guincho, às custas do(a) consumidor(a), até o local que este(a) indicar.

## 4. Decisão do(a) consumidor(a)

Depois de receber as informações acima, o(a) consumidor(a) decidiu (opção marcada): **{{opcao_consumidor}}**

- ( ) **Recusa total:** não autorizar nenhum dos serviços recomendados e retirar o veículo.
- ( ) **Execução parcial:** autorizar somente o seguinte serviço: {{servico_executado}}, e recusar os demais itens do orçamento.
- ( ) **Adiamento:** não realizar o serviço neste momento, ciente de que o orçamento vale por 10 (dez) dias (art. 40, § 1º, do CDC) e de que o defeito pode se agravar até lá.
- ( ) **Peça fornecida pelo(a) consumidor(a) ou peça não original:** autorizar a utilização de peça adquirida pelo(a) próprio(a) consumidor(a) ou de peça que não é original nem nova, ciente de que o fornecedor responde pela mão de obra, mas não pela qualidade, procedência ou adequação dessa peça (art. 21 do CDC).

## 5. Declaração do(a) consumidor(a)

Declaro que:

a) recebi do fornecedor, de forma clara e em linguagem que compreendi, as informações sobre o diagnóstico, o serviço recomendado, o orçamento e as consequências e riscos de não realizar o serviço, e tive a oportunidade de fazer perguntas;

b) a decisão registrada no item 4 foi tomada livremente por mim, sem qualquer pressão;

c) estou ciente de que os danos ao veículo, a mim ou a terceiros que decorrerem do defeito constatado e não reparado por minha decisão não poderão ser atribuídos ao fornecedor;

d) estou ciente de que este termo **não** afasta a responsabilidade do fornecedor pelos serviços que ele efetivamente executou, que continuam cobertos pela garantia legal e pela garantia contratual eventualmente oferecida; e

e) recebi uma via deste termo e do orçamento.

{{cidade}}, {{data}}, às {{hora}}.

&nbsp;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**CONSUMIDOR(A)** — {{consumidor_nome}} — CPF nº {{consumidor_cpf}}

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**FORNECEDOR** — {{oficina_nome_fantasia}} — responsável: {{diagnostico_responsavel}}

&nbsp;

**Registro de recusa de assinatura** (preencher somente se o(a) consumidor(a) se recusar a assinar)

Declaramos que presenciamos a explicação do diagnóstico, do orçamento e dos riscos ao(à) consumidor(a), que decidiu conforme o item 4 e se recusou a assinar este termo. Cópia do termo e do orçamento foi enviada ao(à) consumidor(a) em {{data}}, por \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.

1. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Nome: {{testemunha1_nome}} — CPF: {{testemunha1_cpf}}
2. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Nome: {{testemunha2_nome}} — CPF: {{testemunha2_cpf}}

<!-- FIM_DOCUMENTO -->
