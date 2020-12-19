x = float(input('Qual é a distancia da sua viagem? '))
print(f'Voce etá prestees a começar uma viagem de {x} Km.')
'''
if x > 200:
    print(f'O preço da passagem é de R${x*0.45}')
else:
    print(f'O preço da passagem é de R${x * 0.50}')
'''
preco = x * 0.50 if x <= 200 else x * 0.45
print(f'O preço da passagem é de R${preco}')