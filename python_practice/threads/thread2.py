import threading
import time 


def odd():
    for i in range(1, 10, 2):
        print(i)

def even():
    for i in range(2, 10, 2):
        print(i)


thread1 = threading.Thread(target=odd)
thread2 = threading.Thread(target=even)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("The main thread's execution is completed")