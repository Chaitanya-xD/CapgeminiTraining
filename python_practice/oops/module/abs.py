from abc import ABC, abstractmethod

class Father(ABC):
  @abstractmethod
  def disp(self):
    pass
  def show(self):
    print("Concrete Method")

class Son(Father):
  def disp(self):
    print("This is the implementation of abstract method in the son class ! ! !")

class Daughter(Father):
  def disp(self):
    print("This is the implementation of abstract method in the daughter class ! ! !")

  
def main():
  son = Son()
  daughter = Daughter()
  son.show()
  son.disp()
  daughter.disp()

  # father = Father()
  # father.disp()


main()
