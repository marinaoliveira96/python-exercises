class TagCloud:
  def __init__(self):
    self.__tags = {}

  def add(self, tag):
    self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1
  
  def __getitem__(self, tag):
    return self.__tags.get(tag.lower(), 0)

  def __setitem__(self, tag, count):
    self.__tags[tag.lower()] = count
  
  def __len__(self):
    return len(self.__tags)
  
  def __iter__(self):
    return iter(self.__tags) # essa função retorna um obj iterable, 1 item por vez em for loop

cloud = TagCloud()
print(cloud.__dict__) # {'_TagCloud__tags': {}}

# private memebers = acessiveis do lado de fora