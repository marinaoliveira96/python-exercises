maiores = masc = fem20 = 0
while True:
    idade = int(input('Qual a sua idade? '))
    if idade > 18:
        maiores += 1
    sexo = input("Qual é o seu sexo? [F/M] ").strip().lower()[0]
    if sexo == 'm':
        masc += 1
    elif sexo == 'f':
        if idade < 20:
            fem20 += 1
    c = ' '
    while c not in 'sn':
        c = input('Deseja continuar? [S/N]').strip().lower()[0]
    if c == 'n':
        break
print(f'''Programa encerrado
total de pessoas com mais de 18 anos igual a {maiores}
total de homens cadastrados igual a {masc}
Total de mulheres com menos de 20 anos igual a {fem20}''')

