# POP-OP-02 — Controladoria: leitura e classificação de intimações

Versão 1 — 16/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Laís |
| **Quem executa** | Camila (controladoria); advogado(a) da área confirma a classificação de decisões e sentenças |
| **Gatilho** | Todo dia útil, às 8h; e qualquer intimação recebida fora dessa rotina (e-mail, PJe, cliente) |
| **Termina quando** | Toda intimação do dia classificada, com tarefa e prazo no ADVBOX e responsável avisado |
| **Prazo** | Leitura e classificação até 11h; tarefas criadas até 12h do mesmo dia útil |

## Objetivo

Nenhum prazo perdido e nenhuma dúvida sem critério. A dúvida que mais se repete na controladoria
é: **"essa decisão é caso de embargos, de agravo ou de apelação?"**. Este POP responde com uma
árvore de decisão e com os prazos da lei. Na dúvida, a regra é sempre a mesma: **tratar como
decisão e perguntar ao advogado(a) da área no mesmo dia**.

## Automação x pessoa

| O agente de controladoria faz (Módulo 6) | A Camila faz |
|---|---|
| Lê as publicações das OABs do escritório e as intimações do ADVBOX | Confere se todas as publicações do dia foram lidas (nenhuma "sobrando") |
| Sugere a classificação, o prazo fatal e o prazo interno | Confere a classificação e a contagem do prazo |
| Cria a tarefa no ADVBOX com o prazo | Confere responsável e data da tarefa |
| Quando cabe peça, traz a minuta pronta | Encaminha a minuta ao responsável da área (POP-OP-05) |
| Monta o relatório do dia | Envia o relatório aos advogados até 12h |

O agente **sugere**; quem decide a classificação de decisão, sentença e acórdão é o advogado(a) da área.

## Passo a passo da rotina diária

1. **Levantar as intimações do dia** (8h): ADVBOX (publicações), Domicílio/DJEN, painel do PJe e
   dos sistemas dos tribunais, e-mail do escritório. Conferir as OABs: Laís (GO 62.226), Alex
   `[A CONFIRMAR nº OAB/MA]`, Larissa `[A CONFIRMAR]`, Jaqueline `[A CONFIRMAR]`. — *até 9h*
2. **Para cada intimação, ler a íntegra** do ato (não só o resumo da publicação). — *até 11h*
3. **Classificar** usando a tabela do item "Classificação" e a árvore de decisão. — *até 11h*
4. **Contar o prazo** (item "Como contar o prazo"). Anotar o prazo fatal e o prazo interno. — *até 11h*
5. **Criar a tarefa no ADVBOX** com tipo, responsável, prazo interno e prazo fatal. Salvar o ato
   em PDF no Drive (`03_DECISOES_E_INTIMACOES`). — *até 12h*
6. **Decisão, sentença ou acórdão**: mandar ao advogado(a) da área no mesmo dia, com a classificação
   sugerida, e esperar a confirmação. Se não houver resposta até as 16h, ligar. — *mesmo dia*
7. **Avisar o cliente** quando a intimação mudar algo para ele (audiência, sentença, custas, pedido
   de documento), pelo atendimento (POP-ATD-01). — *até 1 dia útil*
8. **Enviar o relatório do dia** aos advogados: o que chegou, o que é prazo, o que vence nos
   próximos 5 dias úteis. — *até 12h*
9. **Fechamento do dia** (17h): conferir no ADVBOX as tarefas que vencem amanhã e cobrar quem estiver atrasado.

## Classificação

| Classe | Como reconhecer | O que fazer |
|---|---|---|
| **Mero andamento** | Juntada, conclusão, remessa, vista sem prazo, "aguarde-se", despacho que só impulsiona o processo (de mero expediente, sem conteúdo decisório; irrecorrível: CPC, art. 1.001) | Registrar no ADVBOX como andamento. Sem tarefa, salvo se o despacho mandar a parte fazer algo |
| **Intimação para agir** | "Manifeste-se", "junte", "especifique provas", "apresente cálculos", "réplica" | Tarefa com o prazo do despacho. Se o despacho não fixar prazo: 5 dias (CPC, art. 218, § 3º) **(conferir na Justiça do Trabalho)** |
| **Custas** | "Recolha as custas", "preparo", "diligência" | POP-OP-01 |
| **Audiência ou perícia** | Designação de data | Agenda + tarefa de preparo (POP-OP-03 no trabalhista) |
| **Citação / notificação inicial** | Cliente é réu ou reclamado em ação nova | Contestação: cível 15 dias úteis (CPC, art. 335); trabalhista até a audiência (CLT, arts. 841 e 847) |
| **Decisão** | Decide algo no meio do processo (tutela, gratuidade, prova, penhora, desconsideração) | Árvore de decisão (abaixo) + advogado(a) confirma |
| **Sentença** | Encerra a fase de conhecimento ou a execução (CPC, art. 203, § 1º) | Árvore de decisão + advogado(a) confirma |
| **Acórdão / decisão de relator** | Julgamento no tribunal | Advogado(a) avalia o recurso cabível (tabela de prazos) |

