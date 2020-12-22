# Unpacking Operator 
numbers = [1,2,3]
print(*numbers) # 1 2 3

values = [*range(5), *"Hello"]
print(values)

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)