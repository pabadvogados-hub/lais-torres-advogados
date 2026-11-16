# POP-OP-04 — Ações de execução, cobrança e monitória

Versão 1 — 16/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Larissa (cível) |
| **Quem executa** | Estagiários do cível; IA monta a minuta; Dra. Larissa revisa e assina |
| **Gatilho** | Cliente de assessoria passa um devedor para cobrar (POP-ATD-01, demanda nova) |
| **Termina quando** | Ação distribuída, custas recolhidas, citação acompanhada e próximos atos no ADVBOX |
| **Prazo interno** | Escolha da via em 2 dias úteis após os documentos completos; petição inicial protocolada em até 5 dias úteis após os documentos |

## Objetivo

É a demanda judicial mais repetitiva do escritório: o cliente passa o devedor e o escritório
judicializa. Por ser repetitiva, tem modelo, checklist e prazo. O ponto que mais exige atenção é a
**escolha da via certa** (execução, monitória ou cobrança) e a **prescrição**.

## Automação x pessoa

| A automação / IA faz | A pessoa faz |
|---|---|
| Cobra do cliente os documentos do `CK-DIA-01` (MSG-02) | Confere se o título e os documentos estão completos e legíveis |
| Sugere a via cabível e confere a prescrição pelas datas | Dra. Larissa confirma a via e a prescrição |
| Calcula o débito atualizado pelos critérios informados | Confere índices, juros e multa do contrato |
| Monta a minuta da inicial no modelo do escritório | Revisa (POP-OP-05) e protocola |
| Cria as tarefas e prazos no ADVBOX | Acompanha citação, pesquisas de bens e penhora |

## Passo a passo

1. **Receber a demanda e cobrar os documentos** do `CK-DIA-01`. — *D0; cadência da MSG-02*
2. **Conferir a prescrição** antes de qualquer outra coisa. Se estiver perto de prescrever,
   **avisar a Dra. Larissa no mesmo dia**: a ação precisa ser distribuída antes. — *D0 ou no dia dos documentos*

   | Documento | Prazo de prescrição (referência) | Base legal |
   |---|---|---|
   | Cheque (execução) | 6 meses após o fim do prazo de apresentação (30 dias mesma praça; 60 dias outra praça) | Lei 7.357/1985, arts. 33 e 59 |
   | Cheque sem força executiva (monitória) | 5 anos a partir do dia seguinte à data de emissão | Súmula 503 do STJ |
   | Nota promissória (execução) | 3 anos do vencimento | Decreto 57.663/1966 (LUG), art. 70 |
   | Nota promissória sem força executiva (monitória) | 5 anos a partir do dia seguinte ao vencimento | Súmula 504 do STJ |
   | Duplicata contra o sacado | 3 anos do vencimento | Lei 5.474/1968, art. 18, I |
   | Dívida líquida em instrumento público ou particular (contrato, confissão de dívida) | 5 anos | Código Civil, art. 206, § 5º, I |
   | Outros casos | Advogado(a) confere | Código Civil, arts. 205 e 206 |

   Tabela de referência: a Dra. Larissa confere a prescrição de cada caso.

3. **Escolher a via** (Dra. Larissa confirma). — *até 2 dias úteis após documentos completos*

   | O cliente tem | Via | Base legal |
   |---|---|---|
   | **Título executivo extrajudicial**: cheque, nota promissória, duplicata aceita (ou protestada com comprovante de entrega), contrato ou confissão de dívida assinado pelo devedor e por 2 testemunhas, documento assinado eletronicamente nos termos da lei, entre outros | **Execução de título extrajudicial** | CPC, arts. 784 e 824 e seguintes; Lei 5.474/1968, art. 15 |
   | **Prova escrita sem força de título**: contrato sem testemunhas, orçamento aprovado, nota fiscal com canhoto, conversas e e-mails reconhecendo a dívida, cheque ou nota promissória prescritos | **Ação monitória** | CPC, art. 700 |
   | **Sem prova escrita suficiente**, ou dívida que depende de provar o serviço prestado | **Ação de cobrança** (procedimento comum) | CPC, art. 318 |
   | Valor até 40 salários mínimos e o cliente é microempresa, EPP ou pessoa física | Avaliar **Juizado Especial Cível** (sem custas no 1º grau) | Lei 9.099/1995, arts. 3º, 8º, § 1º, e 54 |

   Título executivo assinado eletronicamente: o CPC admite qualquer modalidade de assinatura
   eletrônica prevista em lei, dispensando as testemunhas quando a integridade for conferida pelo
   provedor de assinatura (CPC, art. 784, § 4º) **(conferir no caso concreto)**.

