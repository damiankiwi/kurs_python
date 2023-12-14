def largest_product_of_three(nums):
    nums.sort()

    product1 = nums[-1] * nums[-2] * nums[-3]

    product2 = nums[0] * nums[1] * nums[-1]

    return max(product1, product2)

input1 = [-10, -20, 20, 1]
output1 = largest_product_of_three(input1)
print(output1)

input2 = [-1, -1, 4, 2, 1]
output2 = largest_product_of_three(input2)
print(output2)

input3 = [1, 2, 3, 4, 5, 6]
output3 = largest_product_of_three(input3)
print(output3)