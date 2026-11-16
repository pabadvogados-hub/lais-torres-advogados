# CK-DIA-04 — Procuração, contrato de honorários e carta de preposição

Versão 1 — 16/11/2026 · Dono: Dra. Laís · Usado no POP-ATD-03, no POP-OP-03 e sempre que faltar documento de representação

**Quando usar**: cliente novo; demanda nova de empresa do grupo sem procuração; audiência que
precisa de preposto; procuração antiga ou sem os poderes necessários.
**Regra**: os modelos ficam em `01 ESCRITÓRIO/MODELOS/` com campos `{{chave}}`. Nunca "remendar"
procuração de outro cliente.

## A. Procuração

### Outorgante pessoa física

| Dado | OK |
|---|---|
| Nome completo, nacionalidade, estado civil, profissão | ( ) |
| CPF e RG | ( ) |
| Endereço completo com CEP | ( ) |
| E-mail e telefone | ( ) |

### Outorgante pessoa jurídica

| Dado | OK |
|---|---|
| Razão social, CNPJ, endereço da sede | ( ) |
| Representante legal: nome, CPF, cargo | ( ) |
| Contrato social e última alteração (ou estatuto e ata), para provar quem assina pela empresa | ( ) |

### Poderes

| Poder | Marcar quando |
|---|---|
| Gerais para o foro (ad judicia) e fora dele (et extra) | Sempre |
| Especiais: receber citação, confessar, reconhecer a procedência, transigir, desistir, renunciar, receber e dar quitação, firmar compromisso, assinar declaração de hipossuficiência (precisam constar expressamente — CPC, art. 105) | Quando a demanda exigir (acordo, levantamento de valores, gratuidade) |
| Representação perante Receita Federal e PGFN | Demandas tributárias (no e-CAC, além disso, a procuração eletrônica — POP-TRIB-02) |
| Finalidade | ( ) Geral ( ) Processo / demanda específica: ______ |

### Outorgados

Advogados do escritório que constam na procuração, com OAB: `[A CONFIRMAR lista e números de OAB]`.

## B. Contrato de honorários

| Dado | OK |
|---|---|
| Tipo: ( ) Assessoria mensal ( ) Tributário com êxito ( ) Causa única | ( ) |
| Dados do contratante (como na procuração) | ( ) |
| Escopo: o que está incluído e o que não está | ( ) |
| Valor fixo, forma de pagamento e dia de vencimento | ( ) |
| Êxito: percentual e base (tributário: 25% do proveito econômico para clientes novos; 10% para os antigos) | ( ) |
| Nota fiscal: antes ou depois do pagamento | ( ) |
| Reajuste, multa por atraso, vigência e rescisão | `[A CONFIRMAR cláusulas-padrão]` |
| Foro | `[A CONFIRMAR]` |
| Pessoa jurídica contratada (sociedade da Dra. Laís, CNPJ 58.232.242/0001-90, ou CNPJ do Dr. Alex) | `[A CONFIRMAR regra]` |

## C. Carta de preposição

| Dado | OK |
|---|---|
| Empresa: razão social, CNPJ, endereço | ( ) |
| Quem assina pela empresa (representante legal com poderes no contrato social) | ( ) |
| Preposto: nome, CPF, RG e função | ( ) |
| Processo: número, vara, nome da parte contrária, data da audiência | ( ) |
| Poderes: representar a empresa, prestar depoimento e **transigir** (fazer acordo) | ( ) |
| Documento com foto do preposto e cópia do contrato social para levar à audiência | ( ) |

Regras por justiça:
- **Trabalho**: o preposto não precisa ser empregado; deve conhecer os fatos, e o que disser obriga a empresa (CLT, art. 843, §§ 1º e 3º).
- **Juizado Especial Cível**: preposto credenciado com carta de preposição com poderes para transigir, sem necessidade de vínculo de emprego (Lei 9.099/1995, art. 9º, § 4º).
- **Audiência de conciliação no procedimento comum (cível)**: representante com procuração específica com poderes para negociar e transigir (CPC, art. 334, § 10).

## D. Substabelecimento

| Dado | OK |
|---|---|
| Com ou sem reserva de poderes | ( ) |
| Advogado(a) substabelecido(a) e OAB | ( ) |
| Processo | ( ) |

Salvar: procuração e contrato em `04 CLIENTES/{{cliente}}/01 CONTRATO E DOCUMENTOS/`; carta de preposição em `02 JUDICIAL/{{nº}}/01 DOCUMENTOS DO CLIENTE/`.
