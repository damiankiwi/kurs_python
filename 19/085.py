def increasing_sequence(nums):
    sorted_nums = sorted(nums)
    result = []

    for num in nums:
        result.append(sorted_nums.index(num))

    return result

input1 = [1, 3, 79, 10, 4, 2, 39]
output1 = increasing_sequence(input1)

input2 = [11, 31, 40, 68, 77, 93, 48, 1, 57]
output2 = increasing_sequence(input2)

input3 = [9, -2, 3, 4, -2, 0, 2, -3, 8, -1]
output3 = increasing_sequence(input3)

print(f"Input 1: {input1}")
print(f"Output 1: {output1}")

print(f"Input 2: {input2}")
print(f"Output 2: {output2}")

print(f"Input 3: {input3}")
print(f"Output 3: {output3}")