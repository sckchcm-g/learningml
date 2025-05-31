## Processes that runs in parallel
### CPU-bound tasks that are heavy on CPU usage (e.g., calculations, data processing)
## Parallel execution - multiple cores of the cpu

import multiprocessing

import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square {i * i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube {i * i * i}")

if __name__ == "__main__":
    ## create 2 processes

    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    # start the processes
    t = time.time()
    p1.start()
    p2.start()

    # wait for the processes to finish
    p1.join()
    p2.join()
    print(f"Time taken: {time.time() - t} seconds")

    # Note: The above code will run the square_numbers and cube_numbers functions in parallel.
    # Each function will run in its own process, allowing them to execute simultaneously.
    # This is useful for CPU-bound tasks where you want to take advantage of multiple CPU cores.
