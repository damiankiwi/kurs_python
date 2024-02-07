def sum_numbers_with_more_than_2_digits(numbers, k):
    numbers_with_more_than_2_digits = [num for num in numbers if num >= 10 or num <= -10]
    sum_of_numbers = sum(numbers_with_more_than_2_digits[:k])
    return sum_of_numbers

input1 = [4, 5, 17, 9, 14, 108, -9, 12, 76]
k1 = 4
output1 = sum_numbers_with_more_than_2_digits(input1, k1)
print(f"Input:\n{input1}\nValue of K: {k1}\nOutput: {output1}")

input2 = [4, 5, 17, 9, 14, 108, -9, 12, 76]
k2 = 6
output2 = sum_numbers_with_more_than_2_digits(input2, k2)
print(f"\nInput:\n{input2}\nValue of K: {k2}\nOutput: {output2}")

input3 = [114, 215, -117, 119, 14, 108, -9, 12, 76]
k3 = 5
output3 = sum_numbers_with_more_than_2_digits(input3, k3)
print(f"\nInput:\n{input3}\nValue of K: {k3}\nOutput: {output3}")

input4 = [114, 215, -117, 119, 14, 108, -9, 12, 76]
k4 = 1
output4 = sum_numbers_with_more_than_2_digits(input4, k4)
print(f"\nInput:\n{input4}\nValue of K: {k4}\nOutput: {output4}")