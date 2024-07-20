# Task 5


def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
