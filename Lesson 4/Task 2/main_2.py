# Task 2


def fibonacci_memoized():

    """
    :return: fibonacci sequence
    """

    memo = {}

    def fib(n):
        """

        :param n: number n
        :return: fibonacci sequence
        """

        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]

    return fib
