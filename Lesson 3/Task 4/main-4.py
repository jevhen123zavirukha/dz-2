# Task 4


def cubes(n):
    a = [x ** 3 for x in range(2, n + 1)]
    yield a


cubes2 = cubes(10)
print(next(cubes2))
