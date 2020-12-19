from random import randint
x = randint(0, 10)
i = 0
acertou = False
print('''Sou seu computador... 
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
while not acertou:
    n = int(input('Qual é seu palpite? '))
    i += 1
    if n == x:
        acertou = True
    else:
        if x < n:
            print('Menos... tente mais uma vez.')
        elif x > n:
            print('Mais.. tente mais uma vez.')

print(f'Acertou com {i} tentativas. Parabens!')
