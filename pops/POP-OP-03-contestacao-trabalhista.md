# POP-OP-03 — Contestação trabalhista (com quesitos, impugnação a laudo e preparo de audiência)

Versão 1 — 16/11/2026

| | |
|---|---|
| **Dono do POP** | Kathle (responsável pelo trabalhista) `[A CONFIRMAR grafia]` |
| **Quem executa** | Kathle e estagiários do trabalhista; IA nas etapas de análise e redação; advogado(a) inscrito(a) assina e protocola `[A CONFIRMAR quem]` |
| **Gatilho** | Cliente (empresa) recebeu notificação de reclamação trabalhista, ou a controladoria identificou a citação (POP-OP-02) |
| **Termina quando** | Contestação e documentos protocolados, preposto e testemunhas preparados, audiência realizada e ata salva |
| **Prazo** | Contestação apresentada **até a audiência** (CLT, art. 847); prazo interno: peça pronta para revisão **5 dias úteis** antes da audiência e protocolada **até 1 dia útil** antes |

## Objetivo

Defesa trabalhista sólida, amarrada às provas, sem esquecer preliminar, pedido ou documento. O
método é de 4 etapas: **analisar a inicial → diagnosticar as provas da empresa → alinhar com o
cliente → redigir**. Sem diagnóstico, a peça vira chute: não pular etapas, mesmo com pressa.

## Prazos legais que comandam o trabalho

| Ato | Prazo / regra | Base legal |
|---|---|---|
| Notificação da reclamada | Audiência com antecedência mínima de 5 dias da notificação | CLT, art. 841 |
| Contestação | Até a audiência; pelo PJe, pode ser enviada antes, com sigilo até a audiência | CLT, art. 847 e parágrafo único |
| Ausência da reclamada na audiência | Revelia e confissão quanto à matéria de fato | CLT, art. 844 |
| Preposto | Não precisa ser empregado; deve ter conhecimento dos fatos, e o que disser obriga a empresa | CLT, art. 843, §§ 1º e 3º |
| Testemunhas | Até 3 por parte no rito ordinário; até 2 no sumaríssimo | CLT, arts. 821 e 852-H, § 2º |
| Rito sumaríssimo | Causas de até 40 salários mínimos | CLT, art. 852-A |
| Perícia de insalubridade/periculosidade | Obrigatória quando houver o pedido | CLT, art. 195, § 2º |
| Assistente técnico | Cada parte pode indicar um; laudo no mesmo prazo do perito | Lei 5.584/1970, art. 3º |
| Quesitos e manifestação sobre laudo | Prazo fixado pelo juiz no despacho. No CPC (aplicação subsidiária): quesitos em 15 dias da intimação da nomeação (art. 465, § 1º) e manifestação sobre o laudo em 15 dias (art. 477, § 1º) **(conferir: na Justiça do Trabalho vale o prazo do despacho)** | CLT, art. 769; CPC, arts. 465 e 477 |
| Prazos | Dias úteis | CLT, art. 775 |

## Automação x pessoa

| A IA faz | A pessoa faz |
|---|---|
| Etapa 1: analisa inicial e documentos do reclamante | Junta a inicial completa, documentos e andamento |
| Etapa 2: diagnóstico pedido a pedido com os documentos da empresa | Cobra os documentos da empresa (`CK-DIA-02`) |
| Sugere perguntas para o alinhamento com o cliente | Faz a reunião de alinhamento (etapa humana) |
| Etapa 4: redige a contestação na estrutura padrão | Revisa e ajusta a tese |
| Primeira correção (POP-OP-05) | Revisão final de Kathle e assinatura do advogado(a) |
| Sugere quesitos e minuta de impugnação ao laudo | Confere com o caso e com o assistente técnico |

**A IA nunca inventa** fato, documento, súmula, OJ ou jurisprudência. Faltou informação: marcar
`[CONFIRMAR COM CLIENTE]` ou `[VERIFICAR NOS AUTOS]`. Faltou precedente: `[INSERIR PRECEDENTE CONFERIDO]`.

## Passo a passo

### Fase A — Recebimento (D0 = dia em que a notificação chegou ao escritório)

1. **Registrar**: número do processo, vara, data e tipo da audiência (inicial ou una), rito
   (ordinário ou sumaríssimo), valor da causa. Criar as tarefas no ADVBOX. — *D0*
2. **Pedir ao cliente os documentos e informações** do `CK-DIA-02` (MSG-02). Prazo para o cliente
   enviar: **5 dias úteis**, ou menos se a audiência estiver próxima. — *D0*
3. **Avisar o cliente** da data da audiência, de que precisa de preposto e de testemunhas, e de que
   a ausência gera revelia (CLT, art. 844). — *D0*

### Fase B — Etapa 1: análise inicial (sem os documentos da empresa)

