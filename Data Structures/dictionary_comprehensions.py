#  Dictionary Comprehensions 

values = {x: x* 2  for x in range(5)}
print(values)

# values = []
# for x in range(5):
#   values.append(x*2)

# [expression for item in items]
# values = [x* 2  for x in range(5)]

#  tuples
tuple_values = (x * 2 for x in range(5))
print(tuple_values) # generator object