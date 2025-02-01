"""
Build a `SmartPhone` class inheriting from `MobileDevice`, which in turn inherits from `Electronics`. Demonstrate method overriding and attribute reuse.

"""

class Electronics:
  def __init__(self, brand):  # Initializing brand of electronic device
    self.brand = brand

  def display(self):  # Display details of the electronic device
    print(f"This is a {self.brand} Electronic Device")
    

class MobileDevice(Electronics):
  def __init__(self, brand, type):  # Initializing brand and type of mobile device
    super().__init__(brand)
    self.type = type

  def display(self):  # Display mobile device details
    print(f"This is a {self.brand} {self.type} ")
  

class SmartPhone(MobileDevice):
  def __init__(self, brand, type, model):  # Initializing brand, type, and model for smartphone
    super().__init__(brand, type)
    self.model = model

  def display(self):  # Display smartphone details
    print(f"This is a {self.brand} {self.model} {self.type} ")
  

def main():  # Main function to demonstrate the device hierarchy
  elec = Electronics("L.G")
  elec.display()
  print()
  
  mobDev = MobileDevice("Google", "Mobile Phone")
  mobDev.display()
  print()

  smartPhone = SmartPhone("Samsung", "Mobile Phone", "S25 Ultra")
  smartPhone.display()

main()
