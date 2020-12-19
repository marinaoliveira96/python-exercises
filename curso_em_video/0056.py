menor = 0
velho = 0
media = 0
for i in range(1, 5):
    print('-'*4, f'{i}° pessoa', '-'*4)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ').lower()
    if sexo == 'f':
        if idade < 20:
            menor += 1
    if sexo == 'm':
        if i == 1:
            velho = idade
        else:
            if idade > velho:
                hvelho = nome
    media += idade

print(f'''Tem {menor} mulheres menores de 20
a media de idade do grupo é {media/4}
e o homem mais velho se chama {hvelho}''')





