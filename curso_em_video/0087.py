matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = col3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'[{l}][{c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            col3 += matriz[l][c]
    print()
    if l and c == 1:
        maior = matriz[l][c]
    else:
        if l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
print(f'A soma dos numeros pares é {soma}')
print(f'A soma dos valores da 3 coluna é {col3}')
print(f'O maior numero da 2 linha é {maior}')