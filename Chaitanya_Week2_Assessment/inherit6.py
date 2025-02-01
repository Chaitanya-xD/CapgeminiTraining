"""
Implement a multi-level inheritance example where `Vehicle` is a base class, `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.

"""

class Vehicle:
  def Wheels(self, wheels):  # Method to set wheels
    self.wheels = wheels

  def Capacity(self, capacity):  # Method to set capacity
    self.capacity = capacity

  def display(self):  # Method to display basic vehicle info
    print("This is a vehicle")

class Car(Vehicle):
  def __init__(self, wheels, capacity):  # Initializing car with wheels and capacity
    super().Wheels(wheels)
    super().Capacity(capacity)

  def display(self):  # Display car details
    print(f"This is a car with {self.wheels} wheels")

class Bike(Vehicle):
  def __init__(self, wheels, capacity):  # Initializing bike with wheels and capacity
    super().Wheels(wheels)
    super().Capacity(capacity)

  def display(self):  # Display bike details
    print(f"This is a bike with {self.wheels} wheels")

class ElectricCar(Car):
  def __init__(self, wheels, capacity, Range):  # Initializing electric car with wheels, capacity, and range
    super().__init__(wheels, capacity)
    self.Range = Range

  def display(self):  # Display electric car details
    print(f"This is an Electric Car with {self.Range} Km Range")

def main():  # Main function to display details of all vehicles
  vehicle = Vehicle()
  vehicle.display() 

  car = Car(4, 5)
  car.display() 

  bike = Bike(2, 2)
  bike.display() 

  ecar = ElectricCar(4, 5, 400)
  ecar.display()

main()
