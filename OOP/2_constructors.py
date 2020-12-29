# Constructor: special method that is called when we create a new point object
class MyPoint:
  # magic method = constructor
  def __init__(self, x, y):
    # self: reference to a current point object
    self.x = x
    self.y = y
  def draw(self):
    print(f"Point ({self.x}, {self.y})")

point = MyPoint(1,2)
# print(point.x) # 1
point.draw()
