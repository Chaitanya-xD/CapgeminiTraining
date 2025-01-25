def get_input():
  return ( input("Enter the year: ") )

def check_year(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  else:
    return False

def main():
  print("Enter q to quit")
  while True:
    n = get_input()
    if( n == 'q' ):
      break
    n = int(n)
    if ( check_year(n) ):
      print("Leap Year")
    else:
      print( "Not a Leap Year")

main()