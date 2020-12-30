class TagCloud:
  def __init__(self):
    self.tags = {}

  def add(self, tag):
    self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
  
  def __getitem__(self, tag):
    return self.tags.get(tag.lower(), 0)

  def __setitem__(self, tag, count):
    self.tags[tag.lower()] = count
  
  def __len__(self):
    return len(self.tags)
  
  def __iter__(self):
    return iter(self.tags) # essa função retorna um obj iterable, 1 item por vez em for loop


cloud = TagCloud()
cloud["python"] = 10
len(cloud)
cloud.add("Python")
cloud.add("pyTHon")
cloud.add("PYTHON")
print(cloud.tags)