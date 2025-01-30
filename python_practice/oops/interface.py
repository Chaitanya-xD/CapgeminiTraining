from abc import ABC, abstractmethod

class Iface:
  @abstractmethod
  def impMethod1(self):
    pass
  def impMethod2(self):
    pass

class chil(Iface):
  def impMethod1(self):
    print("Hello")

  def impMethod2(self):
    print("Hello 2")

