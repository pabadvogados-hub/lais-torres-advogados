# POP-TRIB-01 — Tributário: primeiro contato e reunião de diagnóstico

Versão 1 — 16/11/2026

| | |
|---|---|
| **Dono do POP** | Dr. Alex |
| **Quem executa** | Comercial `[A CONFIRMAR quem]` (primeiro contato e agendamento); Dr. Alex (reunião de diagnóstico) |
| **Gatilho** | Lead de tráfego pago do produto tributário, lead da lista do motor (`tributario/motor/`), indicação, ou cliente de assessoria com passivo apontado no `CK-DIAG-02` |
| **Termina quando** | Procuração no e-CAC concedida e POP-TRIB-02 iniciado, ou retorno marcado, ou lead em nutrição |
| **Prazo** | Primeiro contato em 5 minutos; reunião em até 2 dias úteis; cadência de até 15 dias |

## Objetivo

Transformar o lead (ou o cliente da casa com dívida tributária) em procuração no e-CAC, que é o que
permite levantar o passivo e calcular a CAPAG. Todas as oficinas e autopeças que passaram pelo
escritório têm débitos altos que nunca foram trabalhados: **cliente de assessoria também passa por este POP**.

## Automação x pessoa

| A automação faz | A pessoa faz |
|---|---|
| Primeira mensagem em até 5 minutos (MSG-05, modelo 1-T) | Assume a conversa e qualifica |
| Toques de follow-up da cadência (MSG-05) | Ligações da cadência |
| Raio-x do CNPJ (`python tributario/consulta/consultar_cnpj.py <cnpj>`: cadastro, sócios e inscrições na PGFN) e triagem (skill `triagem-tributaria`) | Confere e leva para a reunião |
| Lembretes da reunião (véspera e 1 hora antes) | Confirma presença e recupera falta |

## Passo a passo

1. **Responder em até 5 minutos** pelo número comercial (POP-ATD-02 define qual número e qual
   identidade). A primeira frase diz quem somos. — *5 min*
2. **Preencher os campos do card** no Infinitum: CNPJ, valor aproximado da dívida, regime (Simples,
   Presumido, Real), situação (dívida ativa, execução, parcelamento, bloqueio), gatilho (o que fez
   procurar agora), quem decide, reunião marcada. — *até 24h*
3. **Seguir a cadência** se não houver resposta: D0 texto; D1 áudio curto; D3 ligação; D5 conteúdo
   sobre transação; D8 ligação; D11 "ainda faz sentido?"; D15 despedida e nutrição. — *até 15 dias*
4. **Marcar a reunião de diagnóstico** (20 a 30 minutos, vídeo) com duas opções de horário.
   Confirmar ao marcar, na véspera e 1 hora antes. Pedir que o decisor tenha o **gov.br (prata ou ouro)**
   à mão, porque a procuração é feita ali. — *reunião em até 2 dias úteis*
5. **Deixar no card a consulta pública**: dívida ativa da União, execuções fiscais e situação do CNPJ,
   para o Dr. Alex abrir na reunião. Rodar o raio-x (`tributario/consulta/consultar_cnpj.py`, leva de 20 a
   25 minutos) e a skill `triagem-tributaria`, que organiza o que já se sabe e o que perguntar. — *véspera*
6. **Reunião (Dr. Alex)**: — *20 a 30 min*
   1. Entender a empresa e a dívida (no máximo 5 minutos de conversa inicial).
   2. Mostrar na tela o que está público: inscrições, execuções, situação.
   3. Deixar o cliente dizer o que acontece se nada mudar (bloqueio, penhora, certidão negada, contrato perdido).
   4. Explicar que existe negociação oficial com a PGFN (transação), **sem citar percentual de desconto**.
   5. Explicar que o diagnóstico depende da procuração no e-CAC: sem o extrato completo não há como
      saber a CAPAG nem o desconto possível.
   6. Pedir a procuração **na própria reunião**, com o passo a passo no gov.br.
7. **Fechar o dia**: registrar dores e objeções no card, confirmar a procuração e iniciar o
   POP-TRIB-02. Sem procuração: retorno marcado em até 24h. — *mesmo dia*

## Regras

- Nenhum robô, estagiário ou comercial fala em percentual de desconto ou promete resultado.
- Honorário só é informado pelo Dr. Alex (POP-TRIB-04).
- O diagnóstico é cobrado ou gratuito? `[A CONFIRMAR]` (no modelo de referência, o parecer é vendido
  e o valor é abatido dos honorários se o cliente fechar).

## O que vira tarefa no ADVBOX

Lead fica no Infinitum. Cliente de assessoria: `[TRIB] Reunião de diagnóstico tributário - {{cliente}}` para o Dr. Alex.

## Onde salva no Drive

Lead: `00_ESCRITORIO/COMERCIAL/{{AAAA-MM}}/{{lead}}/`. Cliente da casa: `CLIENTES/{{cliente}}/05_TRIBUTARIO/`.

## Pendências `[A CONFIRMAR]`
- Diagnóstico cobrado ou gratuito; valor.
- Quem faz o primeiro contato e o agendamento.
