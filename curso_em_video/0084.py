lista = list()
dados = list()
maior = menor = nM = menorN = cad = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    cad +=1
    r = input('Deseja continuar? [S/N]: ')
    if r in 'nN':
        break
for p in lista:
    if p == 0:
        maior = menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]
            nM = p[0]
        if p[1] < menor:
            menor = p[1]
            menorN = p[0]
print(f'Foram cadastrados {cad} pessoas.')
print(f'O maior peso foi {maior}, de {nM}')
print(f'O menor peso foi {menor} de {menorN}')
#for p, v in enumerate(lista):
#    print(f'{v[0]}')

