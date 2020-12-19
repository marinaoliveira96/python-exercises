lanche = ('harmburguer', 'suco', 'pizza', 'pudim')
print(lanche[2:])
for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')
#for pos, comida in enumerate(lanche):
#    print(f'eu vou comer {comida} na posição {pos}')
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5))
print(c.index(5, 1))