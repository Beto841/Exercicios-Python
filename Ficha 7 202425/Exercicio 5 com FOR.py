tuplo = (2,3,6,7,2,9,2)

def pares_tuplo(tuplo):
    return tuple(x for x in tuplo if x % 2 == 0)

print(pares_tuplo(tuplo))