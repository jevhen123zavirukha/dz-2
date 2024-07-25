# Task 5
def log_arguments_results(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"Result: {result}")

        return result
    return wrapper
