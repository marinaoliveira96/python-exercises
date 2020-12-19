pessoas = [['Marina', 23], ['Fernanda', 17], ['josé', 50]]
print(pessoas[0][0])
teste = []
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
