from abc import ABC, abstractmethod
from typing import List

class Employee(ABC):
    @abstractmethod
    def work(self) -> str:
        pass
    
    @abstractmethod
    def get_salary(self) -> float:
        pass
    
    

class Manager(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.role = "Manager"

    def work(self) -> str:
        return f"{self.name} is managing the team."

    def get_salary(self) -> float:
        return self.salary

    def __del__(self):
        pass

class Developer(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.role = "Developer"

    def work(self) -> str:
        return f"{self.name} is writing code."

    def get_salary(self) -> float:
        return self.salary

    def __del__(self):
        pass

class Intern(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.role = "Intern"

    def work(self) -> str:
        return f"{self.name} is learning and assisting."

    def get_salary(self) -> float:
        return self.salary

    def __del__(self):
        print('',end='')

class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []

    def promote(self, employee):
        if( employee.role == "Intern"):
            prom = Developer(employee.name,employee.salary)
            self.employees.remove(employee)
            del employee
            self.employees.append(prom)

        elif( employee.role == "Developer"):
            prom = Manager(employee.name,employee.salary)
            self.employees.remove(employee)
            del employee
            self.employees.append(prom)
            

    def hire(self, employee: Employee) -> None:
        self.employees.append(employee)
        print(f"{employee.name} has been hired.")

    def fire(self, employee: Employee) -> None:
        self.employees.remove(employee)
        print(f"{employee.name} has been fired.")

    def get_total_salary(self) -> float:
        return sum(employee.get_salary() for employee in self.employees)

    def show_employee_details(self) -> None:
        print(f"Employees in {self.name} Department:")
        for employee in self.employees:
            print(f"- {employee.name}, Salary: {employee.get_salary()}, Role: {employee.work()}")

class Security(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.role = "Security"

    def work(self) -> str:
        return f"{self.name} is Securing the assets."

    def get_salary(self) -> float:
        return self.salary
    
    def __del__(self):
        pass
    
    

manager = Manager("Alice", 80000)
developer = Developer("Bob", 60000)
intern = Intern("Charlie", 20000)
securitystaff=Security("Ram",5000)

it_department = Department("IT")

it_department.hire(manager)
it_department.hire(developer)
it_department.hire(intern)
it_department.hire(securitystaff)

it_department.show_employee_details()

total_salary = it_department.get_total_salary()
print(f"Total salary expense for {it_department.name} department: ${total_salary}")

it_department.promote(intern)
it_department.promote(developer)
it_department.show_employee_details()