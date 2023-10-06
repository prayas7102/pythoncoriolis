""" question-6 """
# Write a python program to sort a list of tuples by the second value.
# Input: [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]
# Output: [('akash', 5), ('rishav', 10), ('gaurav', 15), ('ram', 20)]


def selection_sort(arr):
    """sorting given array using selection sort"""
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def sort(input_arr):
    """sorting the the (key,value) array by value"""
    # extracting values from input array
    values = [v for k, v in input_arr]
    # sorting the values
    sorted_values = selection_sort(values)
    # converting input arr to dict
    d = dict(input_arr)
    # reversing the dict.items()
    rev_dict = [(value, key) for key, value in d.items()]
    reverse_dict = dict(rev_dict)
    # final ans containing key,value pair sorted
    ans = [(reverse_dict[val], val) for val in sorted_values]
    return ans


print(sort([("rishav", 10), ("akash", 5), ("ram", 20), ("gaurav", 15)]))
