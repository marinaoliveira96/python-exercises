class MyPoint:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # @ decorator
  @classmethod 
  def zero(cls): # cls = class method 1 parameter
    return cls(0,0)

  def draw(self):
    print(f"Point ({self.x}, {self.y})")

point = MyPoint.zero() # factory method: creates a new object
point.draw()