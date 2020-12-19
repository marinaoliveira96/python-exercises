from random import randint
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
op = int(input('Qual é a sua jogada? '))
pc = randint(0, 3)
print('''JO
KEN
PO!!!''')

if op < 0 or op > 2:
    print('OPÇÃO INVÁLIDA!')
if op == pc:
    if op == 0:
        print('-=-' * 9)
        print(f'Coputador jogou PEDRA')
        print(f'Jogador jogou PEDRA')
        print('-=-' * 9)
    elif op == 1:
        print('-=-' * 9)
        print(f'Coputador jogou PAPEL')
        print(f'Jogador jogou PAPEL')
        print('-=-' * 9)
    elif op == 2:
        print('-=-' * 9)
        print(f'Coputador jogou TESOURA')
        print(f'Jogador jogou TESOURA')
        print('-=-' * 9)
    print('EMPATE')
else:
    if op == 0 and pc == 1:
        print('-=-' * 9)
        print(f'Coputador jogou PAPEL')
        print(f'Jogador jogou PEDRA')
        print('-=-' * 9)
        print('COMPUTADOR VENCE')
    elif op == 0 and pc == 2:
        print('-=-' * 9)
        print(f'Coputador jogou TESOURA')
        print(f'Jogador jogou PEDRA')
        print('-=-' * 9)
        print('JOGADOR VENCE')
    elif op == 1 and pc == 0:
        print('-=-' * 9)
        print(f'Coputador jogou PEDRA')
        print(f'Jogador jogou PAPEL')
        print('-=-' * 9)
        print('JOGADOR VENCE')
    elif op == 1 and pc == 2:
        print('-=-' * 9)
        print(f'Coputador jogou TESOURA')
        print(f'Jogador jogou PAPEL')
        print('-=-' * 9)
        print('COMPUTADOR VENCE')
    elif op == 2 and pc == 0:
        print('-=-' * 9)
        print(f'Coputador jogou PEDRA')
        print(f'Jogador jogou TESOURA')
        print('-=-' * 9)
        print('COMPUTADOR VENCE')
    elif op == 2 and pc == 1:
        print('-=-' * 9)
        print(f'Coputador jogou PAPEL')
        print(f'Jogador jogou TESOURA')
        print('-=-' * 9)
        print('JOGADOR VENCE')




