# Estrutura do Drive do escritório

Versão 1 (16/11/2026). Quem cria as pastas é o script `automacoes/drive/criar_estrutura.py`. Os
nomes vêm de um arquivo só, `automacoes/drive/estrutura_drive.json`: se um nome mudar lá, muda em
todos os scripts.

**Regra de ouro:** o documento fica no Drive, e no ADVBOX vai só o link. Se o ADVBOX sair, o acervo
continua inteiro no Drive. A API do ADVBOX nem permite enviar documento, só ler.

## A árvore

```
DRIVE DO ESCRITÓRIO (pasta raiz = escritorio.json -> drive.raiz_id)
├── 00_ESCRITORIO
│   ├── POPS                 cópia dos POPs (pops/*.md)
│   ├── CHECKLISTS           checklists de diagnóstico e do dia a dia
│   ├── MODELOS
│   │   ├── CLIENTES         procuração, contratos de honorários, preposição, notificação
│   │   ├── RH               termo de estágio, contrato de associação
│   │   └── PECAS            modelos de peça e base de teses
│   ├── MENSAGENS            modelos de mensagem (MSG-01 a MSG-07)
│   ├── CONTROLADORIA/AAAA/MM   relatório diário da controladoria
│   ├── COMERCIAL            leads e propostas
│   ├── ENTRADA_WHATSAPP     documento de número sem cadastro (a triagem decide o destino)
│   └── BACKUPS              backup semanal da VPS (cifrado)
├── RH
│   └── NOME COMPLETO - VINCULO          (ESTAGIARIO | ASSOCIADO | EMPREGADO | APOIO)
│       ├── 01_DOCUMENTOS_PESSOAIS
│       ├── 02_CONTRATO_E_ADITIVOS       contrato assinado, averbação OAB, apólice do seguro
│       ├── 03_PAGAMENTOS                AAAA-MM_comprovante.pdf
│       ├── 04_RELATORIOS_E_AVALIACOES   relatório semestral de estágio
│       └── 05_DESLIGAMENTO
├── FINANCEIRO
│   └── AAAA
│       └── MM
│           ├── RELATORIOS        relatório diário (.md e .xlsx)
│           ├── COMPROVANTES      comprovantes de despesas fixas
│           └── NOTAS_FISCAIS
└── CLIENTES
    └── NOME DO CLIENTE (razão social ou nome completo, em maiúsculas)
        ├── 01_CONTRATO_E_DOCUMENTOS       contrato de honorários, procuração, documentos pessoais e societários
        ├── 02_JUDICIAL
        │   └── 0801234-56.2026.8.10.0040 - PARTE CONTRÁRIA - TIPO DE AÇÃO
        │       ├── 01_DOCUMENTOS_DO_CLIENTE
        │       ├── 02_PECAS               minutas, PARECER IA, versão protocolada
        │       ├── 03_DECISOES_E_INTIMACOES
        │       └── 04_CUSTAS_E_GUIAS
        ├── 03_EXTRAJUDICIAL
        │   └── AAAA-MM-DD - ASSUNTO CURTO          uma pasta por DEMANDA
        │       ├── 01_DOCUMENTOS_RECEBIDOS
        │       ├── 02_PRODUCAO                     minutas, pareceres, notificações em elaboração
        │       └── 03_ENTREGUE                     o que foi enviado ao cliente (versão final)
        ├── 04_ASSESSORIA_DIAGNOSTICO      só cliente de assessoria: checklists de entrada e plano
        ├── 05_TRIBUTARIO                  só quando houver demanda tributária
        │   ├── 01_DOCUMENTOS_FISCAIS
        │   ├── 02_RELATORIOS
        │   └── 03_PETICOES
        └── 99_A_CLASSIFICAR               o que chegou e o robô não soube onde pôr (inclui MIGRADO_ADVBOX)
```

## Clientes de assessoria com várias demandas

O cliente de assessoria traz demanda nova toda semana. A estrutura trata isso assim:

1. **Cada demanda extrajudicial tem uma pasta própria**, com data de abertura e assunto:
   `03_EXTRAJUDICIAL/2026-11-18 - NOTIFICACAO FORNECEDOR X`. Ela nunca se mistura com outra, e a
   data na frente deixa a lista em ordem cronológica.
2. **Cada demanda que vira processo** ganha a pasta do processo em `02_JUDICIAL`. A pasta da demanda
   extrajudicial fica onde está, como histórico.
