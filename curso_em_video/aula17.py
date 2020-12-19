lanche = ['pizza', 'hambuerguer', 'pudim', 'bolo']
lanche.append('café')
print(lanche)
lanche.insert(0, 'chocolate')
print(lanche)
del lanche[2]
print(lanche)
lanche.pop()
print(lanche)
if 'pudim' in lanche:
    lanche.remove('pudim')
print(lanche)
num = [7, 3, 4, 1]
num.append(9)
print(num)
num.sort(reverse=True)
num.insert(2, 3)
num.remove(3)
print(num)
print(f'Essa lista tem {len(num)} elementos')