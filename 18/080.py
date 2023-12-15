def first_missing_positive(nums):
    nums_set = set(nums)

    i = 1
    while i in nums_set:
        i += 1

    return i

input1 = [2, 3, 7, 6, 8, -1, -10, 15, 16]
output1 = first_missing_positive(input1)
print(output1)

input2 = [1, 2, 4, -7, 6, 8, 1, -10, 15]
output2 = first_missing_positive(input2)
print(output2)

input3 = [1, 2, 3, 4, 5, 6, 7]
output3 = first_missing_positive(input3)
print(output3)

input4 = [-2, -3, -1, 1, 2, 3]
output4 = first_missing_positive(input4)
print(output4)