""" question-20 """
# Map: Given a list of string return list of bool, true if string starts from a else false
# Input: [“apple”, “banana”, “pear”, “apricot”, “orange”]
# Output: [True, False, False, True, False]

def func(x):
    return x[0]=='a'

def check_starts_from_a(input_list):
    """This function check if input_string start wit a.

    Parameters:
        array of str

    Returns:
        boolean array
    """
    
    return list(map(func, input_list))

INITIAL_ARRAY= ["apple", "banana", "pear", "apricot", "orange"]
print(INITIAL_ARRAY)
print("check_starts_from_a: ", check_starts_from_a(INITIAL_ARRAY))
