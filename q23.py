""" question-22 """


def solve(input_list):
    """This function return array of square of no. greater than 3

    Parameters:
        array of int

    Returns:
        array of int: square of no. greater than 3
    """

    return list(map(lambda x: x**2, filter(lambda x: x > 3, input_list)))


INITIAL_ARRAY = [1, 2, 3, 4, 5]
print(INITIAL_ARRAY)
print("toatl sum: ", solve(INITIAL_ARRAY))