4. **Avaliar a cobrança extrajudicial antes da ação**, quando o cliente quiser ou quando for mais
   barato: notificação extrajudicial (modelo do escritório), protesto do título (Lei 9.492/1997) e
   negativação. Combinar com o cliente o prazo da notificação (sugestão: 5 dias úteis). — *opcional*
5. **Calcular o débito atualizado** pelos critérios do contrato (índice, juros, multa). Sem índice
   ou juros no contrato: correção pelo IPCA e juros pela taxa legal (Código Civil, arts. 389,
   parágrafo único, e 406, na redação da Lei 14.905/2024) **(conferir)**. Salvar a planilha. — *junto com a minuta*
6. **Pesquisar o endereço do devedor** e, se o cliente souber, bens (veículos, imóveis, contas,
   empresa). Execução: pedir já na inicial as pesquisas e bloqueios (SISBAJUD, RENAJUD, INFOJUD;
   CPC, art. 854) quando cabível, e a certidão para averbação premonitória (CPC, art. 828). — *junto com a minuta*
7. **Montar a minuta** no modelo do escritório (IA) — *até 3 dias úteis após a escolha da via*
   - Execução: citação para pagar em **3 dias** (CPC, art. 829); honorários de 10%, reduzidos pela
     metade se pagar no prazo (CPC, art. 827, § 1º); possibilidade de parcelamento pelo devedor (CPC, art. 916).
   - Monitória: mandado de pagamento em **15 dias**, com honorários de 5% (CPC, art. 701); se o
     devedor não pagar nem embargar, constitui-se o título executivo judicial (art. 701, § 2º).
   - Cobrança: pedido de condenação com os juros e a correção do item 5.
8. **Correção** pelo POP-OP-05 e assinatura da Dra. Larissa. — *1 dia útil*
9. **Custas iniciais**: gerar a guia e enviar ao cliente antes da distribuição, ou recolher em até
   15 dias após a intimação, sob pena de cancelamento da distribuição (CPC, art. 290). Ver POP-OP-01. — *antes do protocolo*
10. **Protocolar** e salvar o protocolo no Drive. Avisar o cliente com o número do processo. — *até 5 dias úteis após documentos completos*
11. **Acompanhar** (controladoria, POP-OP-02):
    - citação positiva ou negativa (se negativa, novo endereço ou pesquisa em 5 dias úteis);
    - prazo do devedor: embargos à execução em 15 dias (CPC, art. 915); embargos monitórios em 15 dias (CPC, art. 702);
    - resultado das pesquisas e bloqueios; penhora; acordo proposto pelo devedor (sempre levar ao cliente, por escrito).

## O que vira tarefa no ADVBOX

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[COBRANÇA] Cobrar documentos - {{cliente}} x {{devedor}}` | Atendimento | Cadência MSG-02 |
| `[COBRANÇA] Conferir prescrição e escolher via - {{cliente}} x {{devedor}}` | Dra. Larissa | 2 dias úteis após documentos |
| `[COBRANÇA] Minuta da inicial - {{cliente}} x {{devedor}}` | Estagiário(a) do cível | 3 dias úteis após a via |
| `[CUSTAS] Custas iniciais - {{cliente}} x {{devedor}}` | Camila | Antes do protocolo |
| `[COBRANÇA] Protocolar - {{cliente}} x {{devedor}}` | Dra. Larissa | 5 dias úteis após documentos |
| `[COBRANÇA] Conferir citação - {{processo}}` | Camila | 30 dias após o protocolo e a cada 15 dias |

## Onde salva no Drive

`CLIENTES/{{cliente}}/02_JUDICIAL/{{nº do processo}} - {{devedor}} - {{EXECUÇÃO | MONITÓRIA | COBRANÇA}}/`
Antes da distribuição (ainda sem número): `CLIENTES/{{cliente}}/03_EXTRAJUDICIAL/AAAA-MM-DD - Cobrança {{devedor}}/`;
depois de distribuída, mover para `02_JUDICIAL` com o número.

## Pendências `[A CONFIRMAR]`
- Modelos do escritório de execução, monitória, cobrança e notificação extrajudicial (Módulo 5, a partir das peças reais).
- Política de custas: o cliente paga antes da distribuição ou o escritório adianta?
- Itens marcados **(conferir)**.
