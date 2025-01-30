class DesttructorExample:
  def __init__(self,name):
    self.name = name
    print(f"Object {self.name} is created")

  def __del__(self):
    print(f"Object {self.name} is deleted")

obj = DesttructorExample('Hola')
del obj 