i = media = maior = menor = 0
c = 's'
while c in 'Ss':
    n = int(input('Digite um número: '))
    i += 1
    if i == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    media += n
    c = input('Quer continuar? [S/N] ').lower().strip()[0]
print(f'Você digitou {i} números e a média foi {media/i}')
print(f'O maior valor foi {maior} e o menor {menor}')

