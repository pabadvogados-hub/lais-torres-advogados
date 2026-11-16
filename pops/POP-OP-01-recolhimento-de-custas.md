# POP-OP-01 — Intimação para recolhimento de custas

Versão 1 — 16/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Laís |
| **Quem executa** | Camila (controladoria) gera a guia e controla o prazo; atendimento envia ao cliente e cobra o comprovante |
| **Gatilho** | Intimação, despacho ou exigência para recolher custas, despesas, preparo, diligência ou depósito |
| **Termina quando** | Comprovante juntado no processo e salvo no Drive, tarefa concluída no ADVBOX |
| **Prazo interno** | Guia ao cliente em até 1 dia útil; pagamento até 3 dias úteis antes do prazo fatal; juntada até 1 dia útil antes do prazo fatal |

## Objetivo

Recolhimento de custas é tarefa repetitiva e padrão: gerar a guia, mandar ao cliente, cobrar o
comprovante e juntar no processo. Este POP tira isso da cabeça das pessoas e evita o risco mais grave:
**perder o prazo e ter a ação cancelada ou o recurso não conhecido (deserção)**.

## Tipos de custas e prazos legais

| Situação | Prazo e consequência | Base legal |
|---|---|---|
| **Custas iniciais** não recolhidas na distribuição (cível) | Intimado o advogado, 15 dias para recolher, sob pena de cancelamento da distribuição | CPC, art. 290 |
| **Preparo de recurso** (cível) | Comprovar no ato da interposição. Insuficiente: 5 dias para complementar. Não recolhido: recolher **em dobro**, sob pena de deserção | CPC, art. 1.007, caput, §§ 2º e 4º |
| **Diligência de oficial de justiça, perícia, outras despesas** (cível) | Prazo fixado pelo juiz; se a decisão não fixar, 5 dias | CPC, arts. 82 e 218, § 3º |
| **Recurso inominado** (Juizado Especial) | Preparo nas 48 horas seguintes à interposição, independentemente de intimação | Lei 9.099/1995, art. 42, § 1º |
| **Custas no recurso trabalhista** | Pagas e comprovadas dentro do prazo do recurso | CLT, art. 789, § 1º |
| **Depósito recursal trabalhista** (empresa recorrente) | Comprovado no prazo do recurso | CLT, art. 899, § 1º; Súmula 245 do TST **(conferir)** |
| **Prazos em geral** | Contados em dias úteis | CPC, art. 219; CLT, art. 775 |

Guias: cada tribunal tem seu sistema (TJMA, TJGO, Justiça Federal/TRF1, TRT da 16ª Região no
Maranhão, TRT da 18ª Região em Goiás). O passo a passo de emissão de cada tribunal fica em
`01 ESCRITÓRIO/MODELOS/CUSTAS/` `[A CONFIRMAR: montar o roteiro de cada sistema na implantação]`.

## Automação x pessoa

| A automação faz | A pessoa faz |
|---|---|
| O agente de controladoria identifica a intimação de custas e cria a tarefa com o prazo (POP-OP-02) | Camila confere o prazo e o valor |
| Envia a guia ao cliente (MSG-03) e cobra o comprovante nos dias combinados | Camila gera a guia no site do tribunal |
| Salva o comprovante recebido no Drive | Atendimento liga quando a cadência pedir |
| Avisa a controladoria quando o comprovante chegar | Camila ou o advogado(a) junta o comprovante no processo |

## Passo a passo

1. **Ler a intimação e anotar**: processo, tipo de custa, valor (se informado), prazo fatal e
   consequência de não pagar. Calcular o prazo em dias úteis. — *D0*
2. **Conferir se o cliente tem gratuidade de justiça ou isenção.** Se tiver, avisar o advogado(a):
   pode ser caso de petição informando, não de guia. — *D0*
3. **Gerar a guia** no sistema do tribunal. Conferir: número do processo, nome das partes, valor,
   código da custa e **data de vencimento da guia** (se a guia vencer antes do prazo, anotar). — *D0, até D1 útil*
4. **Salvar a guia** no Drive (`04 CUSTAS E GUIAS`), com nome `AAAA-MM-DD_GUIA-CUSTAS_{{tipo}}.pdf`. — *D0*
5. **Enviar ao cliente** pelo canal dele (MSG-03, modelo 1), com valor, data limite de pagamento
   (prazo interno = prazo fatal menos 3 dias úteis) e o que acontece se não pagar. — *até D1 útil*
6. **Cobrar o comprovante** (MSG-03, modelos 2 a 4):

   | Quando | Ação |
   |---|---|
   | 2 dias úteis depois do envio | Lembrete |
   | Data limite combinada com o cliente | Lembrete com aviso do prazo |
   | Prazo fatal menos 2 dias úteis | **Ligação** do atendimento e aviso ao advogado(a) da área |
   | Prazo fatal menos 1 dia útil | Advogado(a) liga e envia ciência de risco por escrito (MSG-03, modelo 4) |

7. **Política de adiantamento pelo escritório**: o escritório só paga custas no lugar do cliente com
   autorização da Dra. Laís, e o valor é lançado para reembolso `[A CONFIRMAR regra]`.
8. **Recebeu o comprovante**: conferir valor, data e autenticação bancária. Comprovante de
   agendamento **não vale**: pedir o comprovante do pagamento efetivado. — *no dia em que chegar*
9. **Juntar no processo** com petição simples de juntada (modelo em `01 ESCRITÓRIO/MODELOS`). — *até prazo fatal menos 1 dia útil*
10. **Salvar o protocolo** da juntada no Drive e concluir as tarefas no ADVBOX. — *no mesmo dia*

## O que vira tarefa no ADVBOX

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[CUSTAS] Gerar guia e enviar ao cliente - {{cliente}} - {{processo}}` | Camila | D1 útil |
| `[CUSTAS] Cobrar comprovante - {{cliente}} - {{processo}}` | Atendimento | Prazo fatal menos 3 dias úteis |
| `[CUSTAS] Juntar comprovante - {{cliente}} - {{processo}}` | Camila / advogado(a) da área | Prazo fatal menos 1 dia útil (marcar também o prazo fatal) |

## Onde salva no Drive

`04 CLIENTES/{{cliente}}/02 JUDICIAL/{{nº do processo}} - .../04 CUSTAS E GUIAS/` — guia, comprovante e protocolo da juntada.

## Pendências `[A CONFIRMAR]`
- Roteiro de emissão de guia de cada tribunal em que o escritório atua.
- Política de adiantamento de custas pelo escritório e reembolso.
- Quem assina a petição de juntada em cada área.
