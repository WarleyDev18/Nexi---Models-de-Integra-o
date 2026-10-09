from unittest.mock import MagicMock, patch

import pytest
import requests

from pokedex.api import PokemonError, get_pokemon


def _resposta(status, json_data=None):
    r = MagicMock()
    r.status_code = status
    r.json.return_value = json_data or {}
    return r


def test_get_pokemon_sucesso():
    with patch("pokedex.api.requests.get", return_value=_resposta(200, {"name": "pikachu"})) as g:
        dados = get_pokemon("  Pikachu ")
    assert dados["name"] == "pikachu"
    assert g.call_args.args[0].endswith("/pokemon/pikachu")
    assert g.call_args.kwargs["timeout"] == 10


def test_get_pokemon_nao_encontrado():
    with patch("pokedex.api.requests.get", return_value=_resposta(404)):
        with pytest.raises(PokemonError, match="não encontrado"):
            get_pokemon("xyzzy")


def test_get_pokemon_erro_http():
    with patch("pokedex.api.requests.get", return_value=_resposta(500)):
        with pytest.raises(PokemonError, match="500"):
            get_pokemon("pikachu")


def test_get_pokemon_timeout():
    with patch("pokedex.api.requests.get", side_effect=requests.Timeout):
        with pytest.raises(PokemonError, match="demorou"):
            get_pokemon("pikachu")


def test_get_pokemon_erro_de_rede():
    with patch("pokedex.api.requests.get", side_effect=requests.ConnectionError):
        with pytest.raises(PokemonError, match="rede"):
            get_pokemon("pikachu")


def test_get_pokemon_nome_vazio():
    with pytest.raises(PokemonError):
        get_pokemon("   ")
