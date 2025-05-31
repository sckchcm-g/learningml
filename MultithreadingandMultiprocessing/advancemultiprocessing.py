## multiprocessing example with a pool of workers

from concurrent.futures import ProcessPoolExecutor
import time

def print_number(number):
    # time.sleep(2)
    return f"Number: {number}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
if __name__ == "__main__":
    # Ensure the code runs only when executed directly
    # This is necessary for multiprocessing to work correctly on Windows
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_number, numbers)

    for result in results:
        print(result)

