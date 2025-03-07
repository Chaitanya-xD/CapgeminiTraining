def main():
  with open("sample.csv", "w") as file:
    file.write("Name, Age, Color\n")
    for i in range(2):
      name, age, color = input("Enter name, age, color:").split()
      file.write(f"{name},{age},{color}\n")

main()