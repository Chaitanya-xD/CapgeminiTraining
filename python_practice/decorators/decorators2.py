def log_message(func):
  def wrapper(*args, **kwargs):
    result = func(*args,**kwargs)

    path = "decorator_logs.txt"
    f=open(path,"a")
    f.write(result+"\n")
    f.close()
    return result
  return wrapper


@log_message
def aftras():
  return "A String"

@log_message
def aftraswn():
  return "A String\n"

@log_message
def aftrans():
  return "Another String"



def main():
  aftras()
  aftraswn()
  aftrans()

main()