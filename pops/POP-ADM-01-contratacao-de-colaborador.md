# POP-ADM-01 — Contratação de colaborador (estagiário e advogado associado)

Versão 1 — 16/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Laís |
| **Quem executa** | Dra. Laís (decisão e assinatura); agente de RH (checklist, pasta, contrato, cobrança de documentos) |
| **Gatilho** | Decisão de contratar alguém, **ou regularização de quem já trabalha sem contrato** (hoje: todos) |
| **Termina quando** | Contrato assinado por todas as partes, pasta do colaborador completa no Drive, dados de pagamento cadastrados no Asaas e, para o associado, contrato **averbado na OAB** |
| **Prazo** | Contrato assinado **antes do primeiro dia de trabalho** (regularização da equipe atual: até `[A CONFIRMAR data]`) |

## Objetivo

Todo colaborador com contrato, documentos numa pasta no Drive (não no celular) e dados bancários
cadastrados. Hoje ninguém da equipe tem contrato formal, e isso é risco trabalhista: estágio sem
termo de compromisso e associação sem os requisitos da OAB podem ser reconhecidos como vínculo de emprego.

## Os tipos de vínculo

| Vínculo | Instrumento | Regra principal |
|---|---|---|
| **Estagiário(a)** | Termo de compromisso de estágio **tripartite**: estudante, escritório e instituição de ensino | Lei 11.788/2008 |
| **Advogado(a) associado(a)** | Contrato de associação, **averbado no registro da sociedade na OAB** | Regulamento Geral do EAOAB, art. 39, e Provimento CFOAB 169/2015 **(conferir)** |
| **Advogado(a) empregado(a)** | Contrato de trabalho (CLT) | EAOAB, arts. 18 a 21 |
| **Meio período / apoio** (hoje: 1 pessoa, R$ 1.000) | `[A CONFIRMAR: qual vínculo]` | Conferir com o contador |

**Atenção, associado(a) x empregado(a):** associação é sem vínculo de emprego, com participação nos
resultados. Exigir horário fixo de entrada e saída, subordinação e pagamento fixo mensal aproxima a
relação de um vínculo de emprego (CLT, arts. 2º e 3º). A forma de remuneração e a rotina das
advogadas integrais devem ser definidas pela Dra. Laís e pelo Dr. Alex antes de escolher o modelo
de contrato `[A CONFIRMAR]`.

**Atenção, OAB e local de trabalho:** a sociedade contratante (LAÍS TORRES SOCIEDADE INDIVIDUAL DE
ADVOCACIA) é registrada em Goiás, e a equipe trabalha em Imperatriz/MA. Confirmar com a OAB em qual
seccional averbar os contratos e se o escritório de Imperatriz precisa estar registrado como filial
(EAOAB, art. 15, § 5º) **(conferir)**. Confirmar também qual pessoa jurídica contrata cada colaborador
(a sociedade da Laís ou o CNPJ do Dr. Alex no Maranhão) `[A CONFIRMAR]`.

## Checklist de documentos

| Documento | Estagiário(a) | Associado(a) | Empregado(a) |
|---|---|---|---|
| RG e CPF (ou CNH) | Sim | Sim | Sim |
| Comprovante de endereço recente | Sim | Sim | Sim |
| Comprovante de matrícula e frequência no curso | Sim | — | — |
| Dados da instituição de ensino e do professor orientador | Sim | — | — |
| Carteira da OAB (estagiário ou advogado) | Sim, se inscrito(a) como estagiário(a) | Sim | Sim |
| Certidão de regularidade na OAB | — | Sim | Sim |
| Chave Pix e dados bancários (preenchidos pelo próprio colaborador no formulário) | Sim | Sim | Sim |
| Contato de emergência | Sim | Sim | Sim |
| CTPS digital, PIS e exame admissional (ASO) | — | — | Sim |
| Apólice do seguro contra acidentes pessoais | Sim (Lei 11.788/2008, art. 9º, IV) | — | — |

## Regras do estágio (Lei 11.788/2008) que entram no termo

- Matrícula e frequência regular, termo de compromisso tripartite e atividades compatíveis com o termo (art. 3º).
- Supervisor do escritório com formação ou experiência na área, até 10 estagiários por supervisor (art. 9º, III).
- Seguro contra acidentes pessoais (art. 9º, IV).
- Relatório de atividades à instituição de ensino a cada 6 meses, no mínimo (art. 9º, VII).
- Jornada de até 6 horas por dia e 30 horas por semana no ensino superior (art. 10, II).
- Duração máxima de 2 anos no mesmo escritório, salvo estagiário com deficiência (art. 11).
- Estágio não obrigatório: bolsa e auxílio-transporte obrigatórios (art. 12).
- Recesso de 30 dias a cada 1 ano de estágio, remunerado se houver bolsa, proporcional se menor (art. 13).
- Descumprimento caracteriza vínculo de emprego (art. 3º, § 2º, e art. 15).

