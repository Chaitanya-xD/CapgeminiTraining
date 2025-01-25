n = 0
def main():
  while True:
    n = get_input()
    if( n in ['1','2','3','4'] ):
      if n == '1':
        check_bal()
      elif n == '2':
        dep_money()
      elif n == '3':
        with_money()
      else:
        break      
    else:
      print("Enter a valid option(1,2,3,4)")

def get_input():
  n = input( '\nChoose an option:\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit\n' )
  print()
  return n

def check_bal():
  global n
  print("The available balance is",n)

def dep_money():
  global n
  x = int(input("Enter the amout money you want to deposit: "))
  n += x
  print("Deposit Succesful !\nAvailable Balance:",n)

def with_money():
  global n
  x = int(input("Enter the amout money you want to withdraw: "))
  
  if( x > n ):
    print("Insufficient Balance for withdrawl !")
  else:
    n -= x
    print("Withdraw Succesful !\nAvailable Balance:",n)

main()