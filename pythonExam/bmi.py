def get_input():
  height = float(input("Enter your height(Meters): "))
  weight = float(input("Enter your weight(Kilograms): "))

  return height, weight

def calculate(height, weight):
  return weight / (height * height)

def display(bmi):
  if bmi < 18.5:
    print("Underweight")
  elif 18.5 <= bmi < 25:
    print("Normal weight")
  elif 25 <= bmi < 30:
    print("Overweight")
  else:
    print("Obese")

def main():
  h,w = get_input()
  bmi = calculate(h,w)
  display(bmi)

main()