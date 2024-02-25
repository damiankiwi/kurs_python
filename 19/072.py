def find_indices_sum_to_zero(numbers):
    n = len(numbers)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if numbers[i] + numbers[j] + numbers[k] == 0:
                    return [i, j, k]

    return None

input1 = [12, -7, 3, -89, 14, 4, -78, -1, 2, 7]
output1 = find_indices_sum_to_zero(input1)

input2 = [1, 2, 3, 4, 5, 6, -7]
output2 = find_indices_sum_to_zero(input2)

print(f"Input 1: {input1}")
print(f"Output 1: {output1}")

print(f"Input 2: {input2}")
print(f"Output 2: {output2}")