4. **Rodar a análise da inicial** (IA): síntese da demanda; quadro de pedidos com fundamento e valor;
   documentos do reclamante e o que pretendem provar; andamento e prazos; vícios e preliminares em tese
   (inépcia — CPC, art. 330, c/c CLT, art. 840, § 1º; condições da ação; preliminares do CPC, art. 337;
   prescrição bienal e quinquenal — CF, art. 7º, XXIX); teses possíveis e **lista de documentos que a
   empresa precisa providenciar**. — *até D2 úteis*

### Fase C — Etapa 2: diagnóstico com os documentos da empresa

5. **Rodar o diagnóstico pedido a pedido** (IA), para cada pedido: — *até 2 dias úteis após os documentos*
   - a) pedido; b) causa de pedir; c) ônus da prova (CLT, art. 818, c/c CPC, art. 373);
   - d) provas do reclamante; e) provas da empresa e como ajudam;
   - f) cenário: favorável, equilibrado ou desfavorável;
   - g) lacunas e documentos que ainda faltam; h) prova testemunhal necessária (objeto e perfil da testemunha);
   - i) prova pericial necessária; j) tese principal, subsidiária e risco (alto, médio, baixo).
   - Ao final: pedidos de maior risco, pedidos com boa chance, temas-chave, **avaliação de acordo** e esqueleto da contestação.

### Fase D — Etapa 3: alinhamento com o cliente (etapa humana)

6. **Reunião ou ligação com o cliente** (Kathle): confirmar a versão da empresa nos pontos decisivos
   (motivo real da saída, rotina, jornada, pagamentos por fora, testemunhas possíveis). Levar a
   avaliação de acordo, quando houver risco alto. Registrar o que foi dito no ADVBOX. — *até 7 dias úteis antes da audiência*

### Fase E — Etapa 4: redação

7. **Redigir a contestação** (IA) na estrutura padrão, nesta ordem: — *pronta até 5 dias úteis antes da audiência*
   1. Endereçamento; qualificação da reclamada; número do processo.
   2. **I. Síntese da demanda.**
   3. **II. Preliminares** — só as aplicáveis. Avaliar sempre: impugnação à justiça gratuita (CLT,
      art. 790, §§ 3º e 4º); ônus da prova (CLT, art. 818, c/c CPC, art. 373); limitação da condenação
      aos valores da inicial quando os pedidos forem líquidos (CLT, art. 840, § 1º; CPC, arts. 141 e 492);
      prescrição; inépcia; incompetência territorial (CLT, art. 651); ilegitimidade.
      Preliminar sem fundamento real **não entra**: uma sólida vale mais que três frágeis.
   4. **III. Mérito** — um tópico por pedido, cada um com: versão da empresa → documento que prova →
      fundamento legal → pedido de improcedência. Começar com "Pelo princípio da eventualidade".
   5. **IV. Litigância de má-fé** — só se cabível (CLT, arts. 793-A e 793-B).
   6. **V. Honorários sucumbenciais** (CLT, art. 791-A).
   7. **VI. Impugnação específica aos documentos** do reclamante.
   8. **VII. Descontos previdenciários e fiscais; compensação e dedução.**
   9. **VIII. Conclusão e requerimentos**: improcedência, pedidos subsidiários, preliminares, provas
      (depoimento pessoal do reclamante, testemunhas, perícia, documentos), honorários.
   - Terceira pessoa ("o Reclamante", "a Reclamada"); tom firme e técnico; sem comentários do tipo
     "neste tópico será demonstrado"; sem marcadores de lista com símbolo, só a), b), c).
8. **Correção** pelo POP-OP-05 (IA + revisão final de Kathle + assinatura do advogado(a) inscrito(a)). — *até 3 dias úteis antes*
9. **Protocolar** contestação e documentos no PJe, com sigilo até a audiência quando for estratégico.
   Conferir se a notificação ou o despacho exige envio antecipado. — *até 1 dia útil antes da audiência*

### Fase F — Preparo de audiência

10. **Carta de preposição** (modelo em `00_ESCRITORIO/MODELOS`, ver `CK-DIA-04`) assinada pelo
    representante legal, com o documento do preposto. — *até 3 dias úteis antes*
11. **Preparar o preposto** (Kathle): reunião de 30 a 60 minutos com o roteiro dos fatos do processo
    (admissão, função, jornada, salário, saída, cada pedido). Regra: o preposto diz o que sabe, com
    segurança; "não sei" sobre fato do processo pode gerar confissão (CLT, art. 843, § 1º). — *até 2 dias úteis antes*
12. **Testemunhas**: confirmar nome, contato e o que cada uma sabe; até 3 (ordinário) ou 2
    (sumaríssimo). Comparecem independentemente de intimação (CLT, art. 825); no sumaríssimo, só é
    intimada a testemunha comprovadamente convidada que não comparecer (CLT, art. 852-H, § 3º): guardar
    o comprovante do convite. — *até 2 dias úteis antes*
