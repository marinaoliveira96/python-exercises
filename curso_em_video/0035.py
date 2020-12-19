a = float(input('Qual é a medida 1? '))
b = float(input('Qual é a medida 2? '))
c = float(input('Qual é a medida 3? '))

if a < b + c and b < a + c and c < a + b:
    print(f'PODE formar um triangulo')
else:
    print(f'NÃO pode formar um triangulo')



