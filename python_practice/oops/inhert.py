class Student():
  def __init__(self, name):
    self.name = name

class School( Student ):
  def display_school(self):
    print(f"I'm {self.name} from Python School")

class CollegeUG( School ):
  def display_collegeUG(self):
    print(f"I'm {self.name} from Python College UG")

class CollegePG( CollegeUG ):
  def display_collegePG(self):
    print(f"I'm {self.name} from Python College PG")

def main():
  stud = CollegePG( 'OKOKOKOKOK' )

  stud.display_school()
  stud.display_collegeUG()
  stud.display_collegePG()

main()