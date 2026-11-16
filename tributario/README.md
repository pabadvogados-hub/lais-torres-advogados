# Kit tributário — Laís Torres & Alex Brunno Advogados

Tudo o que o produto de **transação tributária na PGFN** do Dr. Alex usa para vender e executar: produto e
comercial, método, banco de teses, banco de leis, motor de prospecção, raio-x por CNPJ, IA do relatório de
passivo e o avaliador da CAPAG. Faz parte do **Módulo 8** do `PROJETO_IMPLANTACAO.md`. Versão de 16/11/2026.

Os **POPs oficiais** do tributário são os do repositório: `pops/POP-TRIB-01` a `POP-TRIB-06`. Este kit é a
caixa de ferramentas que eles usam.

## O que tem aqui

| Pasta | O que é | Como usar |
| --- | --- | --- |
| [`produto/`](produto/PRODUTO_E_COMERCIAL.md) | Produto, preço, papéis da equipe, funil, qualificação, metas e implantação em 90 dias | Ler primeiro |
| [`metodo/`](metodo/METODO.md) | Método em 6 etapas, regras da CAPAG, vetores contestáveis, documentos e prazos | Consulta do dia a dia |
| [`teses/`](teses/00_INDICE.md) | 21 teses (remessa à DAU, CAPAG, parcelamento, prescrição, CDA, execução, sócios, Simples, transação) | `teses/TEMAS/00_BANCO_DE_TESES_POR_TEMA.md` |
| [`leis/`](leis/00_INDICE.md) | 19 normas em texto vigente, cortadas por artigo, com busca | `python tributario/leis/buscar_lei.py PORT6757 34-B` |
| [`motor/`](motor/README.md) | Prospecção: dados abertos da PGFN + BrasilAPI, nota de 0 a 100, favorece MA, PA, TO e GO | `python tributario/motor/motor_autonomo.py` |
| [`consulta/`](consulta/consultar_cnpj.py) | Raio-x de uma empresa (cadastro, sócios, inscrições) em HTML para a reunião de diagnóstico | `python tributario/consulta/consultar_cnpj.py <cnpj>` |
| [`capag/`](capag/avaliar_capag.py) | Avaliador da CAPAG: diz se vale pedir a revisão (arts. 21 a 34-B da Portaria 6.757) | `python tributario/capag/avaliar_capag.py tributario/capag/exemplo_caso.json` |
| [`ia/`](ia/system_prompt_tributarista.md) | Instrução do relatório de passivo fiscal (e-CAC, Regularize, CDAs, execução) | Colar como instrução no Claude e anexar os PDFs |
| [`painel/`](painel/index.html) | Painel visual com o fluxo, a equipe, o comercial, os POPs de referência, as teses, as leis e a CAPAG | Abrir no navegador |

Na raiz do repositório, em `.claude/`, ficam os agentes **`avaliador-capag`** e **`peca-tributaria`** e a
skill **`triagem-tributaria`**. Abra o Claude Code na pasta do repositório para usá-los.

## Onde cada ferramenta entra nos POPs

| POP | Ferramenta |
| --- | --- |
| TRIB-01 Primeiro contato e diagnóstico | `motor/` (lista de leads), `consulta/` (raio-x antes da reunião), skill `triagem-tributaria` |
| TRIB-02 Procuração e levantamento | `ia/` (relatório de passivo a partir dos PDFs do e-CAC e do Regularize) |
| TRIB-03 Análise, CAPAG e parecer | agente `avaliador-capag` + `capag/`, `teses/`, `leis/`, agente `peca-tributaria` |
| TRIB-04 Proposta e fechamento | `produto/` (objeções e preço), `modelos/06_contrato_tributario_exito.md` |
| TRIB-05 Adesão e medidas preparatórias | agente `peca-tributaria` (remessa, revisão da CAPAG, requerimento do art. 14-A) |
| TRIB-06 Acompanhamento mensal | `teses/` T17 e T18 (farol, rescisão e impedimento de 2 anos) |

## Como as peças se encaixam

```
motor/ acha a empresa  ->  consulta/ faz o raio-x para a reunião  ->  triagem-tributaria organiza a conversa
  ->  ia/ gera o relatório de passivo com os PDFs do cliente  ->  avaliador-capag decide se pede revisão
  ->  peca-tributaria redige (teses/ + leis/)  ->  revisor-pecas faz a 1ª correção  ->  Dr. Alex revisa e assina
```

## O avaliador da CAPAG

`capag/avaliar_capag.py` confere o que é objetivo:

- o prazo de 30 dias (art. 29);
- a trava do novo pedido (art. 34-B);
- a comparação entre a CAPAG presumida, a capacidade estimada pelo fluxo de caixa e o passivo total (art. 21);
- os créditos que já são irrecuperáveis pelo art. 25, como os inscritos há mais de 15 anos sem garantia ou com
  execução arquivada pelo art. 40 da LEF há mais de 3 anos;
- os documentos do art. 30 que faltam;
- o DFC feito pelo método indireto.

O agente `avaliador-capag` lê os documentos do cliente, monta o `caso.json`, roda o script e completa o
parecer com os vetores contestáveis, a via escolhida e o cronograma.

Ele **não calcula a faixa A/B/C/D**, porque a fórmula da PGFN não é pública. A faixa sai do Regularize.

## Regras que valem para tudo

- Edital, data de corte, teto e entrada são conferidos no Regularize **no dia de cada caso**. Nunca de memória.
- Faixas A e B não têm desconto, só entrada facilitada. O desconto está em C e D.
- Revisão da CAPAG só com ganho de faixa confirmado. Julgado o pedido, um novo só cabe com fato superveniente
  ou mudança substancial da CAPAG presumida (art. 34-B). A ideia de "CAPAG efetiva irreversível pelo art. 30"
  está errada.
- Transação rescindida veda nova transação por 2 anos (Lei 13.988/2020, art. 4º, § 4º; Portaria PGFN
  6.757/2022, art. 18).
- Teses marcadas `conferir` precisam do inteiro teor antes de ir para a peça. Nenhum número de processo foi inventado.
- Nunca prometer porcentagem de desconto ao lead. Honorário só o Dr. Alex informa.
- Tudo é minuta: nada é protocolado nem enviado ao cliente sem a revisão do Dr. Alex.

## O que fica fora do repositório

O repositório é público. Por isso ficam fora do git (ver `.gitignore`):

- a lista de leads do motor (`motor/leads/`) e os dados da PGFN (`motor/data/`);
- os raio-x gerados (`consulta/saida/`) e os casos de CAPAG (`capag/casos/`), que têm dado de cliente.

Documento de cliente mora no Drive, em `CLIENTES/<CLIENTE>/05_TRIBUTARIO/`.

## Requisitos

Python 3.10 ou mais novo, só a biblioteca padrão. O banco de leis já vem pronto (`leis/banco_leis.db`).
O raio-x por CNPJ lê o trimestre inteiro da PGFN (cerca de 8 GB de CSV). Cada consulta leva de 20 a 25 minutos,
então rode antes da reunião (de preferência na VPS).
