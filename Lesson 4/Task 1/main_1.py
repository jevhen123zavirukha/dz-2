# Task 1


def sequence_generator(first_member, n, func):

    """
    Generator function for a number sequence.

    :param first_member: the value of the first member of the sequence.
    :param n: The number of members to generate.
    :param func: A function that defines the law of sequence.
    :yield: Sequence member.
    """

    current_member = first_member
    for _ in range(n):
        yield current_member
        current_member = func(current_member)


def geometric_progression(member):
    return member * 2


first = int(input("Enter the starting number"))
count = int(input())

gen = sequence_generator(first, count, geometric_progression)

for i in gen:
    print(i)
