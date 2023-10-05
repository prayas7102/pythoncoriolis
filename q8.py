""" question - 8 """


def second_lowest_marks_students(input_array):
    """This function takes a nested arrays.

    Parameters:
        [[name,marks]...]

    Returns:
        [[str,str]]: [[name,second_lowest_marks]...]
    """
    second_lowest_marks = ""
    lowest_marks = "A"
    # finding second lowest grade in the array
    for grade in [value for [key, value] in input_array]:
        if grade > lowest_marks:
            second_lowest_marks = lowest_marks
            lowest_marks = grade
    return [
        [key, value] for [key, value] in input_array if value is second_lowest_marks
    ]


INITIAL_ARRAY = [
    ["rohan", "A"],
    ["vishal", "C"],
    ["tim", "D"],
    ["Jon", "A"],
    ["Kane", "C"],
]
print(f"Given Array is: {INITIAL_ARRAY}")
print(
    f"Student with second lowest marks: {second_lowest_marks_students(INITIAL_ARRAY)}"
)
