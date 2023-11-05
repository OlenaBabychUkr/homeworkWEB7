#Write a decorator that will calculate the execution time of a function.

import time

def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.4f} seconds")
        return result

    return wrapper

@calculate_execution_time
def add(a: int, b: int) -> int:
    return a + b

add(1, 2)
