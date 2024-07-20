# Task 2


def custom_range(start, stop=None, step=1):
    current = start
    if stop is None:
        stop = start + 1

    while (step > 0 and current < stop) or (step < 0 and current > stop):
        yield current
        current += step
