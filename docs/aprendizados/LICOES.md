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
