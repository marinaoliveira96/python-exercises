vel = int(input('Qual é a velocidade atual do carro? '))
multa = (vel - 80) * 7
if vel > 80:
    print(f'A sua velocidade é {vel}Km/h e está acima do permitido. Multa de R${multa:.2f}')
print('Tenha um bom dia, dirija com segurança')

