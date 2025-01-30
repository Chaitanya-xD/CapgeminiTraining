import dis

def main():
  # a,b,c = get_numbers()
  # mx = calc_max(a,b,c)
  # display_max(mx)
  # dis.dis(get_numbers)
  # dis.dis(calc_max)
  # dis.dis(display_max)
  dis.dis(FOR)

def get_numbers(): #Function to read 3 numbers
  a = int(input("Enter the first number: "))
  b = int(input("Enter the second number: "))
  c = int(input("Enter the third number: "))
  
  return a,b,c

def calc_max(a,b,c): #Function to calculate the max of the 3 numbers
  return max( max(a,b),max(b,c) )

def max(a,b): #Function to calculate the sum of the 4 numbers
  return a if ( a > b ) else  b

def display_max(mx): #Function to display the average of the 4 numbers
  print("The max of the three numbers is", mx)

def FOR():
  x = 1 
  y = 2
  z = x*y
  a = x+y

  for i in range(5):
    x += 1
    
  print(z)

main()