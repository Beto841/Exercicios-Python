dados = ([('Vizela', 'Benfica'), (2, 3)],
            [('Porto', 'Arouca'), (1, 2)],
            [('Sporting', 'Portimonense'), (0, 3)])

def num(dados, num_cartoes):
    jogos = 0
    for jogo in dados:
        if jogo[1][0] >= num_cartoes and jogo[1][1] >= num_cartoes:
            jogos += 1
    return jogos

print(num(dados, 1))