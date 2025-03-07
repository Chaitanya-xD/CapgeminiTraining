import threading
import time

def task(lock):
  with lock:
    print(f"{threading.current_thread().name}")
    time.sleep(2)
    print(f"{threading.current_thread().name}")

lock = threading.Lock()

    