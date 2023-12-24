def is_narcissistic_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    narcissistic_sum = sum(int(digit) ** num_digits for digit in num_str)
    return narcissistic_sum == number

# Przykłady użycia
input1 = 153
input2 = 370
input3 = 407
input4 = 409
input5 = 1634
input6 = 8208
input7 = 9474
input8 = 9475

output1 = is_narcissistic_number(input1)
output2 = is_narcissistic_number(input2)
output3 = is_narcissistic_number(input3)
output4 = is_narcissistic_number(input4)
output5 = is_narcissistic_number(input5)
output6 = is_narcissistic_number(input6)
output7 = is_narcissistic_number(input7)
output8 = is_narcissistic_number(input8)

print(f"Sample Input: ({input1})\nSample Output: {output1}")
print(f"Sample Input: ({input2})\nSample Output: {output2}")
print(f"Sample Input: ({input3})\nSample Output: {output3}")
print(f"Sample Input: ({input4})\nSample Output: {output4}")
print(f"Sample Input: ({input5})\nSample Output: {output5}")
print(f"Sample Input: ({input6})\nSample Output: {output6}")
print(f"Sample Input: ({input7})\nSample Output: {output7}")
print(f"Sample Input: ({input8})\nSample Output: {output8}")