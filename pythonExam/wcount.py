def get_input():
  return input("Enter the statement: ")

def calc_occ(s):
  words = list( s.split() )

  mp = {}

  for word in words:
    if word in mp:
      mp[word] += 1
    else:
      mp[word] = 1
  
  return mp

def print_occ(occ):
  for key in occ:
    print(f"{key} : {occ[key]}")

def main():
  s = get_input()
  occ = calc_occ(s)
  print_occ(occ)

main()