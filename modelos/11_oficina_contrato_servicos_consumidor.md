# 11 — Contrato de prestação de serviços de reparação de veículo (oficina x consumidor) e termo de garantia

> **Bloco de preenchimento e notas — não faz parte do documento.** O texto a ser gerado é apenas o que está entre
> os marcadores (comentários HTML) `INICIO_DOCUMENTO` e `FIM_DOCUMENTO`. Convenções: ver `README.md`.
>
> **Quem usa:** a oficina cliente do escritório, como condições gerais impressas no verso ou anexas à ordem de serviço.
> O escritório personaliza uma vez por oficina (dados, garantia contratual, estadia) e a oficina usa em todo atendimento.

## Notas para o escritório

1. **É contrato de adesão** (art. 54 do CDC): redação clara, **fonte não inferior a corpo 12** (§ 3º) e **cláusulas que limitam direitos em destaque** (§ 4º) — neste modelo, as cláusulas em negrito marcadas com "DESTAQUE" devem sair em negrito ou caixa no documento final.
2. **Orçamento prévio e autorização expressa.** Executar serviço sem orçamento prévio e autorização expressa é prática abusiva (art. 39, VI, do CDC). O orçamento deve discriminar mão de obra, materiais e equipamentos, condições de pagamento e datas de início e término; vale 10 dias salvo estipulação em contrário; aprovado, obriga as partes; e o consumidor não responde por acréscimos de serviços de terceiros não previstos (art. 40, §§ 1º a 3º). Serviço adicional descoberto durante o reparo exige **nova autorização**.
3. **Peças.** Presume-se o uso de peças originais novas ou que mantenham as especificações do fabricante; outra situação exige autorização do consumidor (art. 21 do CDC).
4. **Garantia legal x contratual.** A garantia legal independe de termo e não pode ser afastada (art. 24); o prazo para reclamar de vício aparente em serviço de bem durável é de **90 dias** a partir do término do serviço (art. 26, II, e § 1º); vício oculto conta da constatação (art. 26, § 3º). A garantia contratual é **complementar** à legal e deve ser dada por termo escrito com conteúdo mínimo (art. 50 e parágrafo único). `[CONFERIR]` entendimento atual do STJ sobre a contagem do prazo legal após o término da garantia contratual — o modelo foi redigido para não depender dessa questão (a contratual "não reduz nem substitui" a legal).
5. **Exclusões** só valem para a garantia **contratual**; para a legal, só as excludentes do próprio CDC (art. 14, § 3º).
6. **Retenção do veículo até o pagamento** `[CONFERIR]`: o modelo condiciona a entrega ao pagamento com base na exceção do contrato não cumprido (art. 476 do Código Civil), mas há divergência em PROCONs e tribunais sobre a retenção de veículo pela oficina. Conferir a jurisprudência do TJMA/TJGO e do TJTO antes de entregar às oficinas; a alternativa conservadora é retirar o item 7.2.
7. **Devolução das peças substituídas** `[CONFERIR]` se há lei estadual ou municipal no MA, PA, TO ou GO que obrigue a oficina a devolver as peças trocadas. O modelo prevê a devolução a pedido do consumidor, que é boa prática de qualquer forma.
8. **Estadia (guarda após o aviso de conclusão)**: só pode ser cobrada se prevista e informada antes e em valor razoável; valores excessivos podem ser considerados abusivos (art. 51, IV, do CDC).

## Campos

| Campo | O que é | De onde vem |
|---|---|---|
| `{{oficina_razao_social}}`, `{{oficina_nome_fantasia}}`, `{{oficina_cnpj}}`, `{{oficina_endereco}}`, `{{oficina_telefone}}`, `{{oficina_email}}` | Dados da oficina | Cadastro da oficina (fixo) |
| `{{oficina_horario}}` | Horário de funcionamento | Oficina (fixo) |
| `{{valor_diagnostico}}` | Valor cobrado pelo diagnóstico, se o orçamento não for aprovado, ou "sem custo" | Política da oficina (fixo) |
| `{{garantia_contratual_mao_obra}}` | Prazo da garantia contratual da mão de obra (ex.: "90 (noventa) dias ou 5.000 km, o que ocorrer primeiro, contados após o término da garantia legal") | Política da oficina (fixo) |
| `{{garantia_contratual_pecas}}` | Garantia das peças fornecidas pela oficina (ex.: "a garantia oferecida pelo fabricante da peça, nunca inferior à garantia legal") | Política da oficina (fixo) |
| `{{prazo_retirada}}` | Dias para retirada após o aviso de conclusão sem cobrança de estadia. Sugestão: 3 (três) dias úteis | Política da oficina (fixo) |
| `{{valor_estadia}}` | Diária de guarda após o prazo de retirada | Política da oficina (fixo) — valor razoável |
| `{{os_numero}}`, `{{consumidor_*}}`, `{{veiculo_*}}` | Ordem de serviço, consumidor e veículo | Ordem de serviço |
| `{{vistoria_entrada}}` | Estado do veículo na entrada: avarias, combustível, pertences, fotos | Checklist de recepção |
| `{{cidade}}`, `{{data}}` | Local e data | Emissão |

