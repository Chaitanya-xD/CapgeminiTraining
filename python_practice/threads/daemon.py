import time
import threading

def daemon_task():
  while True:
    print("Daemon Thread Runnning")
    time.sleep(1)

daemon_thread = threading.Thread(target=daemon_task, daemon=True)
daemon_thread.start()

time.sleep(5)
