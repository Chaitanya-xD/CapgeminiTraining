def main():
  a,b,c,d = get_numbers()
  avg = calc_avg(a,b,c,d)
  display_avg(avg)
  #hello  

def get_numbers(): #Function to read 4 numbers
  a = int(input("Enter the first number: "))
  b = int(input("Enter the second number: "))
  c = int(input("Enter the third number: "))
  d = int(input("Enter the fourth number: "))
  return a,b,c,d

def calc_avg(a,b,c,d): #Function to calculate the average of the 4 numbers
  return (sum(a,b,c,d))/4

def sum(a,b,c,d): #Function to calculate the sum of the 4 numbers
  return a+b+c+d

def display_avg(avg): #Function to display the average of the 4 numbers
  print("The average of the four numbers is", avg)

main()