"""
Implement an abstract class `ICalculator` with methods `add()`, `subtract()`, `multiply()`, and `divide()`. Create a `BasicCalculator` class that implements these methods.

"""

from abc import ABC, abstractmethod  # Importing ABC and abstractmethod

class ICalculator:  # Abstract base class for calculator operations
  @abstractmethod
  def add(self, a, b):  
    pass
  
  @abstractmethod
  def subtract(self, a, b):  
    pass
  
  @abstractmethod
  def multiply(self, a, b):  
    pass
  
  @abstractmethod
  def divide(self, a, b):  
    pass

class BasicCalculator(ICalculator):  # BasicCalculator class implementing abstract methods
  #Implementation of abstract methods
  def add(self, a, b):  
    return a + b
  
  def subtract(self, a, b):  
    return a - b
  
  def multiply(self, a, b):  
    return a * b
  
  def divide(self, a, b):  
    return a / b
  

def main():  
  calc = BasicCalculator()  
  a, b = map(int, (input("Enter two numbers: ").split()))  #Taking input to perform operations 

  print(f"Sum = {calc.add(a,b)}")  
  print(f"Difference = {calc.subtract(a,b)}")  
  print(f"Product = {calc.multiply(a,b)}")  
  print(f"Divide = {calc.divide(a,b):.2f}")  

main()  
