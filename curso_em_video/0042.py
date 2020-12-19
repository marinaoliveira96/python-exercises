a = float(input('Qual é a medida 1? '))
b = float(input('Qual é a medida 2? '))
c = float(input('Qual é a medida 3? '))

if a < b + c and b < a + c and c < a + b:
    print(f'PODE formar um triangulo')
    if c == a == b:
        print('Equilátero: todos os lados são iguais')
    elif b == a or b == c or a == c:
        print('Isósceles: dois lados diferentes')
    else:
        print('Escaleno: todos os lados diferentes')
else:
    print(f'NÃO pode formar um triangulo')