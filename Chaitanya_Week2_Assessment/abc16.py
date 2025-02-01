"""
Create an interface `IShape` with an abstract method `calculate_area()`. Implement it in `Rectangle` and `Circle` classes.

"""

from abc import ABC, abstractmethod #Importing module for implementing abstract class

class IShape(ABC):   # Defining an abstract class for shapes
  @abstractmethod
  def calculate_area():   #Abstract Method
    pass

class Rectangle(IShape):   # Rectangle class inheriting from IShape
  def calculate_area(self, l, b):
    print(f"Area of Rectangle: {l*b}")

class Circle(IShape):
  def calculate_area(self, r):    #Implementing abstract method
    print(f"Area of circle: {(3.14)*r*r}")

def main():

  rct = Rectangle()
  rct.calculate_area(8,4)
  crc = Circle()
  crc.calculate_area(4)

main()