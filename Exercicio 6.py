jogos = [{'equipa': 'Vizela', 'amarelos': 2, 'vermelhos': 1},
         {'equipa': 'Benfica', 'amarelos': 3, 'vermelhos': 0},
         {'equipa': 'Porto', 'amarelos': 1, 'vermelhos': 0},
         {'equipa': 'Sporting', 'amarelos': 0, 'vermelhos': 1}]

def equipas_com_vermelho(jogos):
    return tuple(jogo['equipa'] for jogo in jogos if jogo['vermelhos'] > 0)

print(equipas_com_vermelho(jogos)) 