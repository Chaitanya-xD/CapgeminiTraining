import random

class customers:
  def __init__(self, name):
    self.orders = {}
    self.customer_name = name

  def add(self, id, item):
    self.orders[id] = [item]

def main():
  name = input("Name of the customer: ")
  orders = []

  print("Enter the orders (press 'q' to exit) ")
  orders = customers(name)
  while True:
    order = input("Order: ")
    id = random.randint(range(10000,100000))
    if( order == 'q' ):
      break
    orders.add(id,order)
  
  print("Name of the customer:",name)
  print("Order ID\tItem")
  for id in orders.orders:
    print(f"{id}\t\t{orders.orders[id]}")

main()