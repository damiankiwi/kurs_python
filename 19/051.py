def product_of_units_digits(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(b % 10)
        a, b = b, a + b
    return result

input1 = 10
output1 = product_of_units_digits(input1)
print(f"Input: {input1}\nOutput:\n{output1}")

input2 = 15
output2 = product_of_units_digits(input2)
print(f"\nInput: {input2}\nOutput:\n{output2}")

input3 = 50
output3 = product_of_units_digits(input3)
print(f"\nInput: {input3}\nOutput:\n{output3}")