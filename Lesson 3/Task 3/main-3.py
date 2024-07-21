# Task 3


def prime_generator(limit):

    """
    :param limit: limit(end)
    :yield: prime numbers.
    """

    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num


upper_limit = int(input("Enter end (0 - ∞): "))
prime_gen = prime_generator(upper_limit)

for prime in prime_gen:
    print(prime)
