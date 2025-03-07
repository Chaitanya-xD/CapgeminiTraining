import time
import functools

def log_execution(func):

  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()

    print(f"Function Name:{func.__name__} called with arguments:{args},{kwargs}")
    print(f"Execution Time: {end_time - start_time:.4f} seconds")
    return result
  
  return wrapper

@log_execution
def add_numbers(a, b):
  time.sleep(1)
  return a + b

@log_execution
def product(a,b):
  time.sleep(1)
  return a * b

result = add_numbers(5,10)
print("Result:",result)
productresult = product(4,5)
print("Product Result: ",productresult)

