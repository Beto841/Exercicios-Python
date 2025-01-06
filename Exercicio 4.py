jogos =[{'visitado': ('Belenenses' , 1), 'visitante': ('Maritimo', 2)},
        {'visitado': ('Nacional' , 5), 'visitante': ('Oliveirense', 0)},
        {'visitado': ('Porto' , 2), 'visitante': ('Torreeense', 2)}]

def conta_empates(jogos):
    empates = 0
    for jogo in jogos:
        if jogo['visitado'][1] == jogo['visitante'][1]: 
            empates += 1
    return empates

print(conta_empates(jogos))