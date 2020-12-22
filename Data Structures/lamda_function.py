# Lambda Functions == anonymous function
# função que só vamos usar uma vez e a passamos como parametro em outra função
items = [
  ('Product1', 10),
  ('Product2', 9),
  ('Product3', 12),
]

# function(key=lambda parameters:expression)
items.sort(key=lambda item:item[1])
print(items)