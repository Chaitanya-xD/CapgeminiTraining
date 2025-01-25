def fact(n):
  ans = 1

  for i in range(1,n+1):
    ans = ans*i
  
  return ans

def get_input():
  n = input('Enter the number: ')
  return n

def validate(n):
  if( not n.isdigit() or  not n.isdigit() or int(n) < 0 ):
    print("Enter a valid positive number!")
    return False
  
  return True

def main():
  n = get_input()
  if validate(n):
    n = int(n)
    print(fact(n))


main()