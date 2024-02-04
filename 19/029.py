def find_indices_sum_to_zero(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == 0:
                return [i, j]

input1 = [1, -4, 6, 7, 4]
output1 = find_indices_sum_to_zero(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = [1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
output2 = find_indices_sum_to_zero(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")