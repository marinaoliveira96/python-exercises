print('-=-' * 10)
print('     10 TERMOS DE UMA PA')
print('-=-' * 10)

t1 = int(input('Primeiro termo: '))
r = int(input('razao: '))
termo = t1
cont = 1
while cont <= 10:
    print(f'{termo} ->' , end='')
    termo += r
    cont += 1
print('FIM')

