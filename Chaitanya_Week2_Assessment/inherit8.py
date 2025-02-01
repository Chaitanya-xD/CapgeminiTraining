"""
Design a system where a base class `Animal` has a method `speak()`, and subclasses `Dog` and `Cat` override it.

"""
class Animal:
  def speak(self):  # Animal speak method
    print("I'm an Animal")

class Dog(Animal):
  def speak(self):  # Dog speak method
    print("Bow Bow")
    
class Cat(Animal):
  def speak(self):  # Cat speak method
    print("Meow Meow")

def main():  # Main function to demonstrate animal sounds
  dog = Dog()
  cat = Cat()

  dog.speak()
  cat.speak()

main()
