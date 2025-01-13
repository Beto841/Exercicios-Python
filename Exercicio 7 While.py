t1 = (6, 0, 2, 8, 9)
t2 = (1, 4, 7, 6, 3)

def intercala(t1, t2):
    t3 = () #cria um tuplo vazio que é onde vamos guardar os valores e que vamos retornar
    #percorre t1 de 0 até ao comprimento de t1 e t2 do comprimento de t2 até 0
    i = 0
    while i < len(t1):
        t3 += (t1[i], t2[len(t2)-i-1]) #adiciona ao tuplo t3 os valores do tuplo t1 e do tuplo t2. O len(t2)-i-1 é para percorrer o tuplo t2 de trás para a frente. len(t2) dá o comprimento do tuplo t2, i é o valor que está a ser percorrido no tuplo t1 e -1 é para começar a percorrer o tuplo t2 de trás para a frente, ou seja, se o comprimento do tuplo t2 for 5, o i for 0, então o valor que vai ser percorrido no tuplo t2 é o 4, que é o último valor do tuplo t2.
        i += 1
    return t3

print(intercala(t1, t2))
        