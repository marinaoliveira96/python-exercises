def sum(x, y):
  return int(x) + int(y)

def minus(x, y):
 return int(x) - int(y)

def divide(x, y):
  return int(x) / int(y)

def multiply(x, y):
  return int(x) * int(y)

def power(x,y):
  return int(x) ** int(y)

def rest(x, y):
  return int(x) % int(y)

def negated(x):
  return - int(x) 

print(sum(2, 2))
print(minus(2, 2))
print(divide(2, '2'))
print(multiply(2, 2))
print(rest(2, 2))
print(negated('1'))