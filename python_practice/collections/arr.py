def main():
  # get_input()
  # lists()
  list_sum()

def list_sum():
  n = int( input("Enter the size of the list: "))
  a = list( map( int, input(f"Enter {n} integers: ").split() ) )
  
  print(f"Sum of {n} integers = {sum(a)} ")


def get_input():
  n = int(input("Enter the value of n: "))

  a = []
  for i in range(n):
    print(f"Enter element {i+1}: ",end='')
    a.append(int(input()))

  print(a)

def lists():
  l1 = [] #Declaring and empty list
  print("This is an empty list: ",l1)
  

  l2 = [0,1,2,3] #List declared with values
  print("\nThis is a list with four items: ",l2)
  

  l3 = ['abc',['c','d']] #Nested list
  print("\nThis is a nested list: ",l3)
  

  l4 = list('spam')#Converts a string to a list, where each character of the string is an element
  print("\nList of char's: ",l4)
  

  #Creating a list from a range of integers
  l5 = list(range(2,5))
  print("\nThe elements from the range(2,5) are: ",l5)
  

  #Using square brackets to access an element in the list
  l6 = [1,2,3,4,5] 
  print("\nThird element of the list: ",l6[2])
  
  
  # Accessing element from a nested list using square brackets 
  l7 = [ [1,2], [2,3], [3,4] ] 
  print("\nElement at row 1, column 2 ([1][2]) is: ",l7[1][1])

  # Slicing a list 
  l8 = [1,2,3,4,5,6,7] 
  print("\nSlicing a list from index 2 to 4: ",l8[2:5])

  # Printing the length of the list
  print("\nThe length of the list is l8 is: ",len(l8))

  #Using nested indexing and slicinig together
  l9 = [ 10, [100,200,300,400], 50 ]
  print("Element at l9[1]: ",l9[1])
  print("Element at l9[1][3]: ",l9[1][3])
  print("Element at l9[1][1:3]: ",l9[1][1:3])

main()