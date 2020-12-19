x = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

op = int(input('Sua opção: '))

if op == 1:
    print(f'{x} convertido BINÁRIO para é igual a {bin(x)[2:]}')
elif op == 2:
    print(f'{x} convertido para OCTAL é igual a {oct(x)[2:]}')
elif op == 3:
    print(f'{x} convertido para HEXADECIMAL é igual a {hex(x)[2:]}')
else:
    print('Opção inválida. Tente novamente.')




