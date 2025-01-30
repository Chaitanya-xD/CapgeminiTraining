class bird:
  def  __init__(self):
    print("bird")

  def fly(self):
    return "This bird can fly"

class mammal:
  def  __init__(self):
    print("mammal")
  
  def walk(self):
    return "This mammal can walk"


class bat(bird, mammal):
  def blind(self):
    super()
    super()
    return "Bats are blind !"
  
bat = bat()

# print(bat.fly())
# print(bat.walk())
# print(bat.blind())