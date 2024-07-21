# Task 2


def custom_range(start, end=None, step=1):

    """
    :param start: start
    :param end: end
    :param step: step
    :yield: analogue of the generator function range
    """

    current = start
    if end is None:
        end = start + 1

    while (step > 0 and current < end) or (step < 0 and current > end):
        yield current
        current += step


for i in custom_range(int(input("Enter start: ")), int(input("Enter end: ")), int(input("Enter step: "))):
    print(f"{i}")
