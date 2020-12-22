# pode retornar 2 valores
def increment(number: int, by: int=1) -> tuple:
  return (number, number + by)

#keyword argument = mais legivel
#print(increment(2, by=3))
print(increment(2))