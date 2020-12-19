listagem = ('lápis', 1.80,
            'boracha', 2,
            'caderno', 30.90,
            'estojo', 9.50,
            'caneta', 2.50)
print('-' * 30)
print('LISTAGEM DE PREÇOS')
print('-' * 30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>5.2f}')
