class Person:
  number_of_people = 0 # especifico da class
  GRAVITY = -9.8

  def __init__(self, name):
    self.name = name
    Person.add_person()
  
  @classmethod #decorator
  def number_of_people_m(cls):
    return cls.number_of_people

  @classmethod #decorator
  def add_person(cls):
    cls.number_of_people += 1

p1 = Person("Marina")
p2 = Person("Fernanda")
print(Person.number_of_people_m())