val = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMAMENTO'
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual é a opção? '))
if op == 1:
    des = val - (val * 0.1)
    print(f'O preço é R$ {val} e o valor à vista com desconto de 10% é R$ {des:.2f}')
elif op == 2:
    des = val - (val * 0.5)
    print(f'O preço é R$ {val} e o valor à vista no cartão, com desconto de 5% é R$ {des:.2f}')
elif op == 3:
    print(f'Em até 2x vezes no cartão o preço é de R${val}')
elif op == 4:
    juros = val + (val * 0.2)
    print(f'O preço é R$ {val} e o valor com juros de 20% é R$ {juros:.2f}')
else:
    print('Opção inválida de pagamento')