## Árvore de decisão: embargos, agravo, apelação ou outro recurso

Responder às perguntas na ordem:

1. **A decisão tem omissão, contradição, obscuridade ou erro material?**
   Sim → **embargos de declaração** (5 dias úteis). Os embargos **interrompem** o prazo dos outros
   recursos (CPC, arts. 1.022, 1.023 e 1.026; CLT, art. 897-A; Lei 9.099/1995, arts. 48 a 50).
   Atenção: embargos sem esses vícios, só para "rediscutir", podem ser considerados protelatórios e gerar multa (CPC, art. 1.026, § 2º).
   Se a decisão também prejudica o cliente no mérito, o advogado(a) decide se embarga primeiro ou recorre direto.

2. **É sentença?**
   - Justiça comum (cível): **apelação**, 15 dias úteis (CPC, arts. 1.003, § 5º, e 1.009).
   - Justiça do Trabalho: **recurso ordinário**, 8 dias úteis (CLT, art. 895; Lei 5.584/1970, art. 6º).
   - Juizado Especial Cível: **recurso inominado**, 10 dias (Lei 9.099/1995, art. 42), contados em dias úteis (Lei 9.099/1995, art. 12-A).

3. **É decisão interlocutória (no meio do processo)?**
   - **Cível**: está no rol do CPC, art. 1.015 (tutela provisória; mérito do processo; convenção de
     arbitragem; desconsideração da personalidade jurídica; gratuidade negada ou revogada; exibição
     de documento; exclusão de litisconsorte; limitação do litisconsórcio; intervenção de terceiros;
     efeito suspensivo em embargos à execução; redistribuição do ônus da prova; outros casos da lei)
     **ou** é decisão em liquidação, cumprimento de sentença, execução ou inventário (art. 1.015, parágrafo único)?
     Sim → **agravo de instrumento**, 15 dias úteis (CPC, arts. 1.003, § 5º, e 1.015).
     Não, mas há **urgência** (esperar a apelação tornaria a discussão inútil) → advogado(a) avalia
     agravo pela taxatividade mitigada (STJ, Tema 988).
     Não → **não cabe recurso agora**: registrar no ADVBOX "impugnar em preliminar de apelação" (CPC, art. 1.009, § 1º).
   - **Trabalhista**: em regra **não cabe recurso imediato** contra decisão interlocutória (CLT, art.
     893, § 1º; Súmula 214 do TST, que traz as exceções). Registrar e avisar o advogado(a): a nulidade
     deve ser alegada na primeira vez que a parte falar nos autos (CLT, art. 795). Contra decisão
     ilegal com dano imediato, o advogado(a) avalia mandado de segurança.
   - **Juizado Especial**: em regra não cabe recurso contra interlocutória **(conferir)**; advogado(a) avalia.

4. **É decisão na execução trabalhista?** → **agravo de petição**, 8 dias úteis (CLT, art. 897, "a").
   Cálculos de liquidação com vista às partes → impugnação fundamentada em 8 dias, prazo comum (CLT, art. 879, § 2º).
   Embargos à execução trabalhista → 5 dias após a garantia do juízo (CLT, art. 884).

5. **É acórdão ou decisão de relator?** → advogado(a) decide. Tabela de prazos abaixo.

## Tabela de prazos

