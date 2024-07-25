# Task 3


def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except Exception as e:
            print(f"An error has occurred: {e}")
    return wrapper

