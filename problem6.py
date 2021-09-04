import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if len(ints) <= 1:
        return None

    smallest = ints[0]
    largest = ints[0]

    for number in ints:
        # Simply find the smallest
        if smallest > number:
            smallest = number
        # Then find the largest
        if number > largest:
            largest = number

    return smallest, largest


## Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if (None) == get_min_max([]) else "Fail")
print("Pass" if ((None) == get_min_max([1])) else "Fail")
