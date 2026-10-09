import argparse
import sys

from pokedex.api import PokemonError, get_pokemon
from pokedex.formatar import formatar_comparacao, formatar_ficha

try:  # usa o repositório de certificados do SO (útil atrás de proxy/antivírus com HTTPS)
    import truststore

    truststore.inject_into_ssl()
except ImportError:
    pass


def montar_parser():
    parser = argparse.ArgumentParser(prog="pokedex", description="PokéDex CLI (PokéAPI)")
    sub = parser.add_subparsers(dest="comando", required=True)
    sub.add_parser("buscar", help="mostra a ficha de um Pokémon").add_argument("nome")
    comp = sub.add_parser("comparar", help="compara dois Pokémon")
    comp.add_argument("nome_a")
    comp.add_argument("nome_b")
    return parser


def main(argv=None):
    args = montar_parser().parse_args(argv)
    try:
        if args.comando == "buscar":
            print(formatar_ficha(get_pokemon(args.nome)))
        else:
            print(formatar_comparacao(get_pokemon(args.nome_a), get_pokemon(args.nome_b)))
    except PokemonError as erro:
        print(f"Erro: {erro}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
