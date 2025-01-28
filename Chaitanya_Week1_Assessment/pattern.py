def disp(n):
  print('Pattern:')

  for i in range(1,n+1):
    for j in range(i):
      print('*',end='')
    print()

def rdisp(n):
  x = input('\nDo you want to view it reverse order, Type Yes to view it: ')

  if( x.lower() == 'yes' ):
    for i in reversed(range(1,n+1)):
      for j in range(i):
        print('*',end='')
      print()

  print()


def main():
  n = int(input('Enter the value of n: '))
  disp(n)
  rdisp(n)

main()