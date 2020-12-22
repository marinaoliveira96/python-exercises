bag = [10, 1234, 654, 99, 55]
print(len(bag))

for item in bag:
  print(f'item: {item}')

i = 1
while i < 11:
  print(i)
  i += 1


guess = 0
answer = 5

while answer != guess:
  guess = int(input('Guess: '))
else:
  print('you win')