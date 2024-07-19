
# Task 1


def geometric_progression(a, r):
    current_term = a
    while True:
        yield current_term
        current_term *= r
