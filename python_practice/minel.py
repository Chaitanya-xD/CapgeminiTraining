def get_input():
  n = int( input("Enter the size of the list: "))
  list_a = list( map( int, input(f"Enter {n} integers: ").split() ) )
  return list_a

def minElement(list_a):
  return sorted(list_a)[0]

def maxElement(list_a):
  return sorted(list_a)[-1]

def getMaxMin(list_a):
    small = list_a[0]
    big = list_a[0]
    for i in range(1, len(list_a)):
        if list_a[i] < small:
            small = list_a[i]
        if list_a[i] > big:
            big = list_a[i]
    
    return small,big


def main():
  list_a = get_input()
  mn, mx = getMaxMin(list_a)
  print(f"Maximum element of the list = {mx}")
  print(f"Minimum element of the list = {mn}")


main()