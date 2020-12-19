a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
c = int(input('Terceiro numero: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'menor valor é {menor}')

#verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O maior valor é {maior}')

