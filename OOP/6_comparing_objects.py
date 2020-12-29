class MyPoint:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  def __gt__(self, other):
    return self.x > other.x and self.y > other.y


point = MyPoint(4,8)
other = MyPoint(1,4)
print(point > other) # cada obj aponta pra um endereço diferente

# comparison magic methods

