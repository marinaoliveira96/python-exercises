class Animal(object):
  def __init__(self):
    print("Animal Constructor")
    self.age = 1

  def eat(self):
    print("eat")
    
class Mammal(Animal):
  def __init__(self): #esse constructor substitui o da base
    print("Mammal Constructor")
    self.weight = 2
    super().__init__()

  def walk(self):
    print("walk")

class Fish(Animal):
  def swin(self):
    print("swin")

m = Mammal()
print(m.age) # AttributeError: 'Mammal' object has no attribute 'age'
print(m.weight)