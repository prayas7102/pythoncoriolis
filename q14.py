""" question-14 """


def decimal_to_octal(decimal_number):
    """This function return octal values

    Parameters:
        integer

    Returns:
        octal values
    """
    if decimal_number == 0:
        return "0"
    octal_digits = []
    while decimal_number:
        octal_digits.append(str(decimal_number % 8))
        decimal_number //= 8
    return "".join(reversed(octal_digits))


def decimal_to_binary(decimal_number):
    """This function return binary values

    Parameters:
        integer

    Returns:
        binary values
    """
    if decimal_number == 0:
        return "0"
    binary_digits = []
    while decimal_number:
        binary_digits.append(str(decimal_number % 2))
        decimal_number //= 2
    return "".join(reversed(binary_digits))


def decimal_to_hexadecimal(decimal_number):
    """This function return hexa-decimal values

    Parameters:
        integer

    Returns:
        hexa-decimal values
    """
    hex_digits = "0123456789abcdef"
    if decimal_number == 0:
        return "0"
    hexadecimal_digits = []
    while decimal_number:
        hexadecimal_digits.append(hex_digits[decimal_number % 16])
        decimal_number //= 16
    return "".join(reversed(hexadecimal_digits))


def solve(input_list):
    """This function return list containing the decimal,
    octal, hexadecimal and binary values separated by decimal.

    Parameters:
        list of input ranges

    Returns:
        list
    """
    ans_array = []
    for num in range(input_list[0], input_list[1] + 1):
        ans = ""
        ans += str(num) + "."
        ans += (
            decimal_to_octal(num)
            + "."
            + decimal_to_hexadecimal(num)
            + "."
            + decimal_to_binary(num)
        )
        ans_array.append(ans)
    return ans_array


print(solve([14, 16]))
