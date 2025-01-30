def main():
  x = input("Enter a number: ")
  mapp = convert(x)

  display( mapp )

def convert(text):
  counter = [0]*10

  for _ in text:
    if _.isnumeric(): 
      counter[ int(_) ]+=1

  return counter

def display( arr ):
  for i in range(0,10):
    print(i, arr[i])

main()

