casa = float(input('Qual o valor da casa?'))
sal = float(input('Qual é o valor do seu salário? '))
anos = int(input('Em quantos anos você vai pagar?'))
prest = casa / (anos * 12)
if prest > sal * 30 / 100:
    print('Empréstimo negado')
else:
    print('Emprestimo aprovado')