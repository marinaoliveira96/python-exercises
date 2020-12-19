print(f'{"DESAFIO 081":=^25}')
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar: [S/N]: ')).upper()[0].strip()
    while resp not in 'SN':
        resp = str(input('Digite uma opção válida. Quer continuar: [S/N]: ')).upper()[0].strip()
    if resp == 'N':
        break
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista digitada é ordem decrescente é {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista e está nas posições ',end='')
    for pos, valor in enumerate(lista):
        if valor == 5:
            print(f'{pos}...', end='')
else:
    print('O valor 5 não está na lista.')