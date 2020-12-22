#sequences types: list & tuples
#Listas são mutáveis

days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
print('Mon' in days) # True
print(len(days)) # 5

days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
print(days) # ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
days.append('Sat')
print(days) # 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']