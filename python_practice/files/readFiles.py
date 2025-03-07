def main():
  "Reading entire File"
  with open("sample.txt","r") as file:
    content = file.read()
    print(content)

  print()
  
  "Reading each line"
  with open("sample.txt","r") as file:
    for line in file:
      print(line.strip())

main()