n1 = int(input('Informe o 1° número: '))
n2 = int(input('Informe o 2° número: '))
op = 0
while op != 5:
    print('''         [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números 
        [ 5 ] sair do programa''')
    op = int(input('>>>>>> Qual é a sua opção?'))
    if op == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif op == 2:
        print(f'{n1} * {n2} = {n1 * n2}')
    elif op == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        elif n2 > n1:
            print(f'O maior número é {n2}')
        else:
            print('Os numeros são iguais')
    elif op == 4:
        n1 = int(input('Informe o 1° número: '))
        n2 = int(input('Informe o 2° número: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)