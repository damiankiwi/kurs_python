def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def sort_by_sum_of_digits(numbers):
    return sorted(numbers, key=sum_of_digits)

input1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
output1 = sort_by_sum_of_digits(input1)
print(f"Input: {input1}\nOutput: {output1}")

input2 = [23, 2, 9, 34, 8, 9, 10, 74]
output2 = sort_by_sum_of_digits(input2)
print(f"\nInput: {input2}\nOutput: {output2}")