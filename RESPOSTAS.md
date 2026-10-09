# RESPOSTAS — PokéDex CLI

## 1. Por que escolhi cada modelo em cada etapa

| Etapa | Modelo | Por quê |
|---|---|---|
| Planejamento (plan mode, `plan.md`, `CLAUDE.md`) | **Opus** | É onde as decisões caras são tomadas (API, stack, estrutura, escopo). Um erro aqui se propaga para todo o código; vale pagar por raciocínio mais profundo, e o volume de tokens é pequeno. |
| Execução (api, formatar, cli, testes) | **Sonnet** | O plano já define o que fazer, então a tarefa é implementar código bem especificado. Sonnet entrega qualidade suficiente com melhor custo e velocidade. |
| Tarefas triviais (README, renomear, docstrings, formatação) | **Haiku** | Baratas e mecânicas; um modelo maior seria desperdício. |
| Revisão (diff, bugs sutis, aderência ao plano) | **Opus** (Sonnet em revisões leves) | Revisar exige achar o que ficou de fora. Convém um modelo forte e, de preferência, uma sessão limpa, para não herdar o viés de quem escreveu. |

Regra geral: gastar o modelo mais forte onde errar custa mais (planejar e revisar) e o mais barato onde a tarefa já está clara (executar).

## 2. Quando usar /clear e /compact

- **/clear**: logo depois de aprovar o plano, antes de começar a executar. `plan.md` e `CLAUDE.md` guardam tudo que importa, então a conversa de planejamento só ocuparia contexto. Também ao trocar de assunto e antes da revisão final, para revisar com contexto limpo.
- **/compact**: no meio da execução (por exemplo depois da camada de API e da formatação, antes da CLI), quando a conversa já está longa mas eu ainda preciso das decisões tomadas (como o tratamento de erros e o problema de certificado SSL). Eu pediria algo como "preserve as decisões de API, os testes pendentes e o estado do plan.md".
- Antes de qualquer um dos dois, deixar o estado em arquivo (checkboxes do `plan.md`), porque o que está só na conversa se perde ou se resume.

Na prática deste projeto, o erro `CERTIFICATE_VERIFY_FAILED` apareceu na execução real. Esse tipo de detalhe é exatamente o que um `/compact` deveria preservar, e ficou registrado no `CLAUDE.md`.

## 3. O que poderia dar errado sem o plan mode

- O Claude executaria na primeira interpretação do pedido, sem eu alinhar API, stack e estrutura. Poderia escolher uma API com chave ou limite de uso, ou uma stack que eu não queria.
- Poderia criar os arquivos no lugar errado. Aqui o diretório de trabalho era o repositório privado de uma empresa, e o código do trabalho acabaria misturado ali.
- Poderia fazer commit e push em um repositório público sem eu ter decidido isso.
- Escopo inflado ou sem testes: sem um plano com critério de "pronto", não há como saber quando acabou nem como revisar o resultado.
- Retrabalho caro: corrigir depois que tudo foi gerado gasta mais tokens e tempo do que corrigir um plano de uma página.

O plan mode também mostrou valor concreto aqui: as perguntas feitas antes da execução (qual API, onde criar a pasta) evitaram os dois primeiros problemas acima.
