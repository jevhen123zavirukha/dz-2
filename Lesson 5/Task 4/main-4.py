# Task 4


import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function execution time : {execution_time:.3f} seconds")
        return result
    return wrapper


@measure_time
def some_function():
    time.sleep(2)


some_function()

