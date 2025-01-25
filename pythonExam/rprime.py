prime = [True]*((10000)+1)
def calcPrimes(n=10000):
    global prime
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1


def isPrime(n):
    global prime
    return prime[n]

def get_input():
  while True:
    a = input('Enter the lower limit: ')
    b = input('Enter the upper limit: ')

    if( a.isdigit() and  b.isdigit() ):
      a = int(a)
      b = int(b)
      if( (a >= 0 and b >= 0) and a < b ):
        break
    print("Enter a valid range!\n")
  
  return a,b

def display_primes(x,y):
   print('Primes: ',end='' )
   for i in range(x,y):
      if( isPrime(i) ):
         print(i,end=' ')

def main():
    calcPrimes()
    x,y = get_input()
    display_primes(x,y)

main()