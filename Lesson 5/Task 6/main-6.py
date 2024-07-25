# Task 6


def limit_calls(max_calls):
    def decorator(func):
        calls = 0

        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < max_calls:
                calls += 1
                return func(*args, **kwargs)
            else:
                print("The maximum number of function calls has been reached.")

        return wrapper
    return decorator