3. **A demanda é registrada em `config/clientes.json`** (`demandas_extrajudiciais`: assunto, data,
   palavras-chave, área, id do registro no ADVBOX). Com as palavras-chave, o documento que chega pelo
   WhatsApp com a legenda "segue a nota do fornecedor X" cai sozinho na pasta certa.
4. **Demanda encerrada** recebe `encerrada_em` no cadastro. A pasta continua no lugar, mas deixa de
   receber documentos automáticos.
5. **No ADVBOX**, toda tarefa precisa de um processo (`lawsuits_id` é obrigatório na API). Por isso
   cada cliente de assessoria tem **um registro de "processo" do tipo assessoria/consultivo**
   (`advbox.registro_assessoria_lawsuit_id`), onde ficam as tarefas extrajudiciais. A demanda grande
   pode ter registro próprio (`demandas_extrajudiciais[].advbox_lawsuit_id`).

Criar uma demanda nova:

```
python automacoes/drive/criar_estrutura.py demanda --cliente <id> --assunto "notificacao fornecedor X" --go
```

## Convenção de nomes de arquivo

| O quê | Padrão | Exemplo |
|---|---|---|
| Documento em geral | `AAAA-MM-DD_TIPO_descricao-curta.ext` | `2026-11-16_GUIA-CUSTAS_diligencia-oficial.pdf` |
| Documento recebido do cliente | `AAAA-MM-DD_DOC-CLIENTE_<legenda>.ext` | `2026-11-16_DOC-CLIENTE_contrato-social.pdf` |
| Peça (minuta) | `MINUTA - TIPO - CLIENTE - Nº DO PROCESSO - AAAA-MM-DD.docx` | `MINUTA - CONTESTACAO - EMPRESA X - 0801234-56.2026.8.10.0040 - 2026-11-16.docx` |
| Peça protocolada | `TIPO - CLIENTE - Nº DO PROCESSO - AAAA-MM-DD.docx/.pdf` | |
| Parecer da 1ª correção | `PARECER IA - <nome da minuta>.md` | |
| Comprovante de pagamento da equipe | `AAAA-MM_comprovante.pdf` | `2026-12_comprovante.pdf` |
| Relatório financeiro | `AAAA-MM-DD_relatorio_financeiro.md/.xlsx` | |
| Relatório da controladoria | `AAAA-MM-DD_relatorio-controladoria.md` | |

Regras: data sempre `AAAA-MM-DD` na frente (ordena sozinho); sem `/ \ : * ? " < > |`; descrição
curta, sem acento, com hífen (o script faz isso).

## Como o documento do WhatsApp chega à pasta (`documento_whatsapp.py`)

1. Telefone → cliente (cadastro). Número sem cadastro vai para `00_ESCRITORIO/ENTRADA_WHATSAPP`.
2. Nº de processo na legenda → pasta do processo (`01_DOCUMENTOS_DO_CLIENTE`).
3. Palavra-chave de uma demanda aberta → pasta da demanda (`01_DOCUMENTOS_RECEBIDOS`).
4. RG, CPF, CNH, contrato social, comprovante de endereço, procuração → `01_CONTRATO_E_DOCUMENTOS`.
5. Cliente com um só caso → pasta desse caso.
6. Fora disso → `99_A_CLASSIFICAR`, com tarefa no ADVBOX para alguém classificar.

Em todos os casos é criada a tarefa `[DOCUMENTO] Documento recebido - <cliente> - <processo/assunto>`,
com o link do Drive e prazo de 1 dia útil.

**Depende do Infinitum:** a API pública dele não entrega mensagem nem anexo. Para o automático, o
POP de atendimento do Infinitum precisa de uma automação "Mensagem no WhatsApp → Crie card" que grave
o anexo num campo do card, e de uma integração "Enviar Webhook" para a VPS (`receptor_webhook.py`).
**A conferir na tela do Infinitum:** se o anexo pode ir para um campo do card. Enquanto isso não for
confirmado, roda-se manualmente: `documento_whatsapp.py --arquivo ... --telefone ... --legenda ...`.

## POPs e checklists

Em 16/11 os POPs, checklists e mensagens foram alinhados a estes nomes (129 trocas em 26 arquivos).
Se um nome mudar no `estrutura_drive.json`, atualize também `pops/README.md` (seção 4.2).
