def remove_duplicates(nums):
    nums_set = set(nums)
    unique_nums = list(nums_set)
    unique_nums.sort()
    return len(unique_nums)

input1 = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4]
output1 = remove_duplicates(input1)
print(output1)

input2 = [1, 2, 2, 3, 4, 4]
output2 = remove_duplicates(input2)
print(output2)