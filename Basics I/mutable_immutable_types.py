# memory location address
# os tipos primarios são imutaveis
x = 1
print(id(x))

# não muda o valor no endereço de memória, o python aloca outro endereço
x = x + 1
print(id(x))

# listas são mutáveis, então quando mudamos uma lista o endereço de memória permanece o mesmo
y = [1,2,3,]
print(id(y))

y.append(4)
print(id(y))