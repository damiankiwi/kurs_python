def find_max_min_indices(lst):
    max_value = max(lst, key=lambda x: x)
    min_value = min(lst, key=lambda x: x)
    max_index = lst.index(max_value)
    min_index = lst.index(min_value)
    return (max_index, max_value), (min_index, min_value)

original_list = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]

max_result, min_result = find_max_min_indices(original_list)

print("Original list:")
print(original_list)
print("Index position and value of the maximum value of the said list:")
print(max_result)
print("Index position and value of the minimum value of the said list:")
print(min_result)