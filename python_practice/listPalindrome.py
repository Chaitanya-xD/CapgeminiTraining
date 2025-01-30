def get_input():
  return input("Enter the string: ")

def isPal(s):
  a = list(s)
  for i in range( (len(a)//2)+1 ):
    if( a[i] != a[-i-1] ):
      return False
  return True

def split_space(s):
  ch = ''
  a = []
  for _ in s:
    if( _.isspace() ):
      if( len(ch) > 0 ):
        a.append(ch)
        ch = ''
    else:
      ch += _
  
  if ( len(ch) > 0 ):
    a.append(ch)

  return a

def main():
  s = get_input()
  ans = 0
  a = split_space(s)

  for word in a:
    if( isPal(word) ):
      ans += 1
  
  print(ans)


main()