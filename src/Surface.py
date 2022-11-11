from Rectangle import Rectangle

class Surface:
  def __init__(self, filename, x, y, height, width):
    self.rect = Rectangle(x,y,height,width)
    self.image = filename

  def getRect(self):
    return self.rect