n = input('Digite uma palavra/frase: ').strip().upper().replace(' ', '')
if n == n[::-1]:
    print('é palindromo')
else:
    print('n é palindromo')

print(n, n[::-1])