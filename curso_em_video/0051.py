print('-=-' * 10)
print('     10 TERMOS DE UMA PA')
print('-=-' * 10)

t1 = int(input('Primeiro termo: '))
r = int(input('razao: '))
decimo = t1 + (10-1) * r
for i in range(t1, decimo + r, r):
    print(f'{i}', end=' =>')
print('ACABOU')
