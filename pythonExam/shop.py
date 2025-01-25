shop = {}
tot = 0

def prompt():
  return input("\nChoose an option from below:\n1. Add items\n2. View items\n3. Total\n4. Exit\n")

def add_items():
  item = input("Enter the name of the item: ")
  price = int(input("Enter the price of the item: "))
  global tot
  tot += price
  
  if item in shop:
    shop[item] += price
  else:
    shop[item] = price

def view_items():
  print()
  for key in shop:
    print(f"{key} : ${shop[key]}")
  print()

def total():
  global tot
  print(f"\nThe total price of the items in the cart is ${tot}")
  print()

def main():
  while True:
    n = prompt()
    if( n in ['1','2','3','4'] ):
      if n == '1':
        add_items()
      elif n == '2':
        view_items()
      elif n == '3':
        total()
      elif n == '4':
        break
    else:
      print("Enter a valid option(1,2,3,4)")

main()