tempo = int(input('qubatos anos tem seu carro? '))
print('carro novo' if tempo<=3 else 'carro velho')
print('--FIM--')
nome = input('qual é o seu nome? ')
if nome == 'Marina':
    print('que nome lindo você tem')
print(f'Bom dia {nome}')

n1 = float(input('digite a nota 1: '))
n2 = float(input('digite a nota 2: '))
m = (n1+n2)/2
print(f'sua media foi {m}')
if m >= 6:
    print('parabens, sua media foi boa')
else:
    print('estude mais')
