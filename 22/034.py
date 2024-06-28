def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def sum_of_digits_in_list(numbers):
    return [sum_of_digits(number) for number in numbers]

numbers = [123, 456, 789, 10, 5]
sums = sum_of_digits_in_list(numbers)

print("Original list:", numbers)
print("Sum of digits of each number in the list:", sums)