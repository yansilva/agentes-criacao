# Agentes de Criação (apps e sites) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Criar um repositório público com um agente orquestrador (Opus) e dois agentes especialistas (apps e sites), clonável em outros dispositivos.

**Architecture:** Repositório com definições de agentes Claude Code em `.claude/agents/*.md`. O orquestrador classifica o pedido e delega ao especialista. Não há código de produto.

**Tech Stack:** Markdown com frontmatter YAML, Git, GitHub CLI (`gh`), Python 3 para validação.

**Spec:** `docs/superpowers/specs/2026-10-17-agentes-criacao-design.md`

## Global Constraints

- Orquestrador: `model: opus`.
- Especialistas (app-builder, site-builder): `model: sonnet`.
- Repositório GitHub: público, nome `agentes-criacao`.
- Idioma dos arquivos de agente: português.
- Nenhum token, senha ou dado pessoal no repositório.

## Review Focus

- Frontmatter com campo ausente ou YAML inválido faz o agente não carregar → validação do frontmatter na Task 4.
- Orquestrador referencia um agente que não existe → checagem de nomes na Task 4.
- Arquivo de agente sem `description` não é escolhido automaticamente → validação na Task 4.
- Modelo errado (orquestrador em sonnet) → checagem de `model` na Task 4.
- Push de arquivo sensível (`.env`, chaves) → `.gitignore` na Task 1 e checagem na Task 5.

---

### Task 1: Scaffold do repositório

**Files:**
- Create: `README.md`
- Create: `.gitignore`
- Create: `.claude/agents/.gitkeep`

**Interfaces:**
- Consumes: nada.
- Produces: pasta `.claude/agents/` onde as Tasks 2–3 criam os agentes.

- [ ] **Step 1: Criar `.gitignore`**

Conteúdo: `.env`, `*.pem`, `*.key`, `node_modules/`, `.DS_Store`.

- [ ] **Step 2: Criar `README.md`**

Conteúdo: o que é o repositório, lista dos três agentes, como clonar em `~/.claude/agents/` ou `.claude/agents/` do projeto, e a nota de que cada agente novo é criado em nova sessão.

- [ ] **Step 3: Criar `.claude/agents/.gitkeep`**

Arquivo vazio para manter a pasta no Git.

- [ ] **Step 4: Inicializar Git**

Run: `cd /home/yan/Yan/agentes-criacao && git init -b main && git status --short`
Expected: lista `.gitignore`, `README.md`, `.claude/`, `docs/` como não rastreados.

- [ ] **Step 5: Commit**

```bash
git add .gitignore README.md .claude docs
git commit -m "chore: scaffold repositório e spec de design"
```

---

### Task 2: Agente orquestrador

**Files:**
- Create: `.claude/agents/orquestrador.md`

**Interfaces:**
- Consumes: nomes `app-builder` e `site-builder` (Task 3).
- Produces: agente `orquestrador` com `model: opus`.

- [ ] **Step 1: Escrever o frontmatter**

```yaml
---
name: orquestrador
description: Use para pedidos de criar um app (mobile ou web) ou um site. Classifica o pedido, aplica brainstorming e delega ao especialista certo.
model: opus
---
```

- [ ] **Step 2: Escrever o corpo**

Seções obrigatórias, em português:
1. Papel: orquestrar a criação de apps e sites.
2. Antes de delegar: invocar a skill `superpowers:brainstorming` para fixar objetivo, público e critério de sucesso. Uma pergunta por vez.
3. Escolha do especialista: `app-builder` para apps mobile/web, `site-builder` para sites.
4. Criação de agente novo: abrir nova sessão com briefing (nome, função, arquivos, critério de pronto).
5. Verificação: conferir o resultado antes de dar como concluído.

- [ ] **Step 3: Verificar o arquivo**

Run: `grep -c "model: opus" .claude/agents/orquestrador.md`
Expected: `1`

---

### Task 3: Agentes especialistas

**Files:**
- Create: `.claude/agents/app-builder.md`
- Create: `.claude/agents/site-builder.md`

**Interfaces:**
- Consumes: nada.
- Produces: `app-builder` e `site-builder`, ambos com `model: sonnet`.

- [ ] **Step 1: Escrever `app-builder.md`**

Frontmatter: `name: app-builder`, `description` (criar app mobile ou web do zero ou evoluir um existente), `model: sonnet`. Corpo: fluxo de brainstorming quando o escopo não está claro, plano com superpowers:writing-plans para projetos novos, testes antes de dar como pronto.

- [ ] **Step 2: Escrever `site-builder.md`**

Frontmatter: `name: site-builder`, `description` (criar site ou landing page), `model: sonnet`. Corpo: mesmo fluxo, com foco em estrutura de páginas, responsividade e SEO básico.

- [ ] **Step 3: Verificar os arquivos**

Run: `grep -l "model: sonnet" .claude/agents/app-builder.md .claude/agents/site-builder.md | wc -l`
Expected: `2`

- [ ] **Step 4: Commit**

```bash
git add .claude/agents
git commit -m "feat: adiciona agentes orquestrador, app-builder e site-builder"
```

---

### Task 4: Validar frontmatter e referências

**Files:**
- Create: `scripts/validar_agentes.py`

**Interfaces:**
- Consumes: os três arquivos de `.claude/agents/`.
- Produces: script que sai com código 0 se tudo estiver válido.

