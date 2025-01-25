def get_num():
  n = int(input('Enter the number for the multiplication table: '))
  return n

def get_range():
  r = int(input("Please enter the range for the multiplication table: "))
  return r

def disp_table(n,r):
  print(f"Multiplication table for {n} :")

  for i in range(1,r+1):
    print(f'{n} x {i} = {n*i}')
  

def main():
  n = get_num()
  r = get_range()  
  disp_table(n,r)

main()