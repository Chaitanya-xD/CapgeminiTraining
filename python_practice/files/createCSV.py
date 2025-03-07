import csv

class Employee:
  def __init__(self,name,age,color):
    self.name = name
    self.age = age
    self.color = color

  def intoCSV(self):
    with open("sample2.csv", "a", newline='') as file:
      Writer = csv.writer(file)
      Writer.writerow([self.name,self.age,self.color])


def main():
    with open("sample2.csv", "w", newline='') as file:
      file.write("Name, Age, Color\n")
    
    for i in range(3):
      name, age, color = input("Enter name, age, color:").split()
      obj = Employee(name, age, color)
      obj.intoCSV()
main()
