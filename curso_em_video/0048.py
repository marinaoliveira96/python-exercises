soma = 0
cont = 0
for y in range(3, 501, 3):
    if y % 2 != 0:
        soma += y
        cont += 1
print(f'a soma é igual a {soma}')
print(f'numeros solicitados = {cont}')