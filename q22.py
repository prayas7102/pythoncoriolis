""" question-22 """
import functools


def sum1(input_list):
    """This function sum of elements in array.

    Parameters:
        array of int

    Returns:
        int: sum of elements
    """

    return functools.reduce(lambda a, b: a + b, input_list)


INITIAL_ARRAY = [2, 4, 7, 3]
print(INITIAL_ARRAY)
print("toatl sum: ", sum1(INITIAL_ARRAY))
