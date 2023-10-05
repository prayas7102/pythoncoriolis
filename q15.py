""" question-15 """


def is_palindrome(input_string):
    """This function check if a input_string is palindromic.

    Parameters:
        input_string (str)

    Returns:
        boolean: true/false
    """

    return input_string == input_string[::-1]


INITIAL_STRING = "aba"
print(f"given string: {INITIAL_STRING}")
print(is_palindrome(INITIAL_STRING))
