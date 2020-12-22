print(isinstance(3, int))

lista = ['marina', 2, 'jujuba']
lista2 = []

for i in lista:
  if isinstance(i, str):
    lista2.append(i)

print(lista2)


myList = ['marina', 123, 9.5]
print(isinstance(9.5, int))

#strings
items = ['marina', 123, 9.5]
print(isinstance(9.5, float))

str_items = ['abc', 'Abc','def', 'BBBB','ghi', 'AAAA']

str_items.sort(key=str.lower, reverse=True)
print(str_items)

new_items = sorted(str_items)
print(new_items)

#numbers
int_numbers = [123, 13.44, 5436, 324.54, 9034]

int_numbers.sort()
print(f'sort.() = {int_numbers}')

int_numbers.sort(reverse=True)
print(f'sort.(reverse=True) = {int_numbers}')

#esse sorted ta relacionado a lista n aos numeros
new_numbers = sorted(int_numbers, reverse=False)
print(f'new numbers = {new_numbers}')

total = sum(int_numbers)
print(total)
