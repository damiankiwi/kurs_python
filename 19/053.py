def product_of_units_digits(numbers):
    result = 1
    for num in numbers:
        last_digit = abs(num) % 10
        result *= last_digit
    return result

input1 = [12, 23]
output1 = product_of_units_digits(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = [12, 23, 43]
output2 = product_of_units_digits(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")

input3 = [113, 234]
output3 = product_of_units_digits(input3)
print(f"\nInput:\n{input3}\nOutput:\n{output3}")

input4 = [1002, 2005]
output4 = product_of_units_digits(input4)
print(f"\nInput:\n{input4}\nOutput:\n{output4}")