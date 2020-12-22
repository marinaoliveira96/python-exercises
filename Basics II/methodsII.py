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

porche = Car(color='Red', price='$40')
print(porche.color, porche.price)

mini = Car()
print(mini.price, mini.price)


#print(dir(Car))
#dir lista as coisas dentro de uma classe, de um obj (todas as propiedades)

#str chamado toda vez q vc printa uma instancia de uma classe

# init (cria a class)