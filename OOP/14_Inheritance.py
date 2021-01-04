class InvalidOperationError(Exception):
  pass

class Stream:
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
    
class FileStream(Stream):
  def read(self):
    print("Reading data from a file")

class NetworkStream(Stream):
  def read(self):
    print("Reading data from a stream")