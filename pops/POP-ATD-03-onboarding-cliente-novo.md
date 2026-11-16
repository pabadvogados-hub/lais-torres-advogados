# POP-ATD-03 — Onboarding do cliente novo

Versão 1 — 16/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Laís |
| **Quem executa** | Estagiário(a) do atendimento `[A CONFIRMAR quem]`; advogado(a) da área nos passos de peça e diagnóstico |
| **Gatilho** | Card do cliente movido para "Fechado" no Infinitum (contrato fechado na reunião) |
| **Termina quando** | Contrato assinado, cobrança cadastrada, pasta no Drive, cliente e demanda no ADVBOX, documentos recebidos e (assessoria) diagnóstico de entrada entregue |
| **Prazo total** | Contrato assinado em até 2 dias úteis; documentos em até 15 dias corridos; diagnóstico da assessoria em até 30 dias corridos |

## Objetivo

O cliente que acabou de fechar tem a melhor experiência do escritório: boas-vindas no mesmo dia,
contrato rápido, sabe com quem falar e o que mandar. E o escritório não recomeça do zero a cada
contratação: modelo de contrato, procuração e lista de documentos já prontos.

## Três tipos de cliente

| Tipo | Contrato | Depois do onboarding |
|---|---|---|
| **Assessoria mensal** (empresa) | Contrato de assessoria `[modelo em 00_ESCRITORIO/MODELOS]` | Diagnóstico de entrada (5 checklists) e plano dos meses seguintes |
| **Tributário** (transação, CAPAG, PGFN) | Contrato tributário com êxito: **25% sobre o proveito econômico para clientes novos**; clientes antigos mantêm 10% | POP-TRIB-02 |
| **Causa única** (um processo ou demanda) | Contrato de causa única | Cobrança de documentos até montar a peça |

## Automação x pessoa

| A automação faz (quando o módulo estiver no ar) | A pessoa faz |
|---|---|
| Ao mover o card para "Fechado": envia boas-vindas (MSG-04) e pede os dados do contrato | Confere os dados recebidos |
| Preenche contrato e procuração com os dados (`{{chaves}}`) e envia o link de assinatura | Revisa contrato quando houver cláusula fora do padrão (Dra. Laís) |
| Cria a pasta no Drive e salva o contrato assinado | Confere a pasta |
| Cadastra cliente e cobranças no Asaas, com lembretes 10/5/3/0 dias (MSG-07) | Confere valor, vencimento e regra da nota fiscal |
| Cria cliente e tarefas no ADVBOX | Confere responsável e prazo das tarefas |
| Cobra os documentos pendentes na cadência (MSG-02) | Liga para o cliente quando a cadência pedir; avisa o advogado(a) |
| Quando os documentos chegam: gera a minuta da peça e manda para revisão | Advogado(a) da área revisa (POP-OP-05) |

## Passo a passo

1. **Boas-vindas** (MSG-04, modelo do tipo de cliente): quem vai atender, canal, horário, o que
   vem a seguir. — *D0, até 2 horas úteis depois do fechamento*
2. **Coletar os dados do contrato** (checklist `CK-DIA-04`, parte "Dados para contrato"). — *D0*
3. **Gerar contrato e procuração** a partir dos modelos do escritório. Cláusula fora do padrão
   (desconto, prazo, escopo diferente) só com OK da Dra. Laís. — *D0 a D1*
4. **Enviar para assinatura eletrônica** `{{ferramenta_assinatura}}` `[A CONFIRMAR]`. Sem assinatura
   em 24 horas: lembrar. Em 48 horas: ligar. — *assinatura até D2 úteis*
5. **Cadastrar a cobrança no Asaas.** — *D0 a D1, após assinatura*
   - Assessoria: registrar os boletos dos 12 meses (aparecem no DDA do cliente).
   - **Desligar as notificações pagas do Asaas** para esse cliente. Os lembretes vão pelo WhatsApp
     do escritório (MSG-07: 10, 5 e 3 dias antes e no dia do vencimento).
   - Nota fiscal pelo Asaas: anotar se o cliente exige a nota **antes** do pagamento ou se ela sai
     **depois** do pagamento.
