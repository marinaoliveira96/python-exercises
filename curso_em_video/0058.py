from random import randint
x = randint(0, 10)
i = 1
print('''Sou seu computador... 
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
n = int(input('Qual é seu palpite? '))
while x != n:
    i += 1
    if x < n:
        print('Menos... tente mais uma vez.')
    elif x > n:
        print('Mais.. tente mais uma vez.')
    n = int(input('Qual é seu palpite? '))

print(f'Acertou com {i} tentativas. Parabens!')

