list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

sum_list = list(map(lambda x, y: x + y, list1, list2))
diff_list = list(map(lambda x, y: x - y, list1, list2))

print("Original lists:")
print("List 1:", list1)
print("List 2:", list2)
print("Sum of the two lists:")
print(sum_list)
print("Difference between the two lists:")
print(diff_list)