def remove_and_count(nums, value):
    nums = [num for num in nums if num != value]
    return len(nums)

input1 = ([1, 2, 3, 4, 5, 6, 7, 5], 5)
output1 = remove_and_count(*input1)
print(output1)

input2 = ([10, 10, 10, 10, 10], 10)
output2 = remove_and_count(*input2)
print(output2)

input3 = ([10, 10, 10, 10, 10], 20)
output3 = remove_and_count(*input3)
print(output3)

input4 = ([], 1)
output4 = remove_and_count(*input4)
print(output4)