"""
Create a `Product` class with attributes `name`, `price`, and `stock`. Write a method `check_availability(quantity)` that returns whether the requested quantity is available.

"""
class Product:
  def __init__(self, name, price, quantity):  # Initializing product details
    self.name = name
    self.price = price
    self.quantity = quantity
  
  def check_availability(self, quantity):  # Method to check availability and calculate cost
    if quantity > self.quantity:
      return f"Requested Quantity not available!, Available Quantity: {self.quantity}"
    else:
      s = f"Requested Quantity Available, Cost:{self.price*quantity}"
      return s
    
def main():  # Main function to interact with the user
  milk = Product("Milk", 35, 5)
  bread = Product("Bread", 35, 5)
  eggs = Product("Eggs", 35, 5)

  while True:
    prod = input("Choose a product\nMilk\nBread\nEggs\nQuit\nOption: ").lower()

    if prod not in ['eggs','quit','milk','bread']:
      print("Choose a correct option\n")
    else:
      print()
      if prod == 'quit':
        break
      elif prod == 'milk':
        qnt = int(input("Enter the required Quantity: "))
        print(milk.check_availability(qnt))
      elif prod == "eggs":
        qnt = int(input("Enter the required Quantity: "))
        print(eggs.check_availability(qnt))
      else:
        qnt = int(input("Enter the required Quantity: "))
        print(bread.check_availability(qnt))
      print()

main()
