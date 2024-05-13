is_sorted = lambda lst: all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

test_list1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
print("Original list:")
print(test_list1)
print("Is the said list is sorted!")
print(is_sorted(test_list1))

test_list2 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
print("Original list:")
print(test_list2)
print("Is the said list is sorted!")
print(is_sorted(test_list2))