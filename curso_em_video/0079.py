lista = list()
c = n = 0
while True:
    n = (int(input('Digite um numero: ')))
    if n in lista:
        print('Numero já cadastrado')
        lista.remove(n)
    else:
        print('Numero cadastrado com sucesso')
    lista += [n]
    c = input('Deseja continuar? [S/N]')
    if c in 'nN':
        break
print(f'Você digitou os valores {lista}')
