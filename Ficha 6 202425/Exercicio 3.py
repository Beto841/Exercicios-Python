v = [('caderno', 10, 150, 0.5),  ('lápis', 75, 220, 0.15), ('tesoura', 234, 50, 2.4)]

def filtra_produtos(v, preço):
    #ver se a lista é vazia retornar um tuplo vazio
    if v == []:
        return ()
    #ver se a preço é menor que zero retorna um tuplo vazio
    if preço < 0:
        return ()
    #criar uma tuplo vazio
    tuplo = ()
    #precorrer a lista v e verificar a posição 3 de cada tuplo
    for i in v:
        if i[3] >= preço:
            #mas se a quantidade for 0 ou menor que 0, não adiciona ao tuplo
            if i[2] <= 0:
                continue #passa para a próxima iteração, sem adicionar ao tuplo
            #se verificar que a posição 3 é maior ou igual a preço, cria um dicionário do tipo {'prod': i[0], 'num': i[3]} e depois adiciona ao tuplo
            tuplo += ({'prod': i[0], 'num': i[1]},)
    
    return tuplo

print(filtra_produtos(v, 0.5))