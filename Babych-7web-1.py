#Write a decorator that will calculate the execution time of a function.

import datetime

def calculate_execution_time(func):
    def wrapper(a,b):
        start_time = datetime.datetime.now()
        func(a,b)
        finish_time = datetime.datetime.now()
        executing_time = finish_time-start_time
        print(executing_time)

    return wrapper

@calculate_execution_time
def add(a: int, b: int) -> int:
    return a + b

add(1, 2)