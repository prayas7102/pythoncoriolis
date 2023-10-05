""" question - 9 """


def swap_case(input_string):
    """This function takes a input string.

    Parameters:
        str: input_string

    Returns:
        str: modified string
    """
    ascii_diff = ord("a") - ord("A")
    index = 0
    new_string = ""
    for char in input_string:
        if "a" <= char <= "z":
            new_string += chr(ord(char) - ascii_diff)
        elif "A" <= char <= "Z":
            new_string += chr(ord(char) + ascii_diff)
        else:
            new_string += char
            index += 1
    return new_string


INITIAL_STRING = "helLo1w2OR#ldg"
print(f"Given string is: {INITIAL_STRING}")
print(f"String with swap case: {swap_case(INITIAL_STRING)}")
