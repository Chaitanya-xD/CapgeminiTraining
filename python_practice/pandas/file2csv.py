import pandas as pd

def main():
  data = []
  while True:
    inpp = input("Enter your Name, Age, Gender: ")
    if ( inpp == 'q' ):
      break
    name, age, gender = inpp.split()
    data.append({'Name':name,'Age':age, 'Gender':gender})

  df = pd.DataFrame(data)
  

main()
