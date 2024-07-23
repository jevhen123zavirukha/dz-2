# Task 3


def apply_and_sum(nums, func):

    """

    :param nums: numbers
    :param func: function
    :return: result
    """

    result = sum(func(x) for x in nums)
    return result
