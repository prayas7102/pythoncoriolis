""" question - 7 """


def average_marks(marks_dict, name):
    """This function takes a dictionary and string.

    Parameters:
        marks_dict(dict) and name (str)

    Returns:
        int: average marks
    """
    avg_marks = 0
    for x in marks_dict[name]:
        avg_marks += x
    return "{:.2f}".format(avg_marks / len(marks_dict[name]))


kv_dict = {"alpha": [20, 30, 40], "beta": [20, 50, 70]}
name = "beta"
print(f"Given data is: {kv_dict}")
print(f"Avg of name: {name} to be calculated")
print(f"Average marks is: : {average_marks(kv_dict, name)}")
