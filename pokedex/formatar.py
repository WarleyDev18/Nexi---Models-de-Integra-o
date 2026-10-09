def total_stats(p):
    return sum(s["base_stat"] for s in p["stats"])


def _tipos(p):
    return ", ".join(t["type"]["name"] for t in p["types"])


def formatar_ficha(p):
    linhas = [
        f"{p['name'].capitalize()} (#{p['id']})",
        f"Tipos: {_tipos(p)}",
        f"Altura: {p['height'] / 10:.1f} m   Peso: {p['weight'] / 10:.1f} kg",
        "Stats base:",
    ]
    linhas += [f"  {s['stat']['name']:<18}{s['base_stat']:>4}" for s in p["stats"]]
    linhas.append(f"  {'Total':<18}{total_stats(p):>4}")
    return "\n".join(linhas)


def formatar_comparacao(a, b):
    nome_a, nome_b = a["name"].capitalize(), b["name"].capitalize()
    larg = max(len(nome_a), len(nome_b), 5) + 2
    sb = {s["stat"]["name"]: s["base_stat"] for s in b["stats"]}
    linhas = [f"{'':<18}{nome_a:>{larg}}{nome_b:>{larg}}"]
    for s in a["stats"]:
        nome = s["stat"]["name"]
        linhas.append(f"{nome:<18}{s['base_stat']:>{larg}}{sb.get(nome, '-'):>{larg}}")
    ta, tb = total_stats(a), total_stats(b)
    linhas.append(f"{'Total':<18}{ta:>{larg}}{tb:>{larg}}")
    if ta == tb:
        linhas.append("Empate!")
    else:
        linhas.append(f"{nome_a if ta > tb else nome_b} vence pelo total de stats.")
    return "\n".join(linhas)
