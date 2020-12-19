pessoas = [['Marina', 23], ['Fernanda', 17], ['José', 50]]
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')
galera = list()
dado = list()
for c in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
