import threading
import time

def single_task():
  print("Task Started")
  time.sleep(2.5)
  print("Task Completed")

def single_task2():
  time.sleep(1)
  print("Task 2 Started")
  time.sleep(0.8)
  print("Task 2 Completed")

thread = threading.Thread(target=single_task)
thread2 = threading.Thread(target=single_task2)
thread.start()
thread2.start()
thread.join()
thread2.join()
print("Main Thread Execution completed")