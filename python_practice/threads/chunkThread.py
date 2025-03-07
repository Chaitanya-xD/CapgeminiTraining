import threading
import time

list1 = [range(100000)]
list2 = [range(100000,200000)]
list3 = [range(200000,300000)]
listt = [list1,list2,list3]

def process(Tlist):
  print("calculating Sum")
  print("Sum:",sum(Tlist))
  time.sleep(5)
  print("calculated Sum")

def main():
  threads = []

  for List in listt:
    thread = threading.Thread(target=process,args=List)
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()

main()