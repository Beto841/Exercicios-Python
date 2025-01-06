v = [('caderno', 10, 150, 0.5),  ('lápis', 75, 220, 0.15), ('tesoura', 234, 50, 2.4)]

def filtra_produtos(v, preço):
    if not v or preço < 0:
        return ()
    
    return tuple({'prod': i[0], 'num': i[1]} for i in v if i[3] >= preço and i[2] > 0)

print(filtra_produtos(v, 0.5))