pal = ('marina', 'nascimento', 'de', 'oliveira')
for p in pal:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in'aeiou':
            print(letra, end='')
