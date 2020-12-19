lista = list ()
while True:
    n = int(input('Digite um numero: '))
    if n not in lista:
        lista.append(n)
        print('valor adicionado')
    else:
        print('Numero repetido')
    r = input('Deseja continuar? ')
    if r in 'nN':
        break
print('-=-' * 15)
lista.sort()
print(f'Numeros adicionados foram {lista}')