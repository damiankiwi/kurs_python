def calculate_ratios(array):
    positive_count = 0
    negative_count = 0
    zero_count = 0

    total_count = len(array)

    for num in array:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    positive_ratio = positive_count / total_count
    negative_ratio = negative_count / total_count
    zero_ratio = zero_count / total_count

    return positive_ratio, negative_ratio, zero_ratio


array_of_integers = [1, -2, 3, 0, -4, 5, 0, -1, 0]

pos_ratio, neg_ratio, zero_ratio = calculate_ratios(array_of_integers)

print("Array of integers:")
print(array_of_integers)
print("\nRatios:")
print(f"Positive ratio: {pos_ratio:.6f}")
print(f"Negative ratio: {neg_ratio:.6f}")
print(f"Zero ratio: {zero_ratio:.6f}")