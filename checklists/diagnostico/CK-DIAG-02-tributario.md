# CK-DIAG-02 — Diagnóstico de entrada: tributário

Versão 1 — 16/11/2026 · Dono: Dr. Alex · Usado no POP-ATD-03, passo 8, e no POP-TRIB-01

## Como usar

- **Quando**: no início da assessoria. **Atenção especial a oficinas mecânicas e autopeças**: todas
  as que passaram pelo escritório tinham débitos tributários altos que nunca foram trabalhados.
- **Quem preenche**: o cliente, com o contador dele. O atendimento envia e cobra (MSG-02).
- **Prazo para o cliente**: 15 dias corridos. O item 1 (procuração no e-CAC) é o mais importante:
  com ele o escritório levanta quase todo o resto sozinho (POP-TRIB-02).
- **Como marcar**: **Tem**, **Não tem** ou **Enviado**.
- **Quem analisa**: Dr. Alex. Havendo passivo, o cliente entra no fluxo do produto tributário
  (POP-TRIB-02 em diante), com os honorários de êxito do contrato.

## Dados da empresa

| Pergunta | Resposta |
|---|---|
| Razão social, CNPJ e CNPJs do mesmo grupo | |
| Regime tributário (Simples Nacional, Lucro Presumido, Lucro Real) | |
| Faturamento anual aproximado | |
| Contador (nome, escritório, telefone, e-mail) | |
| A empresa já fez parcelamento ou transação? Algum foi cancelado (rescindido)? Quando? | |
| Já teve conta bloqueada ou bem penhorado por dívida tributária? | |
| Precisa de certidão negativa para algo (licitação, financiamento, cliente grande)? | |

## Checklist

| # | Item | Por que importa | Tem | Não tem | Enviado | Se não tem, o escritório oferece |
|---|---|---|---|---|---|---|
| 1 | **Procuração eletrônica no e-CAC para o escritório** | Libera o levantamento completo do passivo federal | ( ) | ( ) | ( ) | Passo a passo no gov.br, em 2 minutos |
| 2 | Certidão federal (Receita e PGFN) | Mostra se há pendência federal | ( ) | ( ) | ( ) | Emissão e análise |
| 3 | Certidão estadual (Sefaz) | Pendências de ICMS | ( ) | ( ) | ( ) | Emissão e análise |
| 4 | Certidão municipal | Pendências de ISS, IPTU, taxas | ( ) | ( ) | ( ) | Emissão e análise |
| 5 | Certidão do FGTS (CRF) | Débito de FGTS | ( ) | ( ) | ( ) | Emissão e análise |
| 6 | Certidão trabalhista (CNDT) | Débitos em processos trabalhistas | ( ) | ( ) | ( ) | Emissão e análise |
| 7 | Parcelamentos ativos (federal, estadual, municipal) e situação das parcelas | Parcela atrasada pode cancelar o parcelamento | ( ) | ( ) | ( ) | Controle mensal (POP-TRIB-06) |
| 8 | Dívida ativa da União (Regularize) | Base da transação tributária | ( ) | ( ) | ( ) | Levantamento e CAPAG (POP-TRIB-02 e 03) |
| 9 | Dívida ativa estadual e municipal | Programas próprios de negociação | ( ) | ( ) | ( ) | Levantamento e análise |
| 10 | Execuções fiscais em andamento | Risco de bloqueio e penhora | ( ) | ( ) | ( ) | Defesa e análise de teses (prescrição, nulidade) |
| 11 | Autos de infração e processos administrativos | Prazos de defesa curtos | ( ) | ( ) | ( ) | Defesa administrativa |
| 12 | Intimações na Caixa Postal do e-CAC / Domicílio Tributário Eletrônico | Ex.: termo de exclusão do Simples, com prazo para defesa | ( ) | ( ) | ( ) | Monitoramento |
| 13 | Declarações em dia (PGDAS-D, DCTFWeb, EFD, DEFIS, conforme o regime) | Declaração em atraso gera multa e impede certidão | ( ) | ( ) | ( ) | Verificação com o contador |
| 14 | Notas fiscais de compra de autopeças e produtos com ICMS-ST (amostra de 12 meses) | Possível recuperação de tributo pago a mais (item "Oportunidades") | ( ) | ( ) | ( ) | Análise de recuperação de créditos |
| 15 | Débitos em nome dos sócios (pessoa física) ligados à empresa | Risco de redirecionamento | ( ) | ( ) | ( ) | Análise de risco |

## Oportunidades a avaliar (só o Dr. Alex decide se cabem)

Nenhuma destas é promessa ao cliente: dependem do regime, das notas e da jurisprudência atual.

- **Transação tributária com a PGFN** (Lei 13.988/2020), quando houver dívida ativa da União e CAPAG compatível.
- **PIS/Cofins sobre autopeças com tributação monofásica** (Lei 10.485/2002): avaliar valores pagos
  indevidamente por revendedores, inclusive no Simples Nacional **(conferir)**.
- **ICMS-ST pago a mais** quando a base presumida for maior que a efetiva (STF, Tema 201) e a
  legislação do estado **(conferir)**.
- **Exclusão do ICMS da base do PIS/Cofins** para Lucro Presumido e Real (STF, Tema 69) **(conferir modulação)**.
- **Prescrição** de débitos antigos e de execuções paradas (CTN, art. 174; Lei 6.830/1980, art. 40).

## Resultado (preenche o escritório)

| Item | Valor | Situação | Ação |
|---|---|---|---|
| Passivo federal (Receita + PGFN) | | | |
| Passivo estadual | | | |
| Passivo municipal | | | |
| Faixa de CAPAG | | | |
| Oportunidades de recuperação | | | |

**Pacotes**: Regularização Tributária (diagnóstico do passivo + transação; êxito sobre o proveito
econômico: 25% para clientes novos, 10% para os antigos); Recuperação de Créditos `[A CONFIRMAR modelo de honorários]`;
Monitoramento mensal de certidões e parcelas `[A CONFIRMAR se é incluído na assessoria]`.

Salvar em: `04 CLIENTES/{{cliente}}/04 DIAGNÓSTICO DA ASSESSORIA/` e, havendo passivo, `05 TRIBUTÁRIO/`.
