t1 = (6, 0, 2, 8, 9)
t2 = (1, 4, 7, 6, 3)

def intercala(t1, t2):
    t3 = []  # criar uma lista vazia
    i = 0
    while i < len(t1):
        t3.append(t1[i])  # adicionar elemento de t1
        t3.append(t2[len(t2) - i - 1])  # adicionar elemento de t2 (de trás para frente)
        i += 1
    return tuple(t3)  # converter a lista para tuplo antes de retornar

print(intercala(t1, t2))

#append é exclusivo de listas, não de tuplos porque tuplos são imutáveis é por isso que temos de criar uma lista vazia e adicionar os valores a essa lista e só depois é que a convertemos para tuplo.