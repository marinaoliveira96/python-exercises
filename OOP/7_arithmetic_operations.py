class MyPoint:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __add__(self, other):
    return MyPoint(self.x + other.x, self.y + other.y)
  
  

point = MyPoint(10,8)
other = MyPoint(1,2)
combined = point + other
print(combined.y) # return 10



