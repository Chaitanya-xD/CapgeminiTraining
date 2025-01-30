from cust import customers,order_id

def main():
  name = input("Name of the customer: ")
  orders = []

  print("Enter the orders (press 'q' to exit) ")
  orders = customers(name)
  while True:
    order = input("Order: ")
    if( order == 'q' ):
      break
    ordd = order_id()

    orders.add(ordd.id(),order)
  
  print("Name of the customer:",name)
  print("Order ID\tItem")
  for id in orders.orders:
    print(f"{id}\t\t{orders.orders[id]}")

main()