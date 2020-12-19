n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero. [Digite 999 para parar]: '))
    cont += 1
    soma += n
print(f'foram digitados {cont} numeros e a soma deles é igual a {soma-999}')