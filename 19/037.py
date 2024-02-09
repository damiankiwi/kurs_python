def largest_divisor_less_than_n(n):
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return i
    return 1

input1 = 18
output1 = largest_divisor_less_than_n(input1)
print(f"Input: {input1}\nOutput: {output1}")

input2 = 100
output2 = largest_divisor_less_than_n(input2)
print(f"\nInput: {input2}\nOutput: {output2}")

input3 = 102
output3 = largest_divisor_less_than_n(input3)
print(f"\nInput: {input3}\nOutput: {output3}")

input4 = 500
output4 = largest_divisor_less_than_n(input4)
print(f"\nInput: {input4}\nOutput: {output4}")

input5 = 1000
output5 = largest_divisor_less_than_n(input5)
print(f"\nInput: {input5}\nOutput: {output5}")

input6 = 6500
output6 = largest_divisor_less_than_n(input6)
print(f"\nInput: {input6}\nOutput: {output6}")