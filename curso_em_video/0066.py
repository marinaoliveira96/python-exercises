s = i = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    i += 1
print(f'Foram digitados {i} números e a soma deles é {s}')

