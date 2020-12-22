class Car():
 def __init__(self, **kwargs):
  self.wheels = 4
  self.doors = 4
  self.windows = 4
  self.seats = 4
  self.color = kwargs.get('color', 'black')
  self.price = kwargs.get('price', '$20')

  def __str__(self):
    return f'Car with {self.wheels} wheels'
  
  

class Convertible(Car):
  def __init__(self, **kwargs):
    # super tá chamando o pai
    super().__init__(**kwargs)
    self.time = kwargs.get('time', 10)

  def take_off(self):
    return 'taking off'

porche = Convertible(color='Red', price='$40')
print(porche.color)
