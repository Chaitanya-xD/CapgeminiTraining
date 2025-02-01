"""
Implement a `Student` class with a constructor that initializes `name` and `roll_number`. Write a method to return student details

"""

class Student:
  def __init__(self, name, rno):  # Initializing student name and roll number
    self.name = name.capitalize()
    self.rno = rno
  
  def get_details(self):  # Method to return student details
    return self.name, self.rno

def main():  # Main function to take input and display student details
  name = input("Enter the Name of the student: ")
  rno = input("Enter the Roll Number of the student: ")

  student = Student(name, rno)
  
  details = student.get_details()

  print(f"\nName: {details[0]}")
  print(f"Roll Number: {details[1]}\n")

main()
