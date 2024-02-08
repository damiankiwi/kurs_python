def product_of_odd_digits(number):
    odd_digits = [int(digit) for digit in str(number) if int(digit) % 2 != 0]
    product = 1 if odd_digits else 0
    for digit in odd_digits:
        product *= digit
    return product

input1 = 123456789
output1 = product_of_odd_digits(input1)
print(f"Input: {input1}\nOutput: {output1}")

input2 = 2468
output2 = product_of_odd_digits(input2)
print(f"\nInput: {input2}\nOutput: {output2}")

input3 = 13579
output3 = product_of_odd_digits(input3)
print(f"\nInput: {input3}\nOutput: {output3}")