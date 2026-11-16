# Automações do escritório Laís Torres & Alex Brunno

Stack combinada no kickoff: **ADVBOX + Infinitum (WhatsApp) + Asaas + Google Drive + Claude**, com uma
VPS de ~R$ 50/mês para o banco e o backup. Não há ferramenta paga nova no código. A única exceção é
a ZapSign, que fica opcional e desligada por padrão.

**Todo script roda em DRY-RUN por padrão**: mostra o que faria e não escreve em sistema nenhum. Só com
`--go` ele cria cobrança, Pix, nota, tarefa, pasta ou mensagem. Com `--go`, o script **recusa** rodar
em cima de um arquivo `*.example.json`.

```
automacoes/
├── comum/          clientes das APIs (Asaas, ADVBOX, Infinitum, Drive), banco local, mensagens, nomes, modelos
├── financeiro/     régua de cobrança, nova cobrança/12 boletos, NF, relatório diário, Pix da equipe
├── rh/             checklist por vínculo, pasta, contrato a partir de modelos/, assinatura plugável
├── drive/          estrutura do Drive, documento do WhatsApp -> pasta + tarefa, receptor de webhook, migração do ADVBOX
├── controladoria/  DJEN por OAB -> classificação -> prazo -> tarefa no ADVBOX
├── backup/         backup semanal (banco + conversas + cadastros), exportação do Infinitum
├── pecas/          extração de texto para o agente revisor-pecas
├── atendimento/    andamento do processo no ADVBOX (leitura)
└── testes/         teste offline com dados fictícios
```

Os agentes do Claude Code estão em `.claude/agents/`: `financeiro`, `rh`, `controladoria`,
`revisor-pecas` e `atendimento`. Cada um diz quais scripts usa.

---

## 1. Instalação

### Na máquina do escritório (Windows) e na VPS (Ubuntu 22.04+)

```bash
python -m venv venv
# Windows: venv\Scripts\activate     |  Linux: source venv/bin/activate
pip install -r requirements.txt
python automacoes/testes/teste_offline.py      # tem que terminar com "TUDO OK"
```

### Configuração

1. `config/.env.example` → `config/.env` (credenciais). Chave do Asaas **entre aspas simples**.
2. `config/escritorio.example.json` → `config/escritorio.json` (OABs, IDs do ADVBOX, raiz do Drive,
   dados fiscais do contador, aprovador, modo de envio).
3. `config/clientes.example.json` → `config/clientes.json` (cada cliente: contato financeiro, regra
   da NF, processos, demandas).
4. `config/colaboradores.example.json` → `config/colaboradores.json` e
   `config/despesas_fixas.example.json` → `config/despesas_fixas.json`.
5. Google Drive: criar no Google Cloud do Workspace do escritório um "ID do cliente OAuth" do tipo
   **app para computador**, salvar como `config/oauth_google.json` e rodar uma vez, na máquina do
   escritório, `python automacoes/drive/criar_estrutura.py base`. Isso abre o navegador para o login e
   gera `config/token_google.json`. Depois é só copiar o token para a VPS.
6. ADVBOX: com o token configurado, abrir `GET /settings` para anotar os IDs de usuários e tipos de
   tarefa em `escritorio.json -> advbox`. Cadastrar no ADVBOX: um processo interno "ADMINISTRATIVO"
   (para as tarefas de RH e financeiro), um registro de assessoria/consultivo por cliente de
   assessoria e os tipos de tarefa `[PRAZO]`, `[CONFIRMAR CLASSIFICAÇÃO]`, `[DOCUMENTO]`, `[RH]`,
   `[FINANCEIRO]`, `[CUSTAS]` e `[AUDIÊNCIA]`. **A API do ADVBOX só cria tarefa dentro de um processo.**

`.env`, tokens e os `config/*.json` reais estão no `.gitignore`. O repositório é público: nada disso
pode ser versionado.

---

## 2. Financeiro (`automacoes/financeiro/`)

