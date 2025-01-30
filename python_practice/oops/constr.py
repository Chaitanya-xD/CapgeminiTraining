class Example:
  def __init__(self, name):
    print(f"First Constructor: Hello {name}")

  def __init__(self, age):
    print(f"First Constructor: Age is {age}")


class Example2:
  def __init__(self, studentName, **kwargs):
    self.studentName = studentName

    if 'name' in kwargs and 'age' in kwargs:
      print(f'Your name is {kwargs["name"]}, Your age is {kwargs["age"]}')
    elif 'name' in kwargs:
      print(f'Your name is {kwargs["name"]}.') 
    else:
      print(f'Nameless wonder')


obj = Example(25)

obj2 = Example2('One',name ='Two',age=90)
obj2 = Example2('One',name ='Three')
obj2 = Example2('One')


