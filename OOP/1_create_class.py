# Class: blueprint for creating new objects
# Oject: instance of a class
class MyPoint:
  # todas as funções tem que ter pelo menos um parametro
  def draw(self):
    print("draw")

point = MyPoint()
print(type(point)) # <class '__main__.MyPoint'> main = name of the module
print(isinstance(point, MyPoint)) # True