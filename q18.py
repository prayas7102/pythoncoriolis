""" question-18 """


def absolute_value(input_):
    """This function return weekday of given date

    Parameters:
        tuple of yyyy mm dd

    Returns:
        string: weekday
    """
    if type(input_) in [int, float]:
        if input_ >= 0:
            return input_
        if input_ < 0:
            return -input_
    return "Nope"


print(absolute_value(120))
