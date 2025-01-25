def get_input():
  return input("Enter the string: ")

def isPal(s):
  if s == s[::-1]:
    return True
  

  return False



def main():
  print("Enter q to exit\n")
  while True:
    s = get_input()
    if( s == 'q' ):
      break
    if( isPal(s) ):
      print(f"{s} is a palindrome")
    else:
      print(f"{s} is not a palindrome")
    print()
main()