# Generator Expressions 

from sys import getsizeof
values = (x * 2 for x in range(1000)) # generator object = mais leve, iteravel
for x in values:
  print(x)


print("gen:",getsizeof(values))