---

<!-- INICIO_DOCUMENTO -->

# CONDIÇÕES GERAIS DE PRESTAÇÃO DE SERVIÇOS DE REPARAÇÃO E MANUTENÇÃO DE VEÍCULO

**Ordem de serviço nº** {{os_numero}}

**FORNECEDOR:** {{oficina_razao_social}} ({{oficina_nome_fantasia}}), CNPJ nº {{oficina_cnpj}}, {{oficina_endereco}}, telefone {{oficina_telefone}}, e-mail {{oficina_email}}, horário de funcionamento: {{oficina_horario}}.

**CONSUMIDOR(A):** {{consumidor_nome}}, CPF nº {{consumidor_cpf}}, telefone {{consumidor_telefone}}, e-mail {{consumidor_email}}.

**VEÍCULO:** {{veiculo_marca_modelo}}, ano {{veiculo_ano}}, placa {{veiculo_placa}}, chassi {{veiculo_chassi}}, quilometragem na entrada: {{veiculo_km}} km.

## 1. Recebimento do veículo e vistoria de entrada

1.1. O veículo é recebido mediante vistoria de entrada, que registra avarias aparentes, nível de combustível, acessórios e objetos deixados no veículo: {{vistoria_entrada}}.

1.2. Recomenda-se que o(a) consumidor(a) retire do veículo objetos pessoais e de valor. Objetos não registrados na vistoria de entrada não poderão ser conferidos na devolução.

1.3. Enquanto estiver sob a guarda do fornecedor, o veículo será conservado com o cuidado e a diligência devidos, respondendo o fornecedor pelos danos que nele ocorrerem nesse período.

## 2. Diagnóstico e orçamento prévio

2.1. Nenhum serviço será executado sem **orçamento prévio por escrito e autorização expressa** do(a) consumidor(a) (arts. 39, VI, e 40 do Código de Defesa do Consumidor).

2.2. O orçamento discriminará a mão de obra, as peças e os materiais, os equipamentos utilizados, as condições de pagamento e as datas previstas de início e de término, e terá validade de 10 (dez) dias a contar do seu recebimento pelo(a) consumidor(a).

2.3. **DESTAQUE —** O diagnóstico necessário para elaborar o orçamento custa {{valor_diagnostico}}, valor que será cobrado apenas se o orçamento não for aprovado e que foi informado ao(à) consumidor(a) antes do início do diagnóstico.

2.4. A autorização poderá ser dada por assinatura no orçamento ou por mensagem escrita (WhatsApp ou e-mail) enviada pelo telefone ou endereço eletrônico indicados nesta ordem de serviço.

2.5. Aprovado o orçamento, os valores não serão alterados sem nova concordância do(a) consumidor(a). Se, durante a execução, for constatada a necessidade de serviço ou peça não previstos, o fornecedor interromperá o item afetado e apresentará orçamento complementar, que dependerá de nova autorização expressa.

## 3. Peças

3.1. Serão empregadas peças de reposição originais novas ou que mantenham as especificações técnicas do fabricante. O uso de peça diversa dependerá de autorização expressa do(a) consumidor(a), registrada no orçamento (art. 21 do Código de Defesa do Consumidor).

3.2. **DESTAQUE —** Se o(a) consumidor(a) fornecer peças por conta própria, o fornecedor responderá pela mão de obra de instalação, mas não pela qualidade, procedência ou adequação da peça fornecida, e poderá recusar-se a instalá-la se constatar que ela é incompatível ou compromete a segurança.

3.3. As peças substituídas serão devolvidas ao(à) consumidor(a), se ele(a) assim solicitar até a entrega do veículo, salvo as que, por exigência legal ou do fabricante, devam ser entregues para descarte ou como base de troca, informação que constará do orçamento.

## 4. Testes

