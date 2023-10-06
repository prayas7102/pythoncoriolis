""" question-21 """


def check_starts_from_a(input_list):
    """This function check if input_string start wit a.

    Parameters:
        array of str

    Returns:
        boolean array
    """

    return list(filter(lambda x: x[0] == "a", input_list))


INITIAL_ARRAY = ["apple", "banana", "pear", "apricot", "orange"]
print(INITIAL_ARRAY)
print("check_starts_from_a: ", check_starts_from_a(INITIAL_ARRAY))
