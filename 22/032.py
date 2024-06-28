from collections import Counter

def count_frequencies(unordered_list):
    frequency_count = Counter(unordered_list)
    return frequency_count

unordered_list = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
result = count_frequencies(unordered_list)
print("Frequency of elements in the unordered list:")
print(result)