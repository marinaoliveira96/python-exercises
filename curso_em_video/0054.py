from datetime import date
atual = date.today().year
maiores = 0
menores = 0
ano = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    if atual - ano >= 18:
        maiores += 1
    else:
        menores += 1
print(f'''Ao todos tivemos {maiores} pessoas maiores de idade
E também tivemos {menores} pessoas menores de idade''')
