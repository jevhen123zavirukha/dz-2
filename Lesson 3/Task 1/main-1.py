# Task 1


def geometric_progression(a, r):

    """

    :param a: first member
    :param r: coefficient
    :yield: one term of a geometric progression.
    """

    current_term = a
    while True:
        yield current_term
        current_term *= r


progression = geometric_progression(int(input("Enter first member: ")), int(input("Enter coefficient: ")))

for _ in range(int(input("Enter range: "))):
    print(next(progression))
