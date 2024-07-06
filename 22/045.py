def filter_even_numbers(input_list):
    filtered_list = list(filter(lambda x: x % 2 != 0, input_list))
    return filtered_list

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = filter_even_numbers(input_list)
print(f"Filtered list (only odd numbers): {filtered_list}")