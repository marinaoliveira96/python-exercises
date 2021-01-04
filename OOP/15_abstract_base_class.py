from abc import ABC, abstractmethod
class InvalidOperationError(Exception):
  pass

class Stream(ABC):
  def __init__(self):
    self.oponend = False
    
  def open(self):
    if self.oponend:
      raise InvalidOperationError("Stream is already open")
    self.oponend = True

  def close(self):
    if not self.oponend:
      raise InvalidOperationError("Stream is already closed")
    self.oponend = False
  
  @abstractmethod
  def read(self):
    pass

class FileStream(Stream):
  def read(self):
    print("Reading data from a file")

class NetworkStream(Stream):
  def read(self):
    print("Reading data from a stream")

strem = Stream()
stream.open() # TypeError: Can't instantiate abstract class Stream with abstract method read
