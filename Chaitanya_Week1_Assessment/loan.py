def get_details():
  age = int(input("Enter your Age: "))
  salary = int( input("Enter your Salary: ").replace(',','') )
  credit = int(input("Enter your Credit Score: "))

  return age, salary, credit

def validate(age, salary, credit):
  if( age < 21 ):
    return "Age too low!"
  
  elif( salary < 50000 ):
    return "Not enough Salary!"
  
  elif( credit < 750 ):
    return "Low Credit Score! "
  
  return "Eligible for loan!!!"

def main():
  age, salary, credit = get_details()
  print( validate(age, salary, credit) )

main()