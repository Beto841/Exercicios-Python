jogos = (['Fiji', 23, 'Portugal', 24],
         ['Tonga', 45, 'Romenia', 24],
         ['Japao', 27, 'Argentina', 39])

def abaixoQ(jogos, pontos):
    for jogo in jogos:
        if jogo[1] < pontos or jogo[3] < pontos:
            return True
        else:
            return False

print (abaixoQ(jogos, 20))