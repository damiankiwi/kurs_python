original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nested_list = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

intersection = list(filter(lambda x: any(item in x for item in original_list), nested_list))

print("Original lists:")
print(original_list)
print(nested_list)
print("Intersection of said nested lists:")
print(intersection)