4.1. O(A) consumidor(a) autoriza a realização de testes de rodagem necessários ao diagnóstico e à verificação do serviço, feitos por profissional habilitado do fornecedor, que responde por eventuais danos ocorridos durante o teste.

## 5. Prazo de execução

5.1. O serviço será concluído no prazo indicado no orçamento aprovado. Atrasos decorrentes de falta de peças no mercado ou de serviço complementar serão comunicados ao(à) consumidor(a) assim que conhecidos, com a nova previsão.

## 6. Recusa de serviço recomendado

6.1. Se o(a) consumidor(a) recusar, no todo ou em parte, serviço recomendado pelo fornecedor, a recusa será registrada em **termo de recusa de serviço e ciência de riscos**, que integra esta ordem de serviço.

## 7. Pagamento e entrega do veículo

7.1. O pagamento será feito na entrega do veículo, na forma ajustada no orçamento.

7.2. **DESTAQUE —** A entrega do veículo ocorrerá mediante o pagamento ou a formalização da forma de pagamento ajustada.

7.3. Concluído o serviço, o fornecedor comunicará o(a) consumidor(a) pelo telefone ou e-mail informados. **DESTAQUE —** Se o veículo não for retirado em {{prazo_retirada}} a contar da comunicação, será cobrada estadia de {{valor_estadia}} por dia, a título de guarda.

## 8. Garantia

8.1. **Garantia legal.** Os serviços executados e as peças fornecidas pelo fornecedor têm a garantia legal do Código de Defesa do Consumidor, que independe deste termo e não pode ser excluída. O(A) consumidor(a) pode reclamar de vício aparente no prazo de 90 (noventa) dias contados do término do serviço; em caso de vício oculto, o prazo conta do momento em que o defeito ficar evidenciado (art. 26, II, §§ 1º e 3º, do Código de Defesa do Consumidor). Constatado o vício, o(a) consumidor(a) poderá exigir a reexecução do serviço sem custo, a restituição da quantia paga ou o abatimento proporcional do preço (art. 20 do Código de Defesa do Consumidor).

8.2. **Garantia contratual.** Além da garantia legal, e sem reduzi-la ou substituí-la, o fornecedor oferece:

a) para a mão de obra: {{garantia_contratual_mao_obra}}; e

b) para as peças por ele fornecidas: {{garantia_contratual_pecas}}.

8.3. **DESTAQUE —** A garantia contratual do item 8.2 não cobre: (i) desgaste natural decorrente do uso; (ii) danos causados por acidente, mau uso, uso em competição, sobrecarga ou desrespeito às recomendações do fabricante ou do fornecedor; (iii) intervenção de terceiros nos componentes reparados; (iv) peças fornecidas pelo(a) consumidor(a), quanto à própria peça; e (v) defeitos em componentes não abrangidos pelo serviço executado. Essas exclusões não se aplicam à garantia legal do item 8.1.

8.4. Para exercer a garantia, o(a) consumidor(a) deverá apresentar o veículo no estabelecimento do fornecedor com esta ordem de serviço ou a nota fiscal, no horário de funcionamento. Em caso de impossibilidade de deslocamento por defeito coberto pela garantia, o fornecedor orientará sobre a remoção.

## 9. Proteção de dados

9.1. Os dados pessoais do(a) consumidor(a) serão utilizados para a execução do serviço, a emissão de documentos fiscais, a comunicação sobre o veículo e a garantia, e o cumprimento de obrigações legais (art. 7º, II e V, da Lei nº 13.709/2018). O envio de ofertas e lembretes de manutenção dependerá de consentimento específico, revogável a qualquer tempo: ( ) autorizo ( ) não autorizo.

## 10. Disposições finais

10.1. Reclamações podem ser apresentadas pelo telefone {{oficina_telefone}} ou pelo e-mail {{oficina_email}}. A reclamação comprovadamente formulada obsta a decadência até a resposta negativa do fornecedor (art. 26, § 2º, I, do Código de Defesa do Consumidor).

10.2. Fica assegurado ao(à) consumidor(a) o foro do seu domicílio (art. 101, I, do Código de Defesa do Consumidor).

Declaro que li estas condições gerais, que recebi uma via e que as cláusulas em destaque me foram explicadas.

{{cidade}}, {{data}}.

&nbsp;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**CONSUMIDOR(A)** — {{consumidor_nome}} — CPF nº {{consumidor_cpf}}

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**FORNECEDOR** — {{oficina_nome_fantasia}}

<!-- FIM_DOCUMENTO -->
