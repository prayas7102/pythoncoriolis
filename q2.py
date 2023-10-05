""" question-2 """


def count_alphabets(input_string):
    """This function counts alphabets in a input_string.

    Parameters:
        input_string (str)

    Returns:
        int: no. of alphabets in a input_string
    """
    num = 0
    for char in input_string:
        if "a" <= char <= "z" or "A" <= char <= "Z":
            num += 1
    return num


INITIAL_STRING = "abcdef2j3j4j5j"
print(f"given string: {INITIAL_STRING}")
NUM_OF_ALPHABETS = count_alphabets(INITIAL_STRING)
print(f"No. of alphabetic characters: {NUM_OF_ALPHABETS}")
