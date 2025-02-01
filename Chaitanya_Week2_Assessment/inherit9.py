"""
Simulate multiple inheritance where `FlyingCar` inherits from both `Car` and `Airplane`. Handle potential conflicts in the `move()` method.

"""

class Car:
  def move(self):  # Car movement method
    print("Driving on the road.")

class Airplane:
  def move(self):  # Airplane movement method
    print("Flying in the sky.")

class FlyingCar(Car, Airplane):
  def move(self, way):  # FlyingCar move method with conditional behavior
    if way == 'drive':
      super().move()  # Calls Car's move method
    else:
      Airplane.move(self)  # Calls Airplane's move method

def main():  # Main function to demonstrate FlyingCar movement
  fc = FlyingCar()
  fc.move("drive")
  fc.move("fly")
  fc.move("drive")

main()
