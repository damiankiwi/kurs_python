def find_max_min(iterable):
    max_value = max(iterable)
    min_value = min(iterable)
    return max_value, min_value

numbers = [1, 2, 3, 4, 5, -1, 10, 0]

max_value, min_value = find_max_min(numbers)

print("Original iterable:", numbers)
print("Maximum value:", max_value)
print("Minimum value:", min_value)