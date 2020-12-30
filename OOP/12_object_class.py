# todas as classes derivam do object class (direta ou indiretamente)
class Animal(object):
  def __init__(self):
    self.age = 1

  def eat(self):
    print("eat")
    
# Animal: parent, base
# Mammal: Child, sub
class Mammal(Animal):
  def walk(self):
    print("walk")

class Fish(Animal):
  def swin(self):
    print("swin")

m = Mammal()
isinstance(m, Animal)
isinstance(m, object)
o = object() #have the magic methods
print(issubclass(Mammal, Animal)) #if a class derives form another class
