"""
Develop an interface `IVehicle` with abstract methods `start_engine()` and `stop_engine()`. Implement it in `Car`, `Bike`, and `Truck` classes.

"""
from abc import ABC, abstractmethod  # Importing ABC and abstractmethod

class IVehicle(ABC):  # Abstract base class for vehicle operations
  @abstractmethod
  def start_engine(self):  # Abstract method to start the engine
    pass
  
  @abstractmethod
  def stop_engine(self):  # Abstract method to stop the engine
    pass

class Car(IVehicle):  # Car class implementing IVehicle
  def start_engine(self):  
    print("Starting a Car...")

  def stop_engine(self):  
    print("Turning off the Car engine")

class Bike(IVehicle):  # Bike class implementing IVehicle
  def start_engine(self):  
    print("Starting a Bike...")

  def stop_engine(self):  
    print("Turning off the Bike engine")

class Truck(IVehicle):  # Truck class implementing IVehicle
  def start_engine(self):  
    print("Starting a Truck...")

  def stop_engine(self):  
    print("Turning off the Truck engine")

def main():  # Main function
  car = Car()  
  bike = Bike()  
  truck = Truck()  

  car.start_engine()  
  car.stop_engine()
  
  bike.start_engine()  
  bike.stop_engine()
  
  truck.start_engine()  
  truck.stop_engine()

main()  
