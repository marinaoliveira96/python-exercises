from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = 2019-nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
sexo = input('Qual é o seu sexo? Digite M para masculino e F para feminino: ').lower()

if sexo == 'f':
    print('Você não precisa se alistar.')
elif sexo == 'm':
    print('Você é homem e precisa se alistar.')
    if idade > 18:
        print(f'Você já deveria ter se alistado há {idade - 18} anos')
        print(f'Seu alistamento foi em {atual - (idade - 18)}')
    elif idade < 18:
        print(f'Você tem que se alistar daqui {18 - idade} anos')
        print(f'Seu alistamento será em {atual - (idade - 18)} ')
    else:
        print(f'Você tem que se alistar IMEDIATAMENTE')
else:
    print('ERRO.')


