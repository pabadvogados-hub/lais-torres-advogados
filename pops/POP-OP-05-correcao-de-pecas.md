# POP-OP-05 — Correção de peças (primeira correção pela IA, revisão final pelo responsável da área)

Versão 1 — 16/11/2026

| | |
|---|---|
| **Dono do POP** | Dr. Alex |
| **Quem executa** | IA (primeira correção); revisor(a) da área (revisão final) |
| **Gatilho** | Minuta de peça pronta (feita por estagiário, advogado(a) ou IA) |
| **Termina quando** | Peça com parecer **APROVADA** do revisor(a), salva no Drive e protocolada |
| **Prazo** | Primeira correção pela IA: no mesmo dia útil. Revisão final: até 1 dia útil antes do protocolo |

## Objetivo

Tirar a Laís e o Alex da correção de tudo. A IA faz a primeira correção com critérios objetivos; o
advogado(a) responsável pela área faz só a **revisão final de protocolo**. Os sócios só entram
quando o revisor(a) pedir ou a peça for estratégica.

## Quem faz a revisão final

| Área | Revisor(a) final | Quando sobe para os sócios |
|---|---|---|
| Cível, consumidor, cobrança, execução, monitória | Dra. Larissa | Dúvida da revisora, valor alto ou cliente estratégico → Dra. Laís |
| Trabalhista | Kathle (mérito) + assinatura de advogado(a) inscrito(a) `[A CONFIRMAR quem]` | Dúvida → Dra. Laís |
| Tributário | Dr. Alex | — |
| Contratos | Dra. Laís | — |

## Fluxo

```
Minuta → 1ª correção pela IA → autor(a) ajusta → revisão final da área → protocolo
              (mesmo dia)        (até 1 dia útil)    (até 1 dia útil antes)
```

## Passo a passo

1. **Autor(a) da minuta** salva a peça em `02_PECAS` com o nome `MINUTA - TIPO - CLIENTE - Nº DO PROCESSO - AAAA-MM-DD.docx`
   e junta, na mesma pasta ou em link, **o que a peça enfrenta** (inicial, decisão, sentença) e os documentos que ela cita. — *prazo interno da peça*
2. **Rodar a primeira correção pela IA** com o checklist abaixo. A IA devolve um parecer com status
   **APROVADA**, **APROVADA COM RESSALVAS** ou **NÃO APROVADA**, e a lista numerada de ajustes (onde
   está o problema e qual a correção sugerida). — *mesmo dia útil*
3. **Autor(a) faz os ajustes** e marca no parecer o que foi corrigido. — *até 1 dia útil*
4. **Revisão final** pelo revisor(a) da área: lê a peça inteira, confere o parecer da IA e os pontos
   que a IA não confere (item "O que a IA não faz"). Devolve com OK ou com ajustes. — *até 1 dia útil antes do protocolo*
5. **Versão final** salva como `TIPO - CLIENTE - Nº DO PROCESSO - AAAA-MM-DD.docx` e em PDF, e protocolada.
6. **Registrar no ADVBOX** o protocolo e concluir a tarefa.

## Checklist da primeira correção (critérios objetivos)

A IA percorre as camadas na ordem: o que é eliminatório primeiro.

**Camada 1 — Admissibilidade (eliminatória: qualquer falha = NÃO APROVADA)**
1. Tempestividade: prazo conferido em dias úteis, data da publicação e contagem (POP-OP-02).
2. Endereçamento ao juízo ou tribunal certo.
3. Número do processo conferido dígito a dígito; nomes das partes certos.
4. Procuração e, se for o caso, substabelecimento nos autos; advogado(a) que assina está habilitado(a).
5. Preparo, custas e depósito recursal, quando exigidos (POP-OP-01).
6. Cabimento: é a peça certa para o ato atacado (POP-OP-02, árvore de decisão).

**Camada 2 — Estrutura e conformidade jurídica**
7. Estrutura completa da peça (fatos, direito, pedidos ou a estrutura padrão do tipo de peça).
8. Artigos de lei citados existem e correspondem ao que a peça afirma.
9. Toda jurisprudência, súmula e OJ citada está marcada para conferência humana (ver "O que a IA não faz").
10. Recurso: cada fundamento da decisão atacada foi impugnado especificamente.
11. Defesa ou réplica: todas as preliminares e todos os pedidos da outra parte foram enfrentados.
12. Todo pedido tem fundamento, e todo fundamento tem pedido correspondente.

**Camada 3 — Tese e prova**
13. Cada tese está amarrada a documento ou prova dos autos (ID, folha ou anexo).
14. Não há fato que não esteja nos autos ou nos documentos do cliente.
15. Não há teses contraditórias entre si.
16. O ônus da prova está corretamente distribuído (CPC, art. 373; CLT, art. 818).

**Camada 4 — Riscos**
17. Pontos fracos que a outra parte vai explorar, e se a peça já se antecipa a eles.
18. Risco de preclusão, inovação recursal, litigância de má-fé.

**Camada 5 — Linguagem e formatação**
19. Linguagem formal, técnica, objetiva, sem gíria, sem primeira pessoa no corpo técnico.
20. Ortografia, concordância, repetição de palavras e parágrafos longos demais.
21. Padrão visual do escritório: timbrado, fonte, espaçamento, títulos `[A CONFIRMAR padrão do escritório]`.
22. Fecho, local, data, nome e OAB de quem assina.
23. Nome do arquivo no padrão.

## O que a IA não faz (é do revisor humano)

- **Não confirma vigência** de lei, súmula, OJ ou tese: o revisor confere em fonte oficial.
- **Não confirma que a jurisprudência existe**: toda decisão citada é conferida no site do tribunal
  ou em repositório confiável. Precedente não localizado sai da peça.
- **Não inventa** fato, documento, argumento ou precedente para "completar" a peça.
- **Não substitui** a revisão final nem a assinatura do advogado(a).

## O que vira tarefa no ADVBOX

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[CORREÇÃO IA] {{tipo}} - {{cliente}} - {{processo}}` | Autor(a) da minuta | Mesmo dia útil da minuta |
| `[REVISÃO FINAL] {{tipo}} - {{cliente}} - {{processo}}` | Revisor(a) da área | Prazo fatal menos 1 dia útil |
| `[PROTOCOLO] {{tipo}} - {{cliente}} - {{processo}}` | Quem assina | Prazo fatal menos 1 dia útil |

## Onde salva no Drive

`CLIENTES/{{cliente}}/02_JUDICIAL/{{nº do processo}} - .../02_PECAS/`
- `MINUTA - ...docx` (versões de trabalho)
- `PARECER IA - ...md` (parecer da primeira correção)
- `TIPO - CLIENTE - Nº - AAAA-MM-DD.docx` e `.pdf` (versão protocolada)

## Pendências `[A CONFIRMAR]`
- Padrão visual das peças do escritório (timbrado, fonte, espaçamento, recuo).
- Quem assina as peças trabalhistas.
- Peças reais por área (5 a 10) para calibrar a IA com o estilo do escritório.
