n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
fat = 1
print(f'calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat *= c
    c -= 1
print(f'{fat}')

