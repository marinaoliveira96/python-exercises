from termcolor import colored
sal = float(input('Qual é o salário: R$'))
a1 = sal + sal * 0.1
a2 = sal + sal * 0.15

if sal > 1250:
    print(colored(f'Quem ganhava R${sal} agora ganha {a1}', 'red'))
else:
    print(f'Quem ganhava R${sal} agora ganha {a2}')