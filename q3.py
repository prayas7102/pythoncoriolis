""" question-3 """


def find_three_largest_numbers(nums):
    """
    Find the three largest numbers from a list.

    Parameters:
        nums (list): A list of numbers.

    Returns:
        list: A list containing the three largest numbers.
        If the input list has less than three numbers, it returns an error message.
    """
    if len(nums) < 3:
        return "Input list must have at least three numbers."

    largest_nums = [-(2**31)] * 3  # Initialize with negative infinity

    for num in nums:
        if num > largest_nums[0]:
            largest_nums[2] = largest_nums[1]
            largest_nums[1] = largest_nums[0]
            largest_nums[0] = num
        elif num > largest_nums[1]:
            largest_nums[2] = largest_nums[1]
            largest_nums[1] = num
        elif num > largest_nums[2]:
            largest_nums[2] = num

    return largest_nums


NUMBERS = [23, 5, 8, 14, 63, 12, 45]
RESULT = find_three_largest_numbers(NUMBERS)
print("Input:", NUMBERS)
print("Three largest NUMBERS:", RESULT)
