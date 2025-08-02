from collections import Counter

elements = [1, 2, 3, 4, 5, 11, 3, 3, 6, 7, 8, 9, 3, 10, 1]
element_counter = Counter(elements)

print("Most Common Elements:")
for element, count in element_counter.most_common():
    print(f"{element}: {count}")