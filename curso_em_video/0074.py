from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for n in num:
    print(f'{n} ', end='')
print(f'\no menor valor foi {min(num)}')
print(f'o maior valor foi {max(num)}')