- [ ] **Step 1: Escrever o script**

Para cada `.claude/agents/*.md`: extrair o bloco entre `---`, parsear `name`, `description`, `model`. Exigir os três campos. Confirmar que `orquestrador` tem `model: opus` e os outros `sonnet`. Confirmar que `orquestrador.md` cita `app-builder` e `site-builder`, e que esses arquivos existem.

- [ ] **Step 2: Rodar o script**

Run: `python3 -I scripts/validar_agentes.py`
Expected: `OK: 3 agentes válidos`

- [ ] **Step 3: Commit**

```bash
git add scripts/validar_agentes.py
git commit -m "test: valida frontmatter e referências dos agentes"
```

---

### Task 5: Checagem de segredos e publicação

**Files:** nenhum novo.

- [ ] **Step 1: Checar segredos**

Run: `git grep -nIE "(api[_-]?key|token|password|senha|BEGIN [A-Z ]*PRIVATE KEY)" -- . ':!docs'`
Expected: nenhuma linha de credencial real.

- [ ] **Step 2: Criar repositório público e subir**

Run: `cd /home/yan/Yan/agentes-criacao && gh repo create agentes-criacao --public --source=. --remote=origin --push`
Expected: URL do repositório impresso, branch `main` enviada.

- [ ] **Step 3: Confirmar clone**

Run: `git ls-remote origin main`
Expected: um hash para `refs/heads/main`.

---

## Revisão 2 do plano — time ampliado

Spec: `docs/superpowers/specs/2026-10-17-agentes-criacao-design.md` (revisão 2, time aprovado pelo usuário).

### Task 6: Lote de especialistas (mesmo formato)

**Files (Create, em `.claude/agents/`):**
- `arquiteto.md` — `name: arquiteto`, `model: opus`. Monta o roteiro técnico do projeto e recomenda quais especialistas acionar e em que ordem.
- `designer.md` — `name: designer`, `model: sonnet`. Interface, fluxo de telas, identidade visual, acessibilidade básica.
- `seguranca.md` — `name: seguranca`, `model: sonnet`. Autenticação, segredos, dependências, entradas do usuário.
- `qa.md` — `name: qa`, `model: sonnet`. Testes, critérios de aceite, regressão.
- `devops.md` — `name: devops`, `model: sonnet`. Build, hospedagem, pipeline, variáveis de ambiente.
- `dados.md` — `name: dados`, `model: sonnet`. Modelagem de banco, APIs, migrações.
- `conteudo.md` — `name: conteudo`, `model: sonnet`. Textos, títulos, chamadas, tom de voz.
- `acessibilidade.md` — `name: acessibilidade`, `model: sonnet`. WCAG básico, contraste, teclado, leitor de tela.
- `seo-performance.md` — `name: seo-performance`, `model: sonnet`. Metadados, velocidade, Core Web Vitals.
- `documentacao.md` — `name: documentacao`, `model: sonnet`. README, guia de uso, registro de decisões.

Each file: frontmatter com `name`, `description` (uma frase de quando usar), `model`; corpo em português, curto, com papel e critério de pronto.

**Verify:** `python3 scripts/validar_agentes.py` (após Task 7 atualizar o script).

### Task 7: Orquestrador e validação ampliados

**Files:**
- Modify: `.claude/agents/orquestrador.md` — lista de especialistas, fluxo do arquiteto, regra de maioria (decisão por maioria entre especialistas consultados, empate com o orquestrador, registrado).
- Modify: `scripts/validar_agentes.py` — modelos esperados: `orquestrador` e `arquiteto` opus; os demais sonnet. Orquestrador deve citar todos os especialistas.

**Verify:** `python3 -I scripts/validar_agentes.py` → `OK: 13 agentes válidos` (orquestrador, arquiteto, designer, seguranca, qa, devops, dados, conteudo, acessibilidade, seo-performance, documentacao, app-builder, site-builder).

### Task 8: Publicação

Mesma Task 5 do plano original, com a nova contagem de agentes. Bloqueada até `gh auth login` válido.

---

## Revisão 4 do plano — setores e programação

Spec: revisão 4 do design. Aprovados: `produto`, `marketing`, `juridico-lgpd`, `suporte`, `frontend`, `backend`, `mobile`, `revisao-codigo` (todos sonnet). Os recomendados (`financeiro`, `vendas`, `pesquisa-usuario`, `analytics`) ficam fora.

### Task 9: Lote de 8 especialistas (mesmo formato da Task 6)

Create in `.claude/agents/`: `produto.md`, `marketing.md`, `juridico-lgpd.md`, `suporte.md`, `frontend.md`, `backend.md`, `mobile.md`, `revisao-codigo.md`. Each: frontmatter `name`, `description`, `model: sonnet`; short Portuguese body with papel, como trabalha, entrega, critério de pronto.

### Task 10: Orquestrador e validador com 21 agentes

- Modify `.claude/agents/orquestrador.md`: list all new specialists, one line each.
- Modify `scripts/validar_agentes.py`: all new names sonnet; orquestrador must mention all of them.
- Verify: `python3 -I scripts/validar_agentes.py` → `OK: 21 agentes válidos`, exit 0.

### Task 11: Publicação

Bloqueada até `gh auth login` válido. Mesma Task 5 do plano original.
