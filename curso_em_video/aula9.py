frase = 'Curso em Video Python'
print(frase[9::3])
print(len(frase))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('andoid'))
print('Curso' in frase)
print(frase.replace('python', 'android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
dividido = frase.split()
print((dividido[0]))


f2 = '  aprendendo python  '
print(f2.strip())
print(f2.lstrip())
print('-'.join(frase))