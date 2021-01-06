class Pet: #general
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def show(self):
    print(f"I am {self.name} and I am {self.age} years old")
  
  def speak(self):
    print("I don't speak...")

class Cat(Pet):
  def __init__(self, name, age, color):
    super().__init__(name, age) # class que herdamos
    self.color = color

  def speak(self):
    print("Meow")
  
  def show(self):
    print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
  def speak(self):
    print("Bark")

class Fish(Pet):
  pass 

p = Pet("Pet", 5)
p.speak()
c = Cat("Bingus", 3, "Yellow")
c.show()
d = Dog("Jujuba", 5)
d.show()

f = Fish("Beta", 1)
f.speak()