| Script | O que faz |
|---|---|
| `notificacoes_asaas.py` | Desliga as notificações do Asaas dos clientes que já existem (as que dispararam os 12 avisos). Rodar uma vez na implantação. |
| `nova_cobranca.py` | Cria cliente e cobrança a partir de dados mínimos. O cliente nasce com `notificationDisabled=true`. Avulso: `--parcelas N`. Assessoria: `--assessoria --meses 12` registra **12 boletos mensais**, um por mês, que aparecem no DDA do cliente. Valida CPF/CNPJ e é idempotente pela `externalReference`. |
| `regua_cobranca.py` | Lembretes **10, 5 e 3 dias antes e no dia** do vencimento, com link de pagamento, e "pagamento recebido". Os textos vêm de `mensagens/MSG-07`. O lembrete de atraso fica desligado até a Dra. Laís confirmar. Mensagem com dado faltando não sai: vira pendência. |
| `nota_fiscal.py` | NFS-e pelo Asaas por cliente: `nf.quando = "antes"` (a nota sai na janela de 10 dias e o link vai no lembrete) ou `"depois"` (a nota sai quando o pagamento é confirmado). O PDF vai ao cliente pelo WhatsApp. Travas: data de corte, idempotência e dados fiscais completos. |
| `relatorio_diario.py` | Entradas, saídas, inadimplentes, margem e custo da equipe, em `.md` e `.xlsx`. Pode subir para o Drive e mandar o resumo à Dra. Laís. O que passa fora do Asaas (Nubank) entra por `dados/lancamentos_manuais.csv`. |
| `pagamentos.py` | Pix agendado da equipe e das despesas fixas (`agendar`), lista do dia para aprovar (`aviso-do-dia`), alerta de saldo (`saldo`), comprovantes para o Drive (`comprovantes`) e boleto de despesa (`boleto`). |

### Envio do WhatsApp pelo Infinitum: o que a API permite

A API pública do Infinitum **não tem endpoint para enviar mensagem**, e o Casal da IA não achou
nenhum nos testes com token real (09/2026). Por isso há dois modos (`escritorio.json -> mensageria.modo`):

- **`fila`** (padrão, funciona hoje): cada mensagem vai para `dados/fila_mensagens.jsonl` e para
  `dados/saida/fila_mensagens_AAAA-MM-DD.csv`, com telefone e texto prontos. A equipe envia pelo
  Infinitum.
