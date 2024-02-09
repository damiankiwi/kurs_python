def largest_k_numbers(numbers, k):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[:k]

input1 = [1, 2, 3, 4, 5, 5, 3, 6, 2]
k1 = 1
output1 = largest_k_numbers(input1, k1)
print(f"Input: {input1}\nK: {k1}\nOutput: {output1}")

input2 = [1, 2, 3, 4, 5, 5, 3, 6, 2]
k2 = 2
output2 = largest_k_numbers(input2, k2)
print(f"\nInput: {input2}\nK: {k2}\nOutput: {output2}")

input3 = [1, 2, 3, 4, 5, 5, 3, 6, 2]
k3 = 3
output3 = largest_k_numbers(input3, k3)
print(f"\nInput: {input3}\nK: {k3}\nOutput: {output3}")

input4 = [1, 2, 3, 4, 5, 5, 3, 6, 2]
k4 = 4
output4 = largest_k_numbers(input4, k4)
print(f"\nInput: {input4}\nK: {k4}\nOutput: {output4}")

input5 = [1, 2, 3, 4, 5, 5, 3, 6, 2]
k5 = 5
output5 = largest_k_numbers(input5, k5)
print(f"\nInput: {input5}\nK: {k5}\nOutput: {output5}")