6. **Criar a pasta no Drive** `CLIENTES/{{NOME DO CLIENTE}}/` com as subpastas do README (item 4.2).
   Contrato e procuração assinados em `01_CONTRATO_E_DOCUMENTOS`. — *D0 a D1*
7. **Cadastrar no ADVBOX**: cliente, processo ou demanda, responsável da área e as tarefas abaixo.
   Colar o link da pasta do Drive no cadastro. — *D1*
8. **Pedir os documentos** — *D1*
   - Assessoria: enviar os 5 checklists de diagnóstico (`CK-DIAG-01` a `05`) e marcar a reunião de diagnóstico.
   - Tributário: pedir a procuração no e-CAC (POP-TRIB-02).
   - Causa única: lista de documentos do caso (checklist do dia a dia correspondente).
9. **Cobrar os documentos até chegarem** (MSG-02):

   | Dia | Ação |
   |---|---|
   | D1 | Pedido com a lista completa |
   | D3 | Lembrete com o que já chegou e o que falta |
   | D5 | Lembrete |
   | D8 | Ligação |
   | D12 | Lembrete avisando que a demanda está parada aguardando os documentos |
   | D15 | Advogado(a) da área liga para o cliente; se houver prazo processual, avisar o risco por escrito |

10. **Documentos completos: produzir a peça ou o diagnóstico.** — *prazo da área (ver POP da peça)*
    - Causa única: minuta da peça → correção (POP-OP-05) → protocolo.
    - Assessoria: diagnóstico de entrada (item 11).
11. **Assessoria: diagnóstico e plano dos meses seguintes.** — *até D30*
    - Cada responsável de área analisa o seu checklist (trabalhista: Kathle; tributário: Dr. Alex;
      cobrança: Dra. Larissa; consumidor e oficina: Dra. Laís).
    - O resultado vira um relatório curto: riscos encontrados (alto, médio, baixo), o que fazer
      em cada mês e os **pacotes de implantação** oferecidos para o que o cliente não tem.
    - Dra. Laís apresenta ao cliente em reunião.
12. **Encerrar o onboarding**: mover o card para "Cliente ativo" e marcar as tarefas como concluídas.

## O que vira tarefa no ADVBOX

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[ONBOARDING] Contrato assinado - {{cliente}}` | Atendimento | D2 úteis |
| `[ONBOARDING] Cobrança e NF cadastradas no Asaas - {{cliente}}` | Dra. Laís `[A CONFIRMAR]` | D1 após assinatura |
| `[ONBOARDING] Documentos recebidos - {{cliente}}` | Atendimento | D15 |
| `[DIAGNÓSTICO] Trabalhista / Tributário / Cobrança / Consumidor / Oficina - {{cliente}}` | Responsável de cada área | D25 |
| `[DIAGNÓSTICO] Reunião de apresentação do plano - {{cliente}}` | Dra. Laís | D30 |
| `[PEÇA] {{tipo}} - {{cliente}}` (causa única) | Advogado(a) da área | Prazo da peça |

## Onde salva no Drive

- Contrato, procuração e documentos pessoais ou societários: `CLIENTES/{{cliente}}/01_CONTRATO_E_DOCUMENTOS/`
- Checklists respondidos, documentos do diagnóstico e relatório: `CLIENTES/{{cliente}}/04_ASSESSORIA_DIAGNOSTICO/`
- Documentos do processo: `CLIENTES/{{cliente}}/02_JUDICIAL/{{nº do processo}} - .../01_DOCUMENTOS_DO_CLIENTE/`

## Pendências `[A CONFIRMAR]`
- Ferramenta de assinatura eletrônica.
- Modelos de contrato (assessoria, tributário, causa única) e procuração: a produzir no Módulo 5.
- Valor e dia de vencimento de cada assessoria; regra da nota (antes ou depois do pagamento) por cliente.
- Honorários do produto tributário além do êxito (há valor fixo ou de diagnóstico?).
- Quem cadastra e confere a cobrança no Asaas.
