""" question-17 """


def magic_number(num):
    """This function check if input_string start wit a.

    Parameters:
        integer

    Returns:
        boolean
    """
    sum1 = 0
    while num > 0:
        sum1 += int(num % 10)
        num = int(num / 10)
    if sum1 >= 10:
        return magic_number(sum1)
    return sum1 == 1


print(magic_number(10))
