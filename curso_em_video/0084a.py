temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    r = input('Deseja continuar? [S/N]: ')
    if r in 'nN':
        break
print(f'Lista dos cadastrados: {princ}')
print(f'foram cadastradas {len(princ)} pessoas')
print(f'o maior peso foi {mai} Kg. ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}')
print(f'o menor peso foi {men} Kg. ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}')
