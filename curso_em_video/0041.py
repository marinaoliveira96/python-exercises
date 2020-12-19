from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print(f'O atleta nasceu em {ano} e tem {idade} anos')

if idade <= 9:
    print('Classificação: MIRIM')
elif 9 < idade <= 14:
    print(f'Classificção: INFANTIL')
elif 14 < idade <= 19:
    print('Classificação: JUNIOR')
elif 19 < idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
