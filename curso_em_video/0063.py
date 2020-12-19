n = int(input('entre com um numero: '))
f1 = 0
f2 = 1
print(f'{f1} => {f2}', end='')
x = 3
while x < n:
    f3 = f1 + f2
    print(f' => {f3}', end='')
    f1 = f2
    f2 = f3
    x += 1
print('\nfim')

