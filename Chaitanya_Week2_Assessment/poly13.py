"""
Develop a `Shape` class with a method `area()`. Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.

"""
class Shape:
  def area():  # Base method for calculating area
    print("Calculating Area")

class Square(Shape):
  def area(self, n):  # Calculate area of square
    print(f"Area of Square: {n*n}")

class Triangle(Shape):
  def area(self, b, h):  # Calculate area of triangle
    print(f"Area of Triangle: {(0.5)*b*h}")

def main():  # Main function to demonstrate area calculations
  sq = Square()
  sq.area(4)
  tr = Triangle()
  tr.area(2,4)

main()
