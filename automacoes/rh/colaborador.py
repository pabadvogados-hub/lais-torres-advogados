# -*- coding: utf-8 -*-
"""Agente de RH — admissao e regularizacao da equipe (POP-ADM-01).

Cadastro: config/colaboradores.json (um registro por pessoa: id, nome, vinculo, whatsapp, e-mail,
pagamento, dados_contrato com as {{chaves}} do modelo). Vinculos: estagiario | associado |
empregado | apoio. Checklist por vinculo: automacoes/rh/checklists_vinculo.json.

Subcomandos:
  checklist   --vinculo estagiario|associado|empregado|apoio      mostra o checklist
  novo        --id ID       pasta no Drive (RH/NOME - VINCULO/01..05), mensagem ao colaborador com
                            o checklist, tarefas [RH] no ADVBOX
  status      --id ID | --todos   o que falta de cada um
  receber     --id ID --item CHAVE --arquivo F   sobe o documento na subpasta certa e marca o item
  marcar      --id ID --item CHAVE [--nao-se-aplica]
  contrato    --id ID [--modelo modelos/09_...md] [--dados extra.json]
              gera o contrato do modelo (Markdown {{chave}}) em .md e .docx e confere o que falta
  assinar     --id ID       converte em PDF (pelo Drive) e manda para assinatura (provedor plugavel)
  comprovante --id ID --mes AAAA-MM --arquivo F   arquiva comprovante em 03_PAGAMENTOS
              (os comprovantes do Pix do Asaas sao arquivados por financeiro/pagamentos.py comprovantes)

Dry-run por padrao; --go grava no Drive/ADVBOX/fila e no banco local.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import assinatura  # noqa: E402
from comum import advbox, db, drive, mensageria, modelos  # noqa: E402
from comum.cadastros import colaborador_por_id, colaboradores, lista_colaboradores, pasta_do_colaborador  # noqa: E402
from comum.config import (MODELOS_DIR, SAIDA_DIR, add_modo, agora_iso, banner, bloquear_exemplo,  # noqa: E402
                          data_br, escritorio, garantir_dir, hoje, utf8_stdout)
from comum.nomes import nome_arquivo  # noqa: E402

CHECK = json.loads((Path(__file__).with_name("checklists_vinculo.json")).read_text("utf-8"))


def _col(cid: str) -> dict:
    c = colaborador_por_id(cid)
    if not c:
        raise SystemExit(f"colaborador {cid} nao esta em config/colaboradores.json")
    if (c.get("vinculo") or "").lower() not in CHECK:
        raise SystemExit(f"{cid}: vinculo '{c.get('vinculo')}' invalido (use {', '.join(k for k in CHECK if k[0] != '_')})")
    return c


def _ck(c: dict) -> dict:
    return CHECK[c["vinculo"].lower()]


def _uteis(d: date, n: int) -> date:
    while n:
        d += timedelta(days=1)
        if d.weekday() < 5:
            n -= 1
    return d


def marcas(con, cid: str) -> dict:
    out = {}
    for r in con.execute("SELECT evento, detalhe FROM rh_eventos WHERE colaborador=? ORDER BY criado_em", (cid,)):
        if r["evento"].startswith("item:"):
            out[r["evento"][5:]] = r["detalhe"]
    return out


def _tarefa(cfg, titulo, prazo, executar):
    adv = cfg.get("advbox") or {}
    return advbox.criar_tarefa(adv.get("processo_administrativo_id"), (adv.get("tipos_tarefa") or {}).get("rh"),
                               [(adv.get("responsaveis") or {}).get("rh")], adv.get("usuario_robo_id"), titulo,
                               start_date=hoje().isoformat(), date_deadline=prazo, executar=executar)


def _svc_raiz(cfg):
    raiz = (cfg.get("drive") or {}).get("raiz_id")
    if raiz and drive.credenciais_disponiveis():
        return drive.servico(), raiz
    return None, None


def cmd_checklist(a, cfg, con):
    ck = CHECK[a.vinculo]
    print(f"Checklist — {ck['rotulo']} (modelo: {ck.get('modelo') or '[A DEFINIR]'})")
    for d in ck["documentos"]:
        print(f"  [ ] {d['item']}{' (se houver)' if d.get('opcional') else ''}   -> {d['pasta']}  ({d['chave']})")


def cmd_novo(a, cfg, con):
    c = _col(a.id)
    ck = _ck(c)
    base = ["RH", pasta_do_colaborador(c)]
    svc, raiz = _svc_raiz(cfg)
    estrutura = json.loads((Path(__file__).resolve().parents[1] / "drive" / "estrutura_drive.json").read_text("utf-8"))
    if svc:
        for sub in [[]] + [[s] for s in estrutura["colaborador"]]:
            drive.garantir_caminho(svc, raiz, base + sub, executar=a.go)
    else:
        print(f"  Drive indisponivel: a pasta seria {'/'.join(base)}/ com {', '.join(estrutura['colaborador'])}")
    itens = "\n".join(f"- {d['item']}" for d in ck["documentos"] if d["chave"] != "contrato")
    texto = (f"{(c.get('nome') or '').split(' ')[0].title()}, tudo bem? Para formalizarmos o seu "
             f"{ck['rotulo'].lower()} no escritório, precisamos dos itens abaixo (pode mandar foto ou PDF por aqui):\n"
             f"{itens}\n\nA chave Pix e os dados bancários devem ser informados por você mesmo(a), por escrito.")
    mensageria.enviar(c.get("whatsapp"), texto, origem="rh", referencia=c["id"], executar=a.go, cfg=cfg)
    nome = c.get("nome")
    print("  ADVBOX:", _tarefa(cfg, f"[RH] Documentos - {nome}", _uteis(hoje(), 3).isoformat(), a.go))
    inicio = c.get("inicio")
    print("  ADVBOX:", _tarefa(cfg, f"[RH] Contrato assinado - {nome}", inicio or _uteis(hoje(), 5).isoformat(), a.go))
    if a.go:
        con.execute("INSERT INTO rh_eventos VALUES (?,?,?,?)", (c["id"], "novo", "", agora_iso()))
        con.commit()


def cmd_status(a, cfg, con):
    alvos = lista_colaboradores() if a.todos else [_col(a.id)]
    for c in alvos:
        if (c.get("vinculo") or "").lower() not in CHECK:
            print(f"\n{c.get('nome')}: vinculo '{c.get('vinculo')}' nao definido — [A CONFIRMAR]")
            continue
        ck = _ck(c)
        m = marcas(con, c["id"])
        feitos = sum(1 for d in ck["documentos"] if m.get(d["chave"]) in ("ok", "nao_se_aplica"))
        print(f"\n{c.get('nome')} — {ck['rotulo']}: {feitos}/{len(ck['documentos'])}")
        for d in ck["documentos"]:
            st = m.get(d["chave"])
            marca = "x" if st == "ok" else ("-" if st == "nao_se_aplica" else " ")
            print(f"  [{marca}] {d['item']}")


def cmd_receber(a, cfg, con):
    c = _col(a.id)
    item = next((d for d in _ck(c)["documentos"] if d["chave"] == a.item), None)
    if not item:
        raise SystemExit(f"item {a.item} nao existe no checklist de {c['vinculo']}")
    arq = Path(a.arquivo)
    nome = nome_arquivo(a.item.upper(), c.get("nome", ""), arq.suffix, quando=hoje())
    caminho = ["RH", pasta_do_colaborador(c), item["pasta"]]
    print(f"  {arq.name} -> {'/'.join(caminho)}/{nome}")
    svc, raiz = _svc_raiz(cfg)
    if svc:
        pid = drive.garantir_caminho(svc, raiz, caminho, executar=a.go)
        print("  Drive:", drive.enviar_arquivo(svc, arq, pid, nome, executar=a.go))
    if a.go:
        con.execute("INSERT INTO rh_eventos VALUES (?,?,?,?)", (c["id"], f"item:{a.item}", "ok", agora_iso()))
        con.commit()


def cmd_marcar(a, cfg, con):
    c = _col(a.id)
    if a.item not in {d["chave"] for d in _ck(c)["documentos"]}:
        raise SystemExit(f"item {a.item} nao existe no checklist de {c['vinculo']}")
    valor = "nao_se_aplica" if a.nao_se_aplica else "ok"
    print(f"  {c['nome']}: {a.item} = {valor}{'' if a.go else ' (dry-run, nao gravado)'}")
    if a.go:
        con.execute("INSERT INTO rh_eventos VALUES (?,?,?,?)", (c["id"], f"item:{a.item}", valor, agora_iso()))
        con.commit()


def _modelo_do(c: dict, cfg: dict, explicito: str | None) -> Path:
    if explicito:
        return Path(explicito)
    nome = ((cfg.get("rh") or {}).get("modelos_por_vinculo") or {}).get(c["vinculo"]) or _ck(c).get("modelo")
    if not nome:
        raise SystemExit(f"sem modelo de contrato para o vinculo {c['vinculo']} — informe --modelo")
    p = MODELOS_DIR / nome
    if not p.exists():
        raise SystemExit(f"modelo {p} nao encontrado (a frente de modelos ainda nao entregou?)")
    return p


def _dados_contrato(c: dict, cfg: dict, extra: str | None) -> dict:
    dados = dict(cfg.get("modelos_comuns") or {})
    dados.update(c.get("dados_contrato") or {})
    if extra:
        dados.update(json.loads(Path(extra).read_text("utf-8")))
    dados.setdefault("data_assinatura", data_br(hoje().isoformat()))
    return dados


def _saida_contrato(c: dict) -> Path:
    return garantir_dir(SAIDA_DIR / "rh" / pasta_do_colaborador(c))


def cmd_contrato(a, cfg, con):
    c = _col(a.id)
    modelo = _modelo_do(c, cfg, a.modelo)
    texto, faltando = modelos.render(modelo, _dados_contrato(c, cfg, a.dados))
    nome = nome_arquivo("CONTRATO", f"{modelo.stem} {c.get('nome', '')}", "", quando=hoje())
    pasta = _saida_contrato(c)
    md = pasta / f"{nome}.md"
    md.write_text(texto, encoding="utf-8")
    docx = modelos.markdown_para_docx(texto, pasta / f"{nome}.docx")
    print(f"  Gerado: {md}\n  Gerado: {docx}")
    if faltando:
        print(f"  FALTAM {len(faltando)} campo(s) (preencha em colaboradores.json -> dados_contrato ou "
              f"escritorio.json -> modelos_comuns):")
        for f in faltando:
            print(f"    - {{{{{f}}}}}")
    achados = modelos.fiscal(texto)
    print(f"  Fiscal: {'APROVADO para assinatura' if not achados else 'BARRADO (' + str(len(achados)) + ' achado(s))'}")
    svc, raiz = _svc_raiz(cfg)
    if svc and a.go:
        pid = drive.garantir_caminho(svc, raiz, ["RH", pasta_do_colaborador(c), "02_CONTRATO_E_ADITIVOS"], executar=True)
        print("  Drive:", drive.enviar_arquivo(svc, docx, pid, executar=True))


def cmd_assinar(a, cfg, con):
    c = _col(a.id)
    pasta = _saida_contrato(c)
    gerados = sorted(pasta.glob("*_CONTRATO_*.md"))
    if not gerados:
        raise SystemExit("gere o contrato antes: colaborador.py contrato --id ...")
    md = gerados[-1]
    achados = modelos.fiscal(md.read_text("utf-8"))
    if achados:
        raise SystemExit("FISCAL BARROU — nao vai para assinatura:\n  " + "\n  ".join(achados[:15]))
    docx = md.with_suffix(".docx")
    pdf = b""
    svc, raiz = _svc_raiz(cfg)
    if svc and a.go:
        tmp = drive.garantir_caminho(svc, raiz, ["RH", pasta_do_colaborador(c), "02_CONTRATO_E_ADITIVOS"], executar=True)
        pdf = drive.docx_para_pdf(svc, docx, tmp)
    elif a.go:
        raise SystemExit("--go precisa do Drive para converter o contrato em PDF")
    rh = cfg.get("rh") or {}
    signatarios = [{"nome": c.get("nome"), "papel": c.get("vinculo"), "email": c.get("email"),
                    "telefone": c.get("whatsapp")}]
    signatarios += [dict(s) for s in rh.get("signatarios_escritorio") or []]
    if c["vinculo"] == "estagiario":
        ies = (c.get("dados_contrato") or {})
        signatarios.append({"nome": ies.get("ies_representante") or "[representante da instituicao]",
                            "papel": "instituicao de ensino", "email": ies.get("ies_email") or ""})
    prov = assinatura.provedor((rh.get("assinatura") or {}).get("provedor"))
    r = prov.enviar(pdf, md.stem, signatarios, executar=a.go)
    print("  Assinatura:", r)
    if a.go:
        con.execute("INSERT INTO rh_eventos VALUES (?,?,?,?)", (c["id"], "assinatura_enviada", json.dumps(r), agora_iso()))
        con.commit()


def cmd_comprovante(a, cfg, con):
    c = _col(a.id)
    arq = Path(a.arquivo)
    nome = f"{a.mes}_comprovante{arq.suffix.lower()}"
    caminho = ["RH", pasta_do_colaborador(c), "03_PAGAMENTOS"]
    print(f"  {arq.name} -> {'/'.join(caminho)}/{nome}")
    svc, raiz = _svc_raiz(cfg)
    if svc:
        pid = drive.garantir_caminho(svc, raiz, caminho, executar=a.go)
        print("  Drive:", drive.enviar_arquivo(svc, arq, pid, nome, executar=a.go))


def main():
    utf8_stdout()
    ap = argparse.ArgumentParser(description="Agente de RH (POP-ADM-01)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = add_modo(sub.add_parser("checklist"))
    s.add_argument("--vinculo", required=True, choices=[k for k in CHECK if not k.startswith("_")])
    for nome in ("novo", "assinar"):
        add_modo(sub.add_parser(nome)).add_argument("--id", required=True)
    s = add_modo(sub.add_parser("status"))
    s.add_argument("--id")
    s.add_argument("--todos", action="store_true")
    s = add_modo(sub.add_parser("receber"))
    s.add_argument("--id", required=True)
    s.add_argument("--item", required=True)
    s.add_argument("--arquivo", required=True)
    s = add_modo(sub.add_parser("marcar"))
    s.add_argument("--id", required=True)
    s.add_argument("--item", required=True)
    s.add_argument("--nao-se-aplica", action="store_true")
    s = add_modo(sub.add_parser("contrato"))
    s.add_argument("--id", required=True)
    s.add_argument("--modelo")
    s.add_argument("--dados", help="JSON com campos extras/override")
    s = add_modo(sub.add_parser("comprovante"))
    s.add_argument("--id", required=True)
    s.add_argument("--mes", required=True)
    s.add_argument("--arquivo", required=True)
    a = ap.parse_args()
    banner(a.go, f"RH: {a.cmd}")
    cfg = escritorio()
    bloquear_exemplo(cfg, "escritorio", a.go)
    if a.cmd != "checklist":
        bloquear_exemplo(colaboradores(), "colaboradores", a.go)
    con = db.conectar()
    globals()[f"cmd_{a.cmd}"](a, cfg, con)


if __name__ == "__main__":
    main()
