class Employee:
  def __init__(self, name, salary):
    self._name = name
    self._salary = salary

  @property
  def salary(self):
    return self._salary
  
  @salary.setter
  def salary(self,Salary):
    self._salary = Salary
  
  def allowance(self, allow):
    self._salary += allow

  def deduct(self):
    self._salary = self._salary * 0.95
  

def main():
  emp = Employee('Steve jobs',5000)

  print(f"Initial Salary: {emp.salary}$")
  new_sal = int(input("Enter the new salary: "))
  emp.salary = new_sal
  print(f"New Salary: {emp.salary}$")
  
  emp.deduct()

  print(f"The salary after deduction: {emp.salary}")
  allow = int( input("Enter the allowance amount: ") )
  
  emp.allowance(allow)
  
  print(f"New Salary: {emp.salary}$")
  
  
main()


