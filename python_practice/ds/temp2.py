import concurrent.futures
import time

def long_running_task(x):
    time.sleep(3)  # Simulate some work
    return x * 2

with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(long_running_task, 5)  # Submit the task

    print("Doing other things while the task runs...")  # Main program continues

    # Option 1: Blocking until result is available
    # result = future.result()  # This will wait if the task isn't done yet
    # print(f"Result: {result}")

    # Option 2: Checking if done without blocking
    if future.done():
        result = future.result()
        print(f"Result (non-blocking): {result}")
    else:
        print("Result not yet available.")

    # Option 3: Using a callback (more advanced, but preferred for true asynchronicity)
    def my_callback(future):
        result = future.result()
        print(f"Result from callback: {result}")

    future.add_done_callback(my_callback)

    print("Continuing to do other things...") # The main program continues while the callback is executed later

print("Program finished.")