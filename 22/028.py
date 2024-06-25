import itertools

def find_max_min_aggregation_pairs(nums):
    pairs = list(itertools.combinations(nums, 2))

    pair_sums = [(pair, sum(pair)) for pair in pairs]

    max_pair = max(pair_sums, key=lambda x: x[1])

    min_pair = min(pair_sums, key=lambda x: x[1])

    return max_pair[0], min_pair[0]

nums = [4, 1, 9, 7, 5, 6]

max_pair, min_pair = find_max_min_aggregation_pairs(nums)
print(f"Original list: {nums}")
print(f"Pair with the maximum sum: {max_pair}")
print(f"Pair with the minimum sum: {min_pair}")