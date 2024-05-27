list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

add_three_lists = list(map(lambda x, y, z: x + y + z, list1, list2, list3))

print("Original lists:")
print("list1:", list1)
print("list2:", list2)
print("list3:", list3)
print("Sum of the three lists:")
print(add_three_lists)