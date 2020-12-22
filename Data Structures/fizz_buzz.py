def fizz_buzz(input):
  int(input)
  if input % 3 == 0 and input % 5 == 0:
    return 'fizz_buzz'
  elif input % 3 == 0:
    return 'Fizz'
  elif input % 5 == 0:
    return 'Buzz'
  else:
   return input



print(fizz_buzz(8))

# 3 = fizz
# 5 = buzz
# 3 and 5 = fizz_buzz