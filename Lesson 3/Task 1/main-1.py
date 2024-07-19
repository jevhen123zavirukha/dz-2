
# Task 1


def geometric_progression(a, r):
    current_term = a
    while True:
        yield current_term
        current_term *= r


a = 2
r = 3
progression = geometric_progression(a, r)

for _ in range(5):
    print(next(progression))
