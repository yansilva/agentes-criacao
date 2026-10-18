# Aprendizados: frontend

Contexto: Site do portfólio (construído nesta etapa pelo controlador, sem sessão própria).

## O que funcionou

- Erro real: o caminho de fontes no CSS era relativo à página, não ao arquivo CSS. As fontes falharam com 404 até corrigir.
- Seletor `.site-nav ul` não casava com o elemento: a classe estava no próprio `ul`. O revisor de código pegou isso depois.

## Regras para a próxima vez

- url() dentro de CSS é relativo ao arquivo CSS, nunca à página.
- Confira seletores contra o HTML real antes de dar como pronto.
- Confira fontes no navegador: `document.fonts` deve mostrar `loaded`.

Lições gerais: [LICOES.md](LICOES.md).
