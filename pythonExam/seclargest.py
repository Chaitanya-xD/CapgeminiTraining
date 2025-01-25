def get_input():
  a = list(map( int, input("Enter the list of numbers: ").split() ))
  return a

def display(a):
  a = sorted(a)

  print( a[len(a)-2] )

def main():
  a = get_input()
  display(a)

main()