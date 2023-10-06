""" question-20 """


def func(x):
    """check if string start with 'a'"""
    return x[0] == "a"


def check_starts_from_a(input_list):
    """This function check if input_string start wit a.

    Parameters:
        array of str

    Returns:
        boolean array
    """

    return list(map(func, input_list))


INITIAL_ARRAY = ["apple", "banana", "pear", "apricot", "orange"]
print(INITIAL_ARRAY)
print("check_starts_from_a: ", check_starts_from_a(INITIAL_ARRAY))
