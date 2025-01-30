import math

def isPrime(n):
  if n % 2 == 0 and n != 2 :
    return False
  
  if( n < 2 ):
    return False

  if( n == 2 ):
    return True
  
  
  i = 2 
  while ( i <= int(math.sqrt(n)+1) ):
    if( n % i == 0 ):
      return False
    i += 1

  return True



def main():
  while True:
    a = input('Enter the lower limit: ')
    b = input('Enter the upper limit: ')

    if( a.isdigit() and  b.isdigit() ):
      a = int(a)
      b = int(b)
      if( (a >= 0 and b >= 0) and a < b ):
        break

    print("Enter a valid range!\n")
  
  for i in range( a , b + 1):
    if( isPrime(i) ):
      if( i == 2 ):
        print(i,"is the smallest prime number")
      else:
        print(i)


main()
