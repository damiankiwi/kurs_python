def max_difference(input_list):
    if len(input_list) < 2:
        return 0

    min_element = min(input_list)
    max_element = max(input_list)

    max_diff = max_element - min_element

    return max_diff

input_list = [10, 3, 5, 6, 2, 8]
max_diff = max_difference(input_list)
print(f"The maximum difference between pairs in the list is: {max_diff}")