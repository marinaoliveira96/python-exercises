def plus(*args):
  result = 0
  for number in args:
    result += number
  print(result)

plus(1,2,1,2,3,1,1,1)

# def plus(a, b, *args, **kwargs):
#   print(args, kwargs)
#   # agrs (position) = tuple, kwargs (key arguments) = dict
#   return a + b

# plus(1,2,3,4)