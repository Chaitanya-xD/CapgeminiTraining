import string

def get_string():
  return input("Enter the string: ")

def analysis(s):
  v,c,dig,schar = 0,0,0,0
  special_char = string.punctuation

  for ch in s:
    if ch in ['a','e','i','o','u']:
      v += 1
    if ch.isdigit():
      dig += 1 
    if ch in special_char:
      schar += 1
    if ch not in ['a','e','i','o','u'] and ch not in special_char and not ch.isdigit():
      c += 1

  return v,c,dig,schar


def disp_analysis(s):
  v,c,dig,schar = analysis(s)
  print('The number of vowels in the string:',v)
  print('The number of consonants in the string:',c)
  print('The number of digits in the string:',dig)
  print('The number of special characters in the string:',schar)

def disp_rstring(s):
  print('The reversed string is', s[::-1])

def main():
  s = get_string()
  disp_analysis(s)
  disp_rstring(s)

main()