fer = []
par = []
impar = []
while True:
    fer.append(int(input('Digite um numero: ')))
    r = input('Deseja continuar [S/N]: ').lower()
    if r in 'n':
        break
for m, n in enumerate(fer):
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f'Os numeros digitados foram: {fer}')
print(f'Os numeros pares são {par}')
print(f'Os numeros impares são {impar}')

