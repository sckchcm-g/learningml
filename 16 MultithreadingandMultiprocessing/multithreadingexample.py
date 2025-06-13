### Multithreading 
## When to use multithreading 
### I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations)
### Concurrent tasks: When you have multiple tasks that can run concurrently and are not CPU-bound

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Number: {i}")

def print_letters():
    for letter in 'abcde':
        time.sleep(1)
        print(f"Letter: {letter}")

## create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()
t1.start()
t2.start()

## wait for threads to finish
t1.join()
t2.join()

finish_time = time.time() - t
print(f"Time taken without threading: {finish_time}")