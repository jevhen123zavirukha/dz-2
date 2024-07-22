# Task 5


def fibonacci_sequence():

    """
    :yield: fibonacci sequence
    """

    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci_gen = fibonacci_sequence()
for _ in range(10):
    print(next(fibonacci_gen))
