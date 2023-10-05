""" question-13 """


def count_all_char_string(input_str):
    """This function count all lowercase, uppercase, digits, and special symbols.

    Parameters:
        input_str (str)

    Returns:
        dictionary: dict()
    """
    ans = {}
    ans["digits"] = 0
    ans["lowercase"] = 0
    ans["uppercase"] = 0
    ans["symbols"] = 0
    for char in input_str:
        if "a" <= char <= "z":
            ans["lowercase"] += 1
        elif "A" <= char <= "Z":
            ans["uppercase"] += 1
        elif "0" <= char <= "9":
            ans["digits"] += 1
        else:
            ans["symbols"] += 1

    return ans


print("Count all character in string: ", count_all_char_string("P@#yn26at^&i5ve"))
