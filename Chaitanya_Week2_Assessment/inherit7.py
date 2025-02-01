"""
. Create a multi-level class structure with `Person` → `Employee` → `Manager`, where `Manager` has an additional method `approve_leave()`.

"""
class Person:
  def __init__(self, name, age):  # Initializing person's name and age
    self.name = name
    self.age = age

  def display(self):  # Display person's details
    print(f"Name: {self.name}\nAge: {self.age}")

class Employee(Person):
  def __init__(self, name, age, eid):  # Initializing employee with name, age, and ID
    super().__init__(name, age)
    self.eid = eid

  def display(self):  # Display employee details
    super().display()
    print(f"Employee ID: {self.eid}")

class Manager(Employee):
  def __init__(self, name, age, eid, dept):  # Initializing manager with name, age, ID, and department
    super().__init__(name, age, eid)
    self.dept = dept

  def display(self):  # Display manager details
    super().display()
    print(f"Department: {self.dept}")

  def approve_leave(self, name):  # Method to approve leave for an employee
    print(f"Leave approved for {name}")

def main():  # Main function to create and display employee and manager details
  employee = Employee("Bob", 25, "B1E1")
  employee.display()
  print()
  manager = Manager("Alice", 35, "A1E6", "HR")
  manager.display()
  manager.approve_leave("Bob")

main()
