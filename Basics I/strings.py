# strings = immutables
course = 'Python Programming'
print(len(course))

# pega a última letra
print(course[-1])

#slice
print(course[0:3])

#retorna a string toda
print(course[0:])

# immutables
print(id(course))
print(id(course[0]))

# formatted string
first = "Marina"
last = "Oliveira"
full = f"Hello {first} {last}!"

print(full)