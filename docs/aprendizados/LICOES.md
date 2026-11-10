# Lições gerais dos agentes

Regras que valem para todo o time. Cada agente tem seu próprio arquivo em `docs/aprendizados/`.

1. **Caminhos relativos:** `url()` dentro de CSS é relativo ao arquivo CSS, não à página.
2. **Confirme antes de reportar:** antes de listar uma pendência, confira no estado atual do repositório. Um item já resolvido não vira pendência.
3. **Cite o trecho:** referências só por linha envelhecem depois de qualquer edição. Cite o trecho de código.
4. **Mudança de direção:** atualize o documento com uma nota de revisão e a data. Não apague o histórico.
5. **Sessões de agentes:** só abrem por pedido direto do usuário. Eventos automáticos não abrem sessão; nesses casos, o controlador faz o trabalho e registra isso.
6. **Verificação visual:** não assuma que o layout está certo. Diga o que não foi verificado e peça a verificação.
7. **Seletores e fontes:** confira seletores contra o HTML real e fontes com `document.fonts` no navegador.
8. **Modelo por etapa:** projete com `opus`; execute com o modelo mais barato. Defina o modelo explicitamente em cada agente ou subagente.
9. **Uma sessão por especialista:** cada especialista tem uma única sessão por projeto. Tarefas novas e correções vão para ela com `SendMessage`. Não abra outra sessão para o mesmo especialista. As lições do projeto ficam em `.equipe/memoria/` e os avisos entre especialistas em `.equipe/quadro.md`.
10. **Conversa entre especialistas:** pergunta direta é permitida; tarefa só o líder passa. Quem recebe responde com o que já sabe, sem alterar arquivos e sem consultar um terceiro. No máximo duas trocas por assunto, e tudo vai para o quadro.
11. **Montagem da equipe:** ao instalar os agentes num projeto, abra de uma vez uma sessão por especialista, com o título `<especialista> — <projeto>`, e registre em `.equipe/sessoes.md`. Depois o líder só localiza a sessão.
12. **Quadro compartilhado:** só acrescente linhas ao `.equipe/quadro.md`, com `Edit`. Regravar o arquivo inteiro apaga o que outro especialista escreveu ao mesmo tempo. O líder cria o quadro na montagem.
13. **Pergunta direta é assíncrona:** a resposta do colega chega em outra rodada. Registre a pendência, termine o resto e relate o que ficou pendente.
