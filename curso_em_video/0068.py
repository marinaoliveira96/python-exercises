from random import randint
c = soma = 0
print('=-='*15)
print('VAMOS BRINCAR DE PAR OU IMPAR?')
print('=-='*15)
vencer = True
while True:
    vj = int(input('Diga um valor: '))
    j = input('Par ou Impar [P/I]: ').lower().strip()
    vpc = randint(0, 10)
    soma = vj + vpc
    if j == 'p':
        if soma % 2 == 0:
            print(f'Você digitou {vj} e o Computador {vpc}. Total de {soma}. Deu PAR')
            print('=-=' * 15)
            print('VOCÊ VENCEU.')
            c += 1
            vencer = True
        else:
            print(f'Você digitou {vj} e o Computador {vpc}. Total de {soma}. Deu IMPAR')
            print('=-=' * 15)
            print('VOCÊ PERDEU.')
            vencer = False
            break
    elif j =='i':
        if soma % 2 == 0:
            print(f'Você digitou {vj} e o Computador {vpc}. Total de {soma}. Deu PAR')
            print('=-=' * 15)
            print('VOCÊ PERDEU.')
            vencer = False
            break
        else:
            print(f'Você digitou {vj} e o Computador {vpc}. Total de {soma}. Deu IMPAR')
            print('=-=' * 15)
            print('VOCÊ VENCEU.')
            c += 1
            vencer = True
print(f'Você ganhou {c} veze(s)')


