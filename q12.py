""" question-12 """


def generate_substrings(s, current="", index=0, result=None):
    """
    This function generates all substrings of a given string using recursion.

    Parameters:
        s (str): The original string
        current (str): The current substring being generated
        index (int): The index of the current character being considered
        result (list): List to store the substrings

    Returns:
        list: All substrings of the original string
    """
    if result is None:
        result = []

    n = len(s)

    if index == n:
        result.append(current)
        return result

    generate_substrings(s, current, index + 1, result)
    generate_substrings(s, current + s[index], index + 1, result)

    return result


def solve(input_string):
    """ counts vowels and consonants in a tring and retuens a dict"""
    substrings = generate_substrings(input_string)
    ans = {}
    ans["vowels"] = 0
    ans["consonants"] = 0
    for x in substrings:
        if len(x) == 0:
            continue
        if x[0] in ["a", "e", "i", "o", "u"]:
            ans["vowels"] += 1
        else:
            ans["consonants"] += 1
    return ans


STRING = "abc"
print(solve(STRING))
