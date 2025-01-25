def get_input():
  subj = []

  for i in range(0,5):
    subj.append( int( input(f"Enter the marks of subject {i+1} out of 100: ") ) )

  return subj

def disp_marks(subj):
  sum = 0 
  for _ in subj:
    sum += _
  
  return sum

def disp_percentage(marks):
  return (marks/500)*100

def disp_grade(percentage):
  match True:
    case _ if percentage >= 90: 
      return "A+"
    case _ if percentage >= 80:
      return "A"
    case _ if percentage >= 70:
      return "B"
    case _ if percentage >= 60:
      return "C"
    case _ if percentage >= 50:
      return "D"
    case _ if percentage >= 35:
      return "E" 
    case _:
      return "F"


def main():
  subj = get_input()
  marks = disp_marks(subj)
  percent = disp_percentage(marks)
  grade = disp_grade(percent)

  print("The total marks are",marks)
  print("The Percentage is: ",percent,"%")
  print("Grade: ",grade)

main()
