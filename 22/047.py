def filter_greater_than(numbers, threshold):
    filtered_numbers = list(filter(lambda x: x > threshold, numbers))

    return filtered_numbers


numbers = [1, 5, 8, 12, 3, 7, 10, 2, 4, 6]
threshold = 5
filtered_numbers = filter_greater_than(numbers, threshold)
print(f"Numbers greater than {threshold}: {filtered_numbers}")