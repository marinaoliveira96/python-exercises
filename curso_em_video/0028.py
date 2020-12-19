from random import randint
from time import sleep
from termcolor import colored

y = randint(0, 5)

print(colored('-=-', 'yellow') * 20)
print('Vou pensar em um numero entre 0 e 5, tente advinhar...')
print(colored('-=-','yellow') * 20)
x = int(input('Em que número pensei? '))
print(colored('PROCESSANDO..', 'magenta'))
sleep(2)

if x == y:
    print(colored(f'GANHOU! O número que pensei foi {y}', 'green'))
else:
    print(colored(f'GANHEI! O numero que pensei foi {y} e não o {x}', 'red'))
