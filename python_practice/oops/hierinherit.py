class shape:
  def area(self):
    pass

class Circle(shape):
  def __init__(self, radius):
    self.radius = radius
  
  def area(self):
    return 3.14 * self.radius**2

class Rectangle(shape):
  def __init__(self, length, breadth):
    self.length = length   
    self.breadth = breadth
  
  def area(self):
    return self.length * self.breadth

def main():
  c = Circle(3)
  s = Rectangle(3,4)
  print( c.area() )
  print( s.area() )

main()