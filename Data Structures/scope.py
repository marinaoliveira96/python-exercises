messageGlobal = 'oi do global'
message  = 'global = a'
def greet():
  if True:
    # local variable
    message = 'local = b'
  print(message)
  print(messageGlobal)

greet()
print(message)

# não tem block level scope
