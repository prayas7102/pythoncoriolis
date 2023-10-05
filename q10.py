""" question-10 """


def split_and_join_with_hyphen(input_string):
    """This function takes a input string.

    Parameters:
        str: input_string

    Returns:
        str: new string
    """
    output_string = ""
    for char in input_string:
        if char == " ":
            output_string += "-"
        else:
            output_string += char
    return output_string


initial_string = "this is a string"
print("Output:", split_and_join_with_hyphen(initial_string))
