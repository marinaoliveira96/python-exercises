# set = lista sem duplicates, não estão em ordem e não tem index

numbers = [1,1,2,3,4]
first = set(numbers)
second = {1,5}

print(first | second) # union of sets
print(first & second) # numero que tenha nos 2 sets
print(first - second) # diferença entre os sets
print(first ^second) # simetrical diference