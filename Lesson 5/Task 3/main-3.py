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


@handle_exceptions
def divide(a, b):
    return a / b


print(f"The result of the division is: {divide(int(input("Enter the dividend: ")), int(input("Enter the divisor: ")))}")
