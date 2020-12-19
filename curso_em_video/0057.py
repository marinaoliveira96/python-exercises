n = input('Informe seu sexo [M/F]: ').strip().upper()[0]
while n not in 'MmFf':
    n = input('Dados inválidos. Informe seu sexo [M/F]: ')
print(f'Sexo {n} cadastrado com sucesso')
