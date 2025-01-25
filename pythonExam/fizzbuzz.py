def fizz():
  print("Multiples of 3 under 100 are : ")
  for i in range(1,101):
    if( i % 3 == 0 ):
      print(i,end=' ')
  print()
  
def buzz():
  print("Multiples of 5 under 100 are : ")
  for i in range(1,101):
    if( i % 5 == 0 ):
      print(i,end=' ')
  print()

def fizzbuzz():
  print("Multiples of 3 and 5 under 100 are : ")
  for i in range(1,101):
    if( i % 3 == 0 and i % 5 == 0 ):
      print(i,end=' ')
  print()

  
def main():
  x = input("Pick one:\nFizz\nBuzz\nFizzBuzz\n")
  x = x.lower()

  if( x == 'fizz'):
    fizz()
  elif( x == 'buzz' ):
    buzz()
  elif( x == 'fizzbuzz'):
    fizzbuzz()
  else:
    print("Enter valid option!")
main()