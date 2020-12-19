n = int(input('Digite um numero: '))
i = 0
if n == 1:
    print(f'O numero {n} NÃO é PRIMO')
elif n == 2:
    print(f'O numero {n} é PRIMO')
else:
    for c in range(1, n+1):
        if n % c == 0:
            print(f'\033[34m', end=' ')
            i = i+ 1
        else:
            print('\033[m', end=' ')
        print(f'{c}', end=' ')
    if i > 2:
        print(f'\nO numero {n} NÃO é PRIMO')
    else:
        print(f'\nO numero {n} é PRIMO')

