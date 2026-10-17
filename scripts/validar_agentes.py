#!/usr/bin/env python3
"""Valida frontmatter e referências dos agentes em .claude/agents/."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AGENTS = ROOT / ".claude" / "agents"
MODELOS = {"orquestrador": "opus", "app-builder": "sonnet", "site-builder": "sonnet"}


def frontmatter(texto):
    linhas = texto.splitlines()
    if not linhas or linhas[0].strip() != "---":
        return None
    campos = {}
    for linha in linhas[1:]:
        if linha.strip() == "---":
            return campos
        if ":" in linha and not linha[0].isspace():
            k, v = linha.split(":", 1)
            campos[k.strip()] = v.strip()
    return None


def main():
    erros = []
    arquivos = sorted(AGENTS.glob("*.md"))
    for f in arquivos:
        texto = f.read_text(encoding="utf-8")
        fm = frontmatter(texto)
        if fm is None:
            erros.append(f"{f.name}: frontmatter ausente ou não fechado")
            continue
        for campo in ("name", "description", "model"):
            if not fm.get(campo):
                erros.append(f"{f.name}: campo '{campo}' ausente ou vazio")
        esperado = MODELOS.get(f.stem)
        if esperado and fm.get("model") and fm["model"] != esperado:
            erros.append(f"{f.name}: model '{fm['model']}' != '{esperado}'")
    for nome in MODELOS:
        if not (AGENTS / f"{nome}.md").exists():
            erros.append(f"{nome}.md não existe")
    orq = AGENTS / "orquestrador.md"
    if orq.exists():
        t = orq.read_text(encoding="utf-8")
        for nome in ("app-builder", "site-builder"):
            if nome not in t:
                erros.append(f"orquestrador.md não menciona {nome}")
    if erros:
        for e in erros:
            print(f"ERRO: {e}")
        return 1
    print(f"OK: {len(arquivos)} agentes válidos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
