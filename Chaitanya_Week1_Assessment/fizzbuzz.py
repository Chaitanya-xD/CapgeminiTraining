def fizz():
  print("fizz",end=' ')
  
def buzz():
  print("buzz",end=' ')

def fizzbuzz():
  print("fizzbuzz",end=' ')
  
  
def main():
  for i in range(1,101):
    if( i % 3 == 0 and i % 5 == 0 ):
      fizzbuzz()
    elif( i % 5 == 0 ):
      buzz()
    elif i % 3 == 0 :
      fizz()
    else:
      print(i,end=" ")
main()