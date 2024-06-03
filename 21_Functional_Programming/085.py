def count_same_pairs(list1, list2):
    same_pairs = list(map(lambda x, y: x == y, list1, list2))
    count = sum(same_pairs)
    return count

list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 3, 4, 6]

same_pairs_count = count_same_pairs(list1, list2)

print("List 1:", list1)
print("List 2:", list2)
print("Number of identical pairs:", same_pairs_count)