- **`infinitum_card`**: o script cria um card num POP "ENVIOS AUTOMÁTICOS", com os campos telefone e
  mensagem. No Infinitum, a automação nativa do POP ("Um card for criado" → "Envie WhatsApp da
  organização") manda a mensagem. **A conferir na tela do Infinitum:** se essa ação aceita o telefone e
  o texto vindos dos campos do card. Confirmado isso, basta trocar o modo.

### Autorização do Pix por token no Asaas (conferido na documentação em 16/11/2026)

- `POST /v3/transfers` com `pixAddressKey`, `pixAddressKeyType` e `scheduleDate` (AAAA-MM-DD) cria o
  Pix agendado.
- Quando a conta tem a **validação de eventos críticos por token** (app Asaas ou SMS) ligada, a
  transferência fica pendente até ser autorizada. A referência da API diz que o campo `authorized` é
  "false quando aguarda autorização através do Token SMS". O FAQ de transferências diz que "a
  transferência pode permanecer pendente até a autorização".
- É esse o fluxo combinado: o script agenda, a Dra. Laís recebe às 8h a lista do dia e **aprova no app
  ou no painel com o token**. Nada sai sem esse toque.
- A documentação também oferece um "mecanismo de validação de saque via webhook", em que um servidor
  aprova sozinho. **Não usamos**, porque tiraria a aprovação humana. Ela recomenda ainda a **whitelist
  de IPs**: cadastre o IP da VPS na chave de API.
- **[A CONFERIR na conta deles]**: se o token está ligado para transferências criadas pela API e por
  qual canal ele chega. A própria documentação diz que isso "depende da operação, das configurações
  da conta e do endpoint". Homologar antes no sandbox, onde o token é `000000`.
- O Asaas não tem cadastro de "favorecido" pela API. Os favorecidos ficam em `config/colaboradores.json`
  e `config/despesas_fixas.json`, e cada Pix leva a chave.

---

## 3. RH (`automacoes/rh/colaborador.py`)

O passo a passo do POP-ADM-01: `checklist`, `novo` (cria a pasta `RH/NOME - VINCULO/01..05`, manda a
mensagem com o checklist e abre as tarefas `[RH]`), `status`, `receber` (arquiva o documento na
subpasta certa e marca o item), `marcar`, `contrato`, `assinar` e `comprovante`.

- **Contrato**: o script usa os modelos de `modelos/` (Markdown com `{{chave}}`, blocos opcionais
  `{{#bloco}}…{{/bloco}}` e o texto entre `<!-- INICIO_DOCUMENTO -->` e `<!-- FIM_DOCUMENTO -->`) e gera
  `.md` e `.docx`. O **fiscal** barra o envio para assinatura se sobrar `{{…}}`, `[A CONFIRMAR]`,
  `[CONFERIR]` ou `XXX`.
- **Assinatura (pendente: o escritório não tem ferramenta confirmada)**: a camada é plugável
  (`rh/assinatura.py`).
  - `manual` (padrão, custo zero): gera o PDF e um roteiro para assinar pelo **gov.br**
    (assinador.iti.br).
  - `zapsign`: precisa do plano com API e do `ZAPSIGN_API_TOKEN`.
  - Para plugar outra ferramenta, basta escrever uma classe com `enviar()` e `status()`.
- O PDF sai pelo próprio Drive: o `.docx` sobe como Google Doc, é exportado em PDF e o intermediário é
  apagado. Assim não é preciso Word nem LibreOffice.

---

## 4. Drive (`automacoes/drive/`)

- `ESTRUTURA_DRIVE.md`: a árvore, a convenção de nomes e como o cliente de assessoria com várias
  demandas fica organizado (uma pasta por demanda em `03_EXTRAJUDICIAL`, com data e assunto).
- `criar_estrutura.py`: `base`, `cliente`, `processo`, `demanda`, `colaborador` e `docs` (sobe POPs,
  checklists, mensagens e modelos para `00_ESCRITORIO`). Idempotente e nunca apaga nada.
  `--offline` mostra só o plano.
- `documento_whatsapp.py`: recebe um documento, descobre o cliente pelo telefone, escolhe a pasta
  (processo pelo nº CNJ, demanda pela palavra-chave, documentos pessoais ou `99_A_CLASSIFICAR`), sobe o
  arquivo e cria a tarefa `[DOCUMENTO]` no ADVBOX com o link.
- `receptor_webhook.py`: servidor HTTP mínimo, sem dependência extra, que recebe o webhook do Infinitum,
  guarda o evento e chama o arquivamento.
  - **Depende do Infinitum**: no POP de atendimento, configurar a automação "Mensagem no WhatsApp → Crie
    card" (gravando telefone, texto e **anexo** em campos do card) e a integração "Enviar Webhook"
    quando o card for criado. **A conferir:** se o anexo pode ir para um campo do card.
  - Enquanto isso não for confirmado, roda-se manualmente com `--arquivo`.
- `migrar_docs_advbox.py`: copia para o Drive os documentos que hoje só existem no ADVBOX. Só lê do
  ADVBOX e não apaga nada.

---

## 5. Controladoria (`automacoes/controladoria/intimacoes.py`)

- **Fonte**: DJEN/Comunica do CNJ, gratuito, consultado pelas OABs de `escritorio.json -> controladoria.oabs`.
  A API oscila entre "ocupado" e um falso vazio, e o módulo tenta de novo com espera crescente.
- **Classificação** (`classificador.py`, por regras, sem IA): MERO_ANDAMENTO, EMBARGOS_DE_DECLARACAO,
  AGRAVO, APELACAO, RECURSO_ORDINARIO ou OUTROS (com subtipo: intimação para agir, custas, audiência,
  citação, acórdão, contrarrazões, recurso inominado, interlocutória sem recurso imediato).
  Cada resultado traz o gatilho, a base legal e a confiança. Sentença e decisão vêm com "também cabe
  embargos de declaração (5 dias úteis)".
- **Prazo** (`prazos.py`): publicação no 1º dia útil depois da disponibilização, contagem a partir do
  dia útil seguinte, dias úteis, suspensão de 20/12 a 20/01 e feriados nacionais. Prazo interno é o
  fatal menos 2 dias úteis; protocolo, o fatal menos 1 dia útil.
  - `feriados_locais.json` nasce **vazio**: a controladoria preenche com o calendário do TJMA, TJGO,
    TJTO, TJPA, TRT16, TRT18, TRT10 e TRF1 e das comarcas.
- **ADVBOX**: cria `[PRAZO] …` (fim = prazo interno, `date_deadline` = fatal) e
  `[CONFIRMAR CLASSIFICAÇÃO] …` para decisão, sentença ou acórdão.
  - A API **só cria tarefa em processo cadastrado** (`lawsuits_id` obrigatório). Processo sem
    cadastro vira pendência no relatório.
  - Tipos de tarefa e responsáveis por área vêm do `escritorio.json`.

---

## 6. Backup (`automacoes/backup/`)

- `backup_semanal.py` gera um `.tar.gz` com:
  - o banco local (cópia consistente do SQLite);
  - `dados/conversas/` (eventos do webhook do Infinitum);
  - a exportação do Infinitum;
  - filas e relatórios;
  - os cadastros.
- O arquivo é cifrado com `openssl` AES-256 e uma senha guardada **também fora da VPS**, mantido em
  rotação (8 semanas) e enviado para `00_ESCRITORIO/BACKUPS`.
- Sem cifra, o script não sobe nada para o Drive. `.env` e tokens não entram no backup.
- `exportar_infinitum.py`: salva o que a API do Infinitum expõe (POPs, campos, todos os cards com os
  valores, tarefas e cadastros, se responderem).

### Backup do WhatsApp: a API do Infinitum NÃO expõe o histórico de mensagens

Não existe endpoint de conversa ou mensagem na API pública do Infinitum (conferido com token real,
61 endpoints). O script salva o que a API dá, que são cards e cadastros, **não as conversas**.
Alternativas, da mais barata para a mais trabalhosa:

1. **Hoje, custo zero:** ligar o **backup nativo do WhatsApp Business para o Google Drive** em cada
   celular (Configurações → Conversas → Backup, diário, conta Google do escritório).
   - **A conferir com o suporte do Infinitum** como o número fica conectado (QR/WhatsApp Web ou API
     oficial). Se o app do celular continuar ativo, esse backup continua valendo.
2. **Pedir ao suporte do Infinitum** a exportação das conversas ou um webhook de mensagem. Se a
   automação "Mensagem no WhatsApp" puder disparar o webhook com o conteúdo, o `receptor_webhook.py`
   já grava tudo em `dados/conversas/` e isso entra no backup semanal.
3. **Exportação manual das conversas críticas** ("Exportar conversa" no app). Os `.zip` vão para
   `dados/conversas/exportacoes/` e entram no backup.
4. **Último recurso:** um gateway não oficial auto-hospedado na VPS (Evolution API, código aberto e
   sem licença) como aparelho vinculado, arquivando todas as mensagens. Funciona, mas é **não oficial**:
   tem risco de bloqueio do número e manutenção. Não recomendado sem decisão da Dra. Laís.

---

## 7. VPS: agendamentos (cron) e serviço

```cron
# m  h  dom mon dow   (horário de Brasília na VPS: timedatectl set-timezone America/Sao_Paulo)
0   7  *   *   *     cd /opt/escritorio && venv/bin/python automacoes/financeiro/relatorio_diario.py --go --drive --avisar
30  7  *   *   *     cd /opt/escritorio && venv/bin/python automacoes/financeiro/nota_fiscal.py --go
30  7  *   *   1-5   cd /opt/escritorio && venv/bin/python automacoes/controladoria/intimacoes.py --go --drive
0   8  *   *   *     cd /opt/escritorio && venv/bin/python automacoes/financeiro/regua_cobranca.py --go
0   8  *   *   *     cd /opt/escritorio && venv/bin/python automacoes/financeiro/pagamentos.py aviso-do-dia --go
0   9  *   *   1-5   cd /opt/escritorio && venv/bin/python automacoes/financeiro/pagamentos.py saldo --dias 2 --go
0   14 *   *   *     cd /opt/escritorio && venv/bin/python automacoes/financeiro/nota_fiscal.py --go
0   18 *   *   *     cd /opt/escritorio && venv/bin/python automacoes/financeiro/pagamentos.py comprovantes --mes $(date +\%Y-\%m) --go
0   10 25  *   *     cd /opt/escritorio && venv/bin/python automacoes/financeiro/pagamentos.py agendar --go
30  3  *   *   0     /opt/escritorio/automacoes/backup/backup_semanal.sh >> /var/log/escritorio-backup.log 2>&1
```

O `backup_semanal.sh` aceita `ESCRITORIO_BASE` e `ESCRITORIO_PY` pelo ambiente, para mudar a pasta e o
Python. O padrão é `/opt/escritorio`. **Só ligue um cron depois que o mesmo comando rodar em dry-run com
resultado conferido.**

Receptor de webhook (systemd), atrás de nginx ou caddy com HTTPS:

```ini
# /etc/systemd/system/escritorio-webhook.service
[Unit]
Description=Receptor de webhook do Infinitum
After=network.target
[Service]
WorkingDirectory=/opt/escritorio
ExecStart=/opt/escritorio/venv/bin/python automacoes/drive/receptor_webhook.py --porta 8085 --go
Restart=always
[Install]
WantedBy=multi-user.target
```

---

## 8. Testes

`python automacoes/testes/teste_offline.py` testa, sem rede e sem credencial, com dados fictícios:

- régua (marcos, leitura do MSG-07, lacuna que não sai);
- relatório;
- 12 boletos e parcelas;
- NF (travas);
- Pix (datas);
- motor de prazos;
- classificador (11 casos, incluindo a armadilha do cabeçalho do PJe);
- controladoria completa;
- estrutura e roteamento do Drive;
- modelos e fiscal;
- checklists.

Os scripts também aceitam dados fictícios na própria linha de comando:
`regua_cobranca.py --fixture automacoes/testes/fixture_asaas.json --data 2026-12-05`,
`intimacoes.py --arquivo automacoes/testes/fixture_djen.json`.

---

## 9. Pendências `[A CONFIRMAR]`

- **Infinitum**: se a automação "Envie WhatsApp" aceita telefone e texto vindos de campos do card; se a
  automação "Mensagem no WhatsApp → Crie card" grava o anexo; exportação ou webhook de conversas; como
  os números estão conectados.
- **Asaas**: token de eventos críticos ligado para transferências pela API e o canal (app ou SMS); se a
  NF sai por e-mail ao cliente com `notificationDisabled=true`; se a emissão automática de NF está
  ligada no painel (duplicaria).
- **Contador**: código do serviço municipal, alíquotas (ISS, PIS, COFINS, CSLL, INSS, IR, retenção) e
  data de corte da NF.
- **Dra. Laís**:
  - lista de clientes com valor, vencimento e regra da NF (antes ou depois);
  - lembretes de atraso (dias e tom);
  - multa e juros;
  - equipe (vínculo, valor, dia e chave Pix informada por cada um);
  - despesas fixas;
  - ferramenta de assinatura;
  - quem assina pelo escritório.
- **Controladoria**: OABs do Dr. Alex, da Dra. Larissa e da Dra. Jaqueline; feriados locais conferidos
  nos tribunais.
- **POPs**: atualizar os nomes de pasta para os de `drive/ESTRUTURA_DRIVE.md` (os POPs v1 usam `02 RH`,
  `03 FINANCEIRO/AAAA-MM`, `04 CLIENTES`…).
