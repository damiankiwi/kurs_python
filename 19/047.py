def filter_sum_of_digits(numbers):
    def digit_sum(num):
        return sum(int(digit) for digit in str(abs(num)))

    filtered_numbers = [num for num in numbers if digit_sum(num) > 0]
    return filtered_numbers

input1 = [11, -6, -103, -200]
output1 = filter_sum_of_digits(input1)
print(f"Filtered numbers with sum of digits > 0:\n{output1}")

input2 = [1, 7, -4, 4, -9, 2]
output2 = filter_sum_of_digits(input2)
print(f"\nFiltered numbers with sum of digits > 0:\n{output2}")

input3 = [10, -11, -71, -13, 14, -32]
output3 = filter_sum_of_digits(input3)
print(f"\nFiltered numbers with sum of digits > 0:\n{output3}")