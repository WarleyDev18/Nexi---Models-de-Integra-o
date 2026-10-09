# PokéDex CLI

Mini-projeto de curso feito com o Claude Code: CLI em Python que consome a [PokéAPI](https://pokeapi.co) (gratuita, sem chave).

## Uso
```bash
pip install -r requirements.txt
python -m pokedex.cli buscar pikachu
python -m pokedex.cli comparar pikachu charizard
python -m pytest        # testes sem rede
```

Nome inexistente ou falha de rede mostram uma mensagem amigável e saem com código 1.

## Arquivos
- `CLAUDE.md` — instruções do projeto para o Claude Code
- `plan.md` — plano por etapas (gerado em plan mode)
- `RESPOSTAS.md` — documento com as justificativas pedidas no trabalho
