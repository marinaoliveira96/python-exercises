def say_hello(name, age):
  return f'hello {name} you are {age} years old'

hello = say_hello(name='nico', age='12')
print(hello)

items = ['marina', 9, 5, 'fernanda', 4, 20020, 'Irraaa', 9.5]

def parse_lists(some_list):
  str_list_items = []
  num_list_items = []
  for i in some_list:
    if isinstance(i, float) or isinstance(i, int):
      num_list_items.append(i)
    elif isinstance(i, str):
      str_list_items.append(i)
    else:
      pass
  return str_list_items, num_list_items

print(parse_lists(items))
