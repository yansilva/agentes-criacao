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

## Montar a equipe

Depois de copiar os agentes para um projeto, abra uma sessão para cada especialista antes de começar o trabalho. Quem faz isso é a sessão principal, a mesma que copiou os agentes:

1. Liste os arquivos de `.claude/agents/`. Cada um é um especialista, menos `coordenador` e `orquestrador`, que são líderes.
2. Abra uma sessão por especialista, com o título `<especialista> — <projeto>` e o modelo do campo `model` do arquivo. O prompt manda a sessão ler o próprio arquivo de agente, responder "pronto" e aguardar.
3. Crie `.equipe/quadro.md` e a pasta `.equipe/memoria/`.
4. Registre nome, id e data de cada sessão em `.equipe/sessoes.md`.

As sessões devem abrir no mesmo checkout do projeto, sem worktree própria, para todas enxergarem a mesma pasta `.equipe/`.

A partir daí o líder só localiza a sessão do especialista e envia a tarefa. Para abrir só parte do time, diga quais especialistas quer.

## Nota

Cada especialista trabalha em uma sessão própria e permanente: uma por especialista em cada projeto. O líder (coordenador ou orquestrador) envia as tarefas seguintes e as correções para essa mesma sessão, em vez de abrir outra.

A equipe guarda o que aprende na pasta `.equipe/` do projeto em que trabalha:

- `.equipe/sessoes.md`: qual sessão pertence a cada especialista.
- `.equipe/quadro.md`: decisões e avisos que os especialistas deixam uns para os outros.
- `.equipe/memoria/<nome>.md`: lições de cada especialista no projeto.

Vale versionar essa pasta junto com o projeto, para a memória não se perder.

Os especialistas podem fazer perguntas diretas uns aos outros, mas não podem passar tarefas: trabalho novo só o líder distribui. Cada um anota no quadro o que está fazendo no início da rodada.
