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
  nums = []

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
      nums.append(i)  
  
  print(f"The prime numbers between the range {a} and {b} are:",*(nums))
  print(f"The smallest prime number is:",nums[0])
  print(f"The largest prime number is:",nums[-1])

main()

