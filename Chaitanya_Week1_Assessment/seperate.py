def get_input():
  a = list(map( int, input("Enter the list of numbers: ").split() ))
  return a

def seperate(a):
  odd= []
  even = []

  for i in a:
    odd.append(i) if ( i % 2 == 1 ) else even.append(i)
  
  return odd,even

def p_lists(odd,even):
  print("Odd List:")
  for el in odd:
    print(el,end=' ')
  print()
  print("Even List:")
  for el in even:
    print(el,end=' ')


def main():
  a = get_input()
  odd,even = seperate(a)
  p_lists(odd,even)

main()