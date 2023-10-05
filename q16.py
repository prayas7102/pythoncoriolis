""" question-16 """


def modify_string(input_str):
    """This function modifies a input_string.

    Parameters:
        input_str (str)

    Returns:
        str: modified input_string
    """
    [first_country, second_country] = input_str
    if len(first_country) == 0 or len(second_country) == 0:
        return "string length should be greater than 1"
    modified_string = (
        first_country[0]
        + second_country[0]
        + first_country[int(len(first_country) / 2)]
        + second_country[int(len(second_country) / 2)]
        + first_country[len(first_country) - 1]
        + second_country[len(second_country) - 1]
    )
    return modified_string


list_country = ["America", "Japan"]
print("Modified string: ", modify_string(list_country))
