x = int(input('Primeiro número: '))
y = int(input('Segundo número: '))

if x > y:
    print(f'O primeiro valor é maior: {x} > {y}')
elif x < y:
    print(f'O segundo valor é maior: {y} > {x}')
else:
    print('Os dois valores são iguais')