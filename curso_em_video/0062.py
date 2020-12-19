print('-=-' * 10)
print('     10 TERMOS DE UMA PA')
print('-=-' * 10)

mais = 1
t1 = int(input('Primeiro termo: '))
r = int(input('razao: '))
termo = t1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} ->', end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais? '))
print(f'Progressão finalizada com {total} termos digitados')


