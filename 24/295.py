from collections import Counter

ctr1 = Counter(x=3, y=2, z=10)
ctr2 = Counter(x=1, y=2, z=3)

union_counter = ctr1 + ctr2
print("Union Counter:", union_counter)

intersection_counter = ctr1 & ctr2
print("\nIntersection Counter:", intersection_counter)

difference_counter = ctr1 - ctr2
print("\nDifference Counter:", difference_counter)