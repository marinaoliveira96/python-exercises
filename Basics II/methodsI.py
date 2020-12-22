class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4
  # methos => function inside a class
  # o 1 argumento (self) de cada método é a instancia que chama o método
  def start(self):
    print(self.color)
    print('I started')

porche = Car()
porche.color = 'Red'
porche.start()