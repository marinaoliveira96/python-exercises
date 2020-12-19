print('-'*15)
print('LOJÃO DO BRÁS')
print('-'*15)
menor = total = cont = supercaro = 0
ncaro = ' '
while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if cont == 1 or preco < menor:
        menor = preco
        ncaro = nome
    if preco > 1000.00:
        supercaro += 1
    c = ' '
    while c not in 'sn':
        c = input('Quer continuar?').strip().lower()[0]
    if c == 'n':
        break
print('FIM DO PROGRAMA')
print(f'''O total da compra foi R${total}
Temos {supercaro} produtos custando mais que R$1000.00
O produto mais BARATO foi {ncaro} que custa R${menor}''')
