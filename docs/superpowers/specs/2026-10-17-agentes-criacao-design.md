# Agentes de Criação (apps e sites) — Design

Data: 2026-10-17
Status: aguardando revisão do usuário

## Objetivo

Um repositório público no GitHub com agentes Claude Code para criar **apps (mobile/web)** e **sites**. Um **orquestrador** (Opus) recebe o pedido, decide o tipo de projeto e delega ao agente especialista. Cada agente novo é criado em uma sessão própria. O repositório deve ser clonável em outros dispositivos.

## Entendimento (a confirmar)

- Dito pelo usuário: agentes para apps e sites; orquestrador com Opus; skill superpowers; cada agente novo em nova sessão; publicar no GitHub para usar em outros dispositivos; repositório **público**.
- Premissa nossa: os agentes são arquivos de definição Claude Code (`.claude/agents/*.md`), não serviços externos.

## Abordagem escolhida (A)

Repositório único com:

- `.claude/agents/orquestrador.md` — modelo `opus`. Classifica o pedido (app ou site), usa a skill superpowers (brainstorming antes de criar), e delega ao especialista certo. Ao criar um agente novo, abre uma nova sessão com um briefing.
- `.claude/agents/app-builder.md` — modelo `sonnet` (ver decisões abaixo). Cria apps mobile/web.
- `.claude/agents/site-builder.md` — cria sites.
- `README.md` — como clonar, usar e instalar os agentes em outro dispositivo.
- `docs/superpowers/specs/` — specs de design (este arquivo).
- `docs/superpowers/plans/` — planos de implementação (depois da aprovação da spec).

### Formato de cada agente

Frontmatter com `name`, `description` (quando usar), `model`, e `tools` quando necessário. Corpo em português com: papel, quando delegar, fluxo de trabalho, critérios de pronto.

### Fluxo do orquestrador

1. Recebe o pedido do usuário.
2. Aplica brainstorming para fixar objetivo, público e critério de sucesso.
3. Escolhe o especialista (app ou site). Se o pedido for ambíguo, pergunta uma coisa por vez.
4. Para criar um agente novo: abre nova sessão com briefing completo (nome, função, arquivos, critério de pronto).
5. Verifica o resultado antes de dar como concluído.

## Decisões

- Repo público: confirmado pelo usuário. Antes de publicar, checar que nada sensível (tokens, dados pessoais) está no repositório.
- Modelo dos especialistas: `sonnet` por custo, o orquestrador usa `opus`. Pode ser trocado.
- Nada de código de produto neste repo; só definições de agentes e docs.

## Verificação

- Frontmatter válido em cada `.md` de agente (YAML parseável, campos obrigatórios presentes).
- Cada agente referenciado pelo orquestrador existe.
- Um teste de uso: o orquestrador delega um pedido de site e um de app para o especialista certo.

## Publicação

1. `git init` na pasta `agentes-criacao`.
2. Commit com as definições e docs.
3. Criar repositório público no GitHub e dar push. Só depois da aprovação desta spec e do plano.

## Fora de escopo

- Automatizar a criação de projetos de app/site em si (isso é trabalho dos agentes depois de criados).
- Outros tipos de agente além de app e site, nesta primeira versão.

## Questões em aberto

- Nome do repositório no GitHub (sugestão: `agentes-criacao`).
- Confirmar modelo `sonnet` para os especialistas.
