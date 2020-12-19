tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    n = int(input('digite um numero de 0 a 10: '))
    if 0 <= n <= 10:
        break
    print(f'tente novamente')
print(f'o numero digitado foi {tupla[n]}')