## Automação x pessoa

| O agente de RH faz | A pessoa faz |
|---|---|
| Envia ao colaborador o checklist do tipo de vínculo e o formulário de dados | Dra. Laís define vínculo, valor, função, horário e data de início |
| Cria a pasta do colaborador no Drive e salva o que chegar | Colaborador envia os documentos |
| Gera o contrato no modelo, com os dados (`{{chaves}}`) | Dra. Laís revisa o contrato |
| Envia para assinatura eletrônica e cobra quem não assinou | Instituição de ensino assina o termo (estágio) |
| Cadastra os dados de pagamento no Asaas (POP-ADM-02) | Dra. Laís confere o cadastro |
| Lembra os prazos: relatório semestral, fim do estágio, recesso | Dra. Laís protocola a averbação na OAB (associado) |

## Passo a passo

1. **Definir o vínculo e as condições** (Dra. Laís): tipo, função, área, supervisor, horário, valor,
   dia de pagamento, data de início. — *D0*
2. **Enviar ao colaborador o checklist** do vínculo e o formulário de dados (incluindo chave Pix
   preenchida por ele). — *D0*
3. **Criar a pasta** `RH/{{NOME COMPLETO}} - {{VÍNCULO}}/` com as subpastas abaixo. — *D0*
4. **Receber e conferir os documentos.** Faltou algo: cobrar em 2 dias úteis. — *até D3 úteis*
5. **Gerar o contrato** no modelo do vínculo (modelo em `00_ESCRITORIO/MODELOS/RH/`). — *D3*
6. **Revisão da Dra. Laís.** — *D4*
7. **Assinatura eletrônica** de todas as partes (no estágio: estudante, escritório e instituição de
   ensino; muitas instituições têm modelo e fluxo próprios `[A CONFIRMAR por faculdade]`). — *antes do 1º dia*
8. **Seguro** (estágio): incluir o estagiário na apólice e salvar o comprovante. — *antes do 1º dia*
9. **Averbação na OAB** (associado): protocolar o contrato para averbação no registro da sociedade e
   salvar o protocolo e a certidão. — *até 10 dias úteis após a assinatura `[A CONFIRMAR prazo e taxa na OAB]`*
10. **Cadastrar o pagamento** no Asaas (POP-ADM-02). — *antes do 1º pagamento*
11. **Criar os lembretes**: relatório semestral do estágio, vencimento do termo, recesso, renovação. — *D0 do início*

## Regularização da equipe atual

Mesmo passo a passo, para cada pessoa que já trabalha no escritório (5 estagiários, 2 advogadas
integrais e a pessoa de meio período), com data de início real `[A CONFIRMAR]`. Prioridade: quem
está há mais tempo e as advogadas integrais (definir o modelo de vínculo antes).

## O que vira tarefa no ADVBOX

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[RH] Documentos - {{colaborador}}` | Agente de RH / Dra. Laís | D3 úteis |
| `[RH] Contrato assinado - {{colaborador}}` | Dra. Laís | Antes do 1º dia |
| `[RH] Averbação na OAB - {{colaborador}}` | Dra. Laís | 10 dias úteis após a assinatura |
| `[RH] Relatório semestral de estágio - {{colaborador}}` | Supervisor(a) | A cada 6 meses |
| `[RH] Vencimento do termo de estágio - {{colaborador}}` | Dra. Laís | 30 dias antes do fim |

## Onde salva no Drive

```
RH/{{NOME COMPLETO}} - {{ESTAGIÁRIO | ASSOCIADO | EMPREGADO | APOIO}}/
├── 01_DOCUMENTOS_PESSOAIS
├── 02_CONTRATO_E_ADITIVOS        contrato assinado, averbação OAB, apólice do seguro
├── 03_PAGAMENTOS                 comprovantes por mês (AAAA-MM_comprovante.pdf), recibos
├── 04_RELATORIOS_E_AVALIACOES    relatórios semestrais de estágio
└── 05_DESLIGAMENTO               termo de rescisão ou distrato
```

## Pendências `[A CONFIRMAR]`
- Modelo de vínculo das advogadas integrais (associação ou emprego) e forma de remuneração.
- Seccional da OAB para averbação; necessidade de filial em Imperatriz/MA; prazo e taxa da averbação.
- Qual pessoa jurídica contrata cada colaborador.
- Vínculo da pessoa de meio período.
- Instituições de ensino de cada estagiário e se têm modelo próprio de termo.
- Seguradora e apólice do seguro de estágio.
- Data-limite para regularizar a equipe atual.
- Modelos de contrato (Módulo 3; o Casal da IA ofereceu enviar o modelo de contrato que usa).
