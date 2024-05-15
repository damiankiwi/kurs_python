list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

filtered_list = list(filter(lambda x: x not in list2, list1))

print("Original list1:")
print(list1)
print("Original list2:")
print(list2)
print("Remove all elements from 'list1' present in 'list2:")
print(filtered_list)