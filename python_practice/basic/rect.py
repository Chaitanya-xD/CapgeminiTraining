def display(data):
  print(f"Area of the rectangle is {data}")

def get_input():
  length = int(input("Length: "))
  breadth = int(input("Breadth: "))
  return (length,breadth)

def calc_area(param):
  return param[0] * param[1]

def main():
  display(calc_area(get_input()))

main()