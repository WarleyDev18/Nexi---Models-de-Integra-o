from pokedex.formatar import formatar_comparacao, formatar_ficha, total_stats

PIKACHU = {
    "name": "pikachu", "id": 25, "height": 4, "weight": 60,
    "types": [{"type": {"name": "electric"}}],
    "stats": [
        {"base_stat": 35, "stat": {"name": "hp"}},
        {"base_stat": 55, "stat": {"name": "attack"}},
    ],
}
CHARIZARD = {
    "name": "charizard", "id": 6, "height": 17, "weight": 905,
    "types": [{"type": {"name": "fire"}}, {"type": {"name": "flying"}}],
    "stats": [
        {"base_stat": 78, "stat": {"name": "hp"}},
        {"base_stat": 84, "stat": {"name": "attack"}},
    ],
}


def test_total_stats():
    assert total_stats(PIKACHU) == 90


def test_ficha_converte_unidades():
    texto = formatar_ficha(PIKACHU)
    assert "Pikachu (#25)" in texto
    assert "electric" in texto
    assert "0.4 m" in texto and "6.0 kg" in texto
    assert "hp" in texto and "35" in texto


def test_ficha_varios_tipos():
    assert "fire, flying" in formatar_ficha(CHARIZARD)


def test_comparacao_indica_vencedor():
    texto = formatar_comparacao(PIKACHU, CHARIZARD)
    assert "Total" in texto
    assert "Charizard vence" in texto


def test_comparacao_empate():
    assert "Empate" in formatar_comparacao(PIKACHU, PIKACHU)