13. **Pasta da audiência**: contestação, documentos, cálculo do risco, proposta de acordo autorizada
    pelo cliente (valor máximo por escrito), perguntas ao reclamante e às testemunhas. — *1 dia útil antes*
14. **Depois da audiência**: salvar a ata, lançar no ADVBOX os próximos atos (prazos, perícia,
    razões finais, sentença) e avisar o cliente. — *no mesmo dia*

### Fase G — Perícia (insalubridade, periculosidade, doença ocupacional)

15. **Quesitos e assistente técnico**: no prazo do despacho de nomeação do perito. Indicar assistente
    técnico `[A CONFIRMAR: profissionais parceiros]` e apresentar quesitos. — *prazo interno: 2 dias úteis antes do fatal*
    Quesitos-base (adaptar ao caso):
    1. Quais as atividades efetivamente exercidas pelo reclamante e em quais locais?
    2. Qual o agente (físico, químico, biológico) alegado e qual o anexo da NR-15 ou NR-16 aplicável?
    3. A exposição era habitual, intermitente ou eventual? Por quanto tempo da jornada?
    4. A empresa fornecia EPI? Quais, com CA válido, com que periodicidade? (fichas de EPI)
    5. Os EPIs fornecidos neutralizavam ou eliminavam o agente? Fundamente.
    6. Há laudo ambiental da empresa (PGR, LTCAT, laudo de insalubridade)? Suas conclusões coincidem com a perícia?
    7. A perícia foi feita no local original de trabalho e nas mesmas condições da época do contrato?
    8. (Doença) Há nexo causal ou concausal com o trabalho? Há incapacidade? Total ou parcial, temporária ou permanente? Há fatores extralaborais?
16. **Acompanhar a diligência pericial** com o cliente e o assistente técnico (data e local).
17. **Impugnação ao laudo**: no prazo do despacho. A IA compara o laudo com os quesitos, com os
    documentos da empresa (fichas de EPI, PGR, LTCAT) e com o parecer do assistente; aponta quesito não
    respondido, conclusão sem base técnica, período ou local errado, EPI ignorado. Pedir esclarecimentos
    ou nova perícia quando cabível (CPC, arts. 477, § 2º, e 480). Honorários periciais: responsabilidade
    da parte sucumbente no objeto da perícia (CLT, art. 790-B). — *prazo interno: 2 dias úteis antes do fatal*

## O que vira tarefa no ADVBOX

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[TRAB] Cobrar documentos da empresa - {{cliente}} - {{processo}}` | Atendimento | D0 + 5 dias úteis |
| `[TRAB] Análise da inicial (etapa 1) - {{processo}}` | Kathle | D2 úteis |
| `[TRAB] Diagnóstico com documentos (etapa 2) - {{processo}}` | Kathle | 2 dias úteis após documentos |
| `[TRAB] Alinhamento com cliente - {{processo}}` | Kathle | Audiência menos 7 dias úteis |
| `[PRAZO] Contestação - {{cliente}} - {{processo}}` | Kathle | Pronta: audiência menos 5 dias úteis; protocolo: menos 1 dia útil |
| `[AUDIÊNCIA] Preparar preposto e testemunhas - {{processo}}` | Kathle | Audiência menos 2 dias úteis |
| `[AUDIÊNCIA] {{tipo}} - {{processo}} - {{data}}` | Advogado(a) que vai à audiência | Data da audiência |
| `[PRAZO] Quesitos e assistente técnico - {{processo}}` | Kathle | Prazo do despacho menos 2 dias úteis |
| `[PRAZO] Manifestação sobre laudo - {{processo}}` | Kathle | Prazo do despacho menos 2 dias úteis |

## Onde salva no Drive

`CLIENTES/{{cliente}}/02_JUDICIAL/{{nº do processo}} - {{reclamante}} - RECLAMAÇÃO TRABALHISTA/`
- `01_DOCUMENTOS_DO_CLIENTE` — documentos da empresa, carta de preposição.
- `02_PECAS` — análise (etapas 1 e 2), contestação (minuta e protocolada), quesitos, impugnação ao laudo.
- `03_DECISOES_E_INTIMACOES` — notificação, atas, laudo, sentença.

## Pendências `[A CONFIRMAR]`
- Quem assina e protocola as peças trabalhistas enquanto a Kathle não estiver inscrita como advogada.
- Papel timbrado e padrão de formatação das peças do escritório.
- Assistentes técnicos parceiros (engenharia de segurança e medicina do trabalho).
- 5 a 10 contestações reais do escritório, para montar o banco de teses próprio.
- Prazos marcados como **(conferir)**.
