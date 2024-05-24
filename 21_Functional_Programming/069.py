from collections import Counter

original_list = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]

count_occurrences = lambda lst: dict(Counter(lst))

occurrences = count_occurrences(original_list)

print("Original list:")
print(original_list)
print("Count the occurrences of the items in the said list:")
print(occurrences)