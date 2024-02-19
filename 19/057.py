def sum_magnitudes_with_sign(nums):
    total = 0
    sign_product = 1

    for num in nums:
        total += abs(num)
        sign_product *= 1 if num >= 0 else -1

    return total * sign_product

input1 = [1, 3, -2]
output1 = sum_magnitudes_with_sign(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = [1, -3, 3]
output2 = sum_magnitudes_with_sign(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")

input3 = [10, 32, 3]
output3 = sum_magnitudes_with_sign(input3)
print(f"\nInput:\n{input3}\nOutput:\n{output3}")

input4 = [-25, -12, -23]
output4 = sum_magnitudes_with_sign(input4)
print(f"\nInput:\n{input4}\nOutput:\n{output4}")