class Animal:
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
m.eat()
print(m.age)