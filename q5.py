""" question-5 """


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


def selection_sort_by_key(d):
    """sorting dictionary by key"""
    keys = list(d.keys())
    items_sorted = selection_sort(keys)
    sorted_dict = {key: d[key] for key in items_sorted}
    return sorted_dict


def selection_sort_by_value(d):
    """sorting dictionary by value"""
    values = list(d.values())
    values_sorted = selection_sort(values)
    # reversing the dictionary from k,v -> v,k
    rev_dict = [(value, key) for key, value in d.items()]
    reverse_dict = dict(rev_dict)
    # building new dict from reversed dict
    new_dict = {reverse_dict[num]: num for num in values_sorted}
    return new_dict


my_dict = {"c": 3, "a": 1, "b": 2}

sorted_dict_by_value = selection_sort_by_value(my_dict)
print(sorted_dict_by_value)

sorted_dict_by_key = selection_sort_by_key(my_dict)
print(sorted_dict_by_key)
