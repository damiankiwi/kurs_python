def find_positions(nums, target):
    start = -1
    end = -1

    for i, num in enumerate(nums):
        if num == target:
            if start == -1:
                start = i
            end = i

    return [start, end]

input1 = ([5, 7, 7, 8, 8, 8], 8)
output1 = find_positions(*input1)
print(output1)

input2 = ([1, 3, 6, 9, 13, 14], 4)
output2 = find_positions(*input2)
print(output2)