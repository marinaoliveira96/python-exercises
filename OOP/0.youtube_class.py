class Dog:
  # esse metodo é chamado sempre que chamamos Dog() = criamos umas instancia
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_name(self):
    return self.name

  def get_age(self):
    return self.age

  def set_age(self ,age):
    self.age = age


d = Dog("Jujuba", 5) #new instance of dog
d.set_age(1)
print(d.age)
d2 = Dog("dino", 4)
print(type(d)) # <class '__main__.Dog'>