# CLAUDE.md — PokéDex CLI

Mini-projeto de curso: CLI em Python que consome a PokéAPI (gratuita, sem chave).

## Comandos
- Instalar: `pip install -r requirements.txt`
- Testes: `python -m pytest` (sem rede; `requests` é mockado)
- Buscar: `python -m pokedex.cli buscar pikachu`
- Comparar: `python -m pokedex.cli comparar pikachu charizard`

## Estrutura
- `pokedex/api.py` — única camada que fala com a rede (`get_pokemon`)
- `pokedex/formatar.py` — funções puras que viram texto (sem I/O)
- `pokedex/cli.py` — argparse e códigos de saída
- `tests/` — pytest

## Regras
- API: `https://pokeapi.co/api/v2/pokemon/{nome}`, nome em minúsculas, timeout de 10s.
- Erros de rede/404 viram `PokemonError`; a CLI mostra mensagem amigável e sai com código 1.
- Testes nunca acessam a internet.
- Dependências de runtime: `requests` e `truststore` (esta usa os certificados do SO; resolveu `CERTIFICATE_VERIFY_FAILED` em rede com proxy/antivírus). Nunca usar `verify=False`.
- Código e mensagens em português; nomes de funções em português sem acento.
- Este repo é público: nada de dados, chaves ou referências internas de empresa.

## Fluxo de trabalho
Plan mode primeiro, `plan.md` é a fonte da verdade das etapas; marque os checkboxes ao concluir cada uma. Só fazer commit/push quando o usuário pedir.
