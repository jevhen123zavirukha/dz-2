# Task 3


def sum_2(nums, func):

    """

    :param nums: numbers
    :param func: function
    :return: result
    """

    result = sum(func(x) for x in nums)
    return result


if __name__ == "__main__":
    nums = [i for i in range(4)]

    def double(x):
        return x * 2


    total = sum_2(nums, double)
    print(total)
