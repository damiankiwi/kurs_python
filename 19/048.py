def find_order_violations(nums):
    violations = []
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            violations.extend([i, i + 1])
    return violations

input1 = [1, 2, 3, 0, 4, 5, 6]
output1 = find_order_violations(input1)
print(f"Indices of order violations: {output1}")

input2 = [1, 2, 3, 4, 5, 6]
output2 = find_order_violations(input2)
print(f"\nIndices of order violations: {output2}")

input3 = [1, 2, 3, 4, 6, 5, 7]
output3 = find_order_violations(input3)
print(f"\nIndices of order violations: {output3}")

input4 = [-3, -2, -3, 0, 2, 3, 4]
output4 = find_order_violations(input4)
print(f"\nIndices of order violations: {output4}")