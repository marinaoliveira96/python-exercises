class MyPoint:
  # class attributes: compartilhados por todas as instancias de uma class
  defult_color = "red"
  def __init__(self, x, y):
    self.x = x
    self.y = y
# x, y, e z são instances attributes = atributos do objeto pointe e another
  def draw(self):
    print(f"Point ({self.x}, {self.y})")

point = MyPoint(1,2)
print(point.defult_color)
print(MyPoint.defult_color)

point.z = 10
point.draw()

another = MyPoint(3, 4)
another.draw()

