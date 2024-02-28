def reorder_numbers(arr):
    if (arr[0] + arr[-1]) % 2 == 0:
        return sorted(arr)
    else:
        return sorted(arr, reverse=True)

input1 = [3, 7, 4]
output1 = reorder_numbers(input1)

input2 = [2, 7, 4]
output2 = reorder_numbers(input2)

input3 = [1, 5, 6, 7, 4, 2, 8]
output3 = reorder_numbers(input3)

input4 = [1, 5, 6, 7, 4, 2, 9]
output4 = reorder_numbers(input4)

print(f"Input 1: {input1}")
print(f"Output 1: {output1}")

print(f"Input 2: {input2}")
print(f"Output 2: {output2}")

print(f"Input 3: {input3}")
print(f"Output 3: {output3}")

print(f"Input 4: {input4}")
print(f"Output 4: {output4}")