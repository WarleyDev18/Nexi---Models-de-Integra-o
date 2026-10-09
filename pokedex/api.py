import requests

BASE_URL = "https://pokeapi.co/api/v2"
TIMEOUT = 10


class PokemonError(Exception):
    """Erro ao consultar a PokéAPI (mensagem já amigável para o usuário)."""


def get_pokemon(nome):
    nome = nome.strip().lower()
    if not nome:
        raise PokemonError("Informe o nome de um Pokémon.")
    try:
        resp = requests.get(f"{BASE_URL}/pokemon/{nome}", timeout=TIMEOUT)
    except requests.Timeout:
        raise PokemonError("A PokéAPI demorou demais para responder.") from None
    except requests.RequestException:
        raise PokemonError("Falha de rede ao acessar a PokéAPI.") from None
    if resp.status_code == 404:
        raise PokemonError(f"Pokémon '{nome}' não encontrado.")
    if resp.status_code != 200:
        raise PokemonError(f"A PokéAPI respondeu com erro HTTP {resp.status_code}.")
    return resp.json()
