n = input('Digite uma palavra/frase: ').strip().upper()
pal = n.split()
junto = ''.join(pal)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('temos um palindromo')
else:
    print('não temos um palindromo')
print(junto, inverso)