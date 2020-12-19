valores = list()
for c in range(0, 4):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}')
print('Cheguei ao fim da lista')

a = [1, 2, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')