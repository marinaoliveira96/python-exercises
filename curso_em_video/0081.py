lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    r = input('Deseja continuar? [S/N]')
    if r in 'nN':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    for c, v in enumerate(lista):
        if v == 5:
            print(f'o valor 5 está na lista, na posição {c}')
else:
    print('O valor 5 não está na lista')
