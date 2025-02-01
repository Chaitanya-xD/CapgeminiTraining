"""  
Create a class `Employee` with properties `name`, `id`, and `department`. Instantiate an object and assign values dynamically.

"""

class Employee:
  def __init__(self, name, id, dept):  # Initializing employee details
    self.name = name
    self.id = id
    self.dept = dept


def main():  # Main function
  name = input("Enter the name of the employee: ")  
  id = input("Enter the id of the employee: ")  
  dept = input("Enter the department of the employee: ")  
  emp = Employee(name, id, dept)  # Creating an employee object

  print("Name \t ID \t Department")  
  print(f"{emp.name} \t {emp.id} \t {emp.dept}")  # Displaying employee details

main()  
