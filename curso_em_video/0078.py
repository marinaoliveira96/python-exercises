lista = list()
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        menor = maior = lista [c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
         menor = lista[c]
print(f'Os valores digitados foram: {lista}')
#print(f'O maior valor digitado foi {maior} nas posições {lista.index(maior)}.. ')
#print(f'O menor valor digitado foi {menor} nas posições {lista.index(menor)}.. ')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O maior valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
