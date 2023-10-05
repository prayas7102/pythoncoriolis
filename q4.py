""" question - 4 """


def modify_string(input_string):
    """This function takes a input_string.

    Parameters:
        input_string (str)

    Returns:
        str: modified input_string
    """
    first_char = input_string[0]
    new_string = first_char
    for char in input_string[1:]:
        if char == first_char:
            new_string += "$"
        else:
            new_string += char
    return new_string


INITIAL_STRING = "restart"
print(f"Given string is: {INITIAL_STRING}")
print(f"Modified string: {modify_string(INITIAL_STRING)}")
