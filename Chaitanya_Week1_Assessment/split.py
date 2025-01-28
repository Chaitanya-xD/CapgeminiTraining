def get_input():
  amt = int(input('Enter the Total Bill Amount: '))
  ppl = int(input('Enter the number of people: '))
  tip = input('Enter the tip percentage: ')
  tip.replace('%','')
  tip = int(tip)

  return amt, ppl, tip  

def calc_split(amt, ppl, tip):
  amt = amt + ( amt*(tip/100) )
  return amt/ppl


def display_split(amt, ppl, tip):
  split = calc_split(amt, ppl, tip)
  print('The Amount each person has to pay is',round(split,2))

def main():
  amt, ppl, tip = get_input()
  display_split(amt,ppl,tip)
main()