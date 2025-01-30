class Cat:
  def sound(self):
    print("Meow")

class Dog:
    print("Dog")

for animal in [ Cat(), Dog() ]:
  animal.sound()

