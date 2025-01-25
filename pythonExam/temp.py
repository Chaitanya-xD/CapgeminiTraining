import sys

def celToFar(n):
  return ((n * 9/5) + 32)

def celToKel(n):
  return n + 273.15

def farToCel(n):
  return (n - 32) * 5/9 

def farToKel(n):
  return celToKel(farToCel(n))

def kelToCel(n):
  return n-273.15

def kelToFar(n):
  return celToFar(kelToCel(n))


def get_input():
  u = input('Choose the input unit :\n1. Celsius \n2. Kelvin\n3. Fahrenheit\n')
  if( u not in ['1','2','3']  ):
    print("Enter a valid input !")
    sys.exit()

  n = input('Enter the temperature: ')
  if( not n.isdigit() ):
    print("Enter a valid input !")
    sys.exit()
  
  n = int(n)
  
  op = input('Choose the output unit :\n1. Celsius \n2. Kelvin\n3. Fahrenheit\n')
  if( op not in ['1','2','3']  ):
    print("Enter a valid input !")
    sys.exit()

  return u,n,op


def main():
  u,n,op = get_input()

  if u == op:
    print('The converted temperature is',n)

  elif( u == '1' ):
    if( op == '2' ):
      print("The converted temperature in Kelvin is",celToKel(n))
    elif( op == '3'):
      print("The converted temperature in Fahrenheit is",celToFar(n))

  elif( u == '2'):
    if( op == '1' ):
      print("The converted temperature in Celsius is",kelToCel(n))
    elif( op == '3'):
      print("The converted temperature in Fahrenheit is",kelToFar(n))
  
  else:
    if( op == '1' ):
      print("The converted temperature in Celsius is",farToCel(n))
    elif( op == '2'):
      print("The converted temperature in Kelvin is",farToKel(n))

main()