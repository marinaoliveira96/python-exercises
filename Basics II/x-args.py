def multiply(*list):
  total = 1
  for number in list:
    total *= number
  return total

# *list é uma tuple com numeros
print(multiply(2,3,4,5))