class employee:
  def __init__(self, name):
    self._name = name
  
  @property
  def name(self):
    return self._name 

  @name.setter
  def name(self,Name):
    self._name = Name

def main():
  l1 = employee('Ram')
  l2 = employee('Fam')
  l3 = employee('Pam')

  a = [l1,l2,l3]

  print(a)

  b = [l1.name,l2.name,l3.name]

  print(b)



main() 