| Peça | Cível (CPC) | Trabalhista (CLT) |
|---|---|---|
| Embargos de declaração | 5 dias úteis (art. 1.023) | 5 dias úteis (art. 897-A) |
| Apelação / recurso ordinário | 15 dias úteis (arts. 1.003, § 5º, e 1.009) | 8 dias úteis (art. 895) |
| Agravo de instrumento | 15 dias úteis (art. 1.015) | 8 dias úteis, só para destrancar recurso (art. 897, "b") |
| Agravo interno (decisão de relator) | 15 dias úteis (arts. 1.003, § 5º, e 1.021) | 8 dias úteis **(conferir)** |
| Recurso especial / extraordinário | 15 dias úteis (arts. 1.003, § 5º, 1.029) | Recurso de revista: 8 dias úteis (art. 896) |
| Contrarrazões | 15 dias úteis (arts. 1.003, § 5º, e 1.010, § 1º) | 8 dias úteis (art. 900) |
| Contestação | 15 dias úteis (art. 335) | Até a audiência (art. 847) |
| Réplica | 15 dias úteis (arts. 350 e 351) | Prazo fixado pelo juiz |
| Embargos à execução | 15 dias úteis (art. 915) | 5 dias após garantia (art. 884) |
| Impugnação ao cumprimento de sentença | 15 dias úteis após o prazo de pagamento voluntário (art. 525) | — |
| Manifestação sem prazo fixado | 5 dias (art. 218, § 3º) | Conferir com o advogado(a) |

Juizado Especial Cível: recurso inominado 10 dias; embargos de declaração 5 dias (Lei 9.099/1995, arts. 42 e 49), em dias úteis (art. 12-A).

## Como contar o prazo

1. **Dias úteis** no cível e no trabalhista (CPC, art. 219; CLT, art. 775).
2. **Exclui o dia do começo e inclui o do vencimento** (CPC, art. 224; CLT, art. 775).
3. **Diário eletrônico (DJEN)**: considera-se publicada no **primeiro dia útil seguinte à
   disponibilização**; o prazo começa no **primeiro dia útil seguinte à publicação** (CPC, art. 224,
   §§ 2º e 3º; Lei 11.419/2006, art. 4º, §§ 3º e 4º).
4. **Intimação pelo sistema (portal)**: considera-se feita no dia da consulta; sem consulta,
   10 dias corridos após o envio (Lei 11.419/2006, art. 5º, § 3º).
5. **Mesma intimação pelo DJEN e pelo portal**: há regra específica e mudanças recentes na
   jurisprudência e nas normas do CNJ. **Contar pela data mais antiga** e o advogado(a) confere `(conferir)`.
6. **Feriados e suspensões**: conferir o calendário do tribunal e os feriados municipais (Imperatriz,
   Goiânia e a comarca do processo). Recesso de 20 de dezembro a 20 de janeiro suspende os prazos
   (CPC, art. 220; CLT, art. 775-A).
7. **Prazo em dobro**: Fazenda Pública, Ministério Público e Defensoria (CPC, arts. 180, 183 e 186).
   Litisconsortes com advogados diferentes **não** têm prazo em dobro em processo eletrônico (CPC, art. 229, § 2º).
8. Registrar no ADVBOX **o prazo fatal e o prazo interno** (fatal menos 2 dias úteis para a peça
   pronta; menos 1 dia útil para protocolar).

## O que vira tarefa no ADVBOX

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[PRAZO] {{peça}} - {{cliente}} - {{processo}}` | Advogado(a) da área | Prazo interno (e prazo fatal anotado) |
| `[CONFIRMAR CLASSIFICAÇÃO] {{decisão/sentença}} - {{processo}}` | Advogado(a) da área | Mesmo dia |
| `[AUDIÊNCIA] {{tipo}} - {{processo}} - {{data}}` | Advogado(a) da área | Data da audiência + tarefa de preparo 5 dias úteis antes |
| `[CUSTAS] ...` | Ver POP-OP-01 | |
| `[AVISAR CLIENTE] {{assunto}} - {{processo}}` | Atendimento | 1 dia útil |

## Onde salva no Drive

- Ato processual: `CLIENTES/{{cliente}}/02_JUDICIAL/{{nº do processo}} - .../03_DECISOES_E_INTIMACOES/AAAA-MM-DD_{{tipo}}.pdf`
- Relatório diário: `00_ESCRITORIO/CONTROLADORIA/AAAA-MM/AAAA-MM-DD_relatorio-controladoria.md`

## Pendências `[A CONFIRMAR]`
- Números de OAB do Dr. Alex, da Dra. Larissa e da Dra. Jaqueline, para monitorar as publicações.
- Se o ADVBOX já captura as publicações de todas as OABs e de quais tribunais.
- Prazos marcados como **(conferir)** acima: confirmação do advogado(a) antes de virarem regra.
