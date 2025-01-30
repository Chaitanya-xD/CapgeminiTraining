def fib(n):
  if( n == 0 ):
    return 0
  
  if( n == 1 ):
    return 1
  
  return fib(n-2) + fib(n-1)

def main():
  n = int( input("Enter the value of n: ") )
  
  for i in range(0,n):
    print(fib(i),end=' ')
  print()

main()