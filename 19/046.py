def min_even_value_and_index(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]

    if not even_numbers:
        return []

    min_even_value = min(even_numbers)
    min_even_index = numbers.index(min_even_value)

    return [min_even_value, min_even_index]

input1 = [1, 9, 4, 6, 10, 11, 14, 8]
output1 = min_even_value_and_index(input1)
print(f"Minimum even value and its index of the said array of numbers:\n{output1}")

input2 = [1, 7, 4, 4, 9, 2]
output2 = min_even_value_and_index(input2)
print(f"\nMinimum even value and its index of the said array of numbers:\n{output2}")

input3 = [1, 7, 7, 5, 9]
output3 = min_even_value_and_index(input3)
print(f"\nMinimum even value and its index of the said array of numbers:\n{output3}")