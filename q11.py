""" question-11 """


def modify_string(input_str, index, char):
    """This function modifies a input_string.

    Parameters:
        input_str (str)

    Returns:
        int: modified input_string
    """
    # Convert the string to a list of characters
    char_list = list(input_str)
    if 0 <= index < len(char_list):
        char_list[index] = char
    # Convert the list of characters back to a string
    modified_string = "".join(char_list)
    return modified_string


print("Modified string: ", modify_string("abcdefghijk", 5, "k"))
