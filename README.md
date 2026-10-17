# agentes-criacao

Repositório com definições de agentes do Claude Code para criar apps e sites.

## Agentes

- **orquestrador**: recebe o pedido, decide o que construir e delega aos demais agentes.
- **app-builder**: constrói aplicativos.
- **site-builder**: constrói sites.

## Como usar

Copie a pasta de agentes para o local desejado:

```bash
# Global (todos os projetos)
cp -r .claude/agents/* ~/.claude/agents/

# Apenas em um projeto
cp -r .claude/agents/* /caminho/do/projeto/.claude/agents/
```

## Nota

Cada agente novo é criado em uma sessão própria.
