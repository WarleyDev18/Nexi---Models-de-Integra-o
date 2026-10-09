# plan.md — PokéDex CLI

Objetivo: CLI em Python que busca e compara Pokémon usando a PokéAPI.
Decisões: PokéAPI (sem chave) · Python 3.13 · `requests` + `pytest` · argparse.

## Etapas
- [x] 1. Scaffold: pasta, `git init`, `.gitignore`, `requirements.txt`
- [x] 2. `CLAUDE.md` e `plan.md`
- [x] 3. `api.py`: `get_pokemon(nome)` com timeout 10s, trata 404/timeout/rede via `PokemonError`; testes mockados primeiro
- [x] 4. `formatar.py`: ficha (nome, id, tipos, altura, peso, stats) e comparação lado a lado com total de stats
- [x] 5. `cli.py`: subcomandos `buscar` e `comparar`, erro amigável, exit code 1 em falha
- [x] 6. Revisão: pytest, execução real (pikachu, charizard, nome inválido), revisão do diff
- [x] 7. `README.md` e `RESPOSTAS.md` (modelos, clear/compact, riscos sem plan mode)
- [x] 8. Commit e push para o GitHub (só com confirmação do usuário)

## Modelos por etapa
- Planejamento: Opus (decisões caras de errar)
- Execução: Sonnet (código bem especificado)
- Tarefas triviais/README: Haiku
- Revisão: Opus (ou Sonnet para revisão leve)

## Verificação final
- `python -m pytest` verde
- `buscar pikachu`, `comparar pikachu charizard` funcionam; `buscar xyzzy` dá erro amigável com exit code 1
