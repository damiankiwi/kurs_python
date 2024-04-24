array1 = [1, 2, 3, 5, 7, 8, 9, 10]
array2 = [1, 2, 4, 8, 9]

intersection = lambda arr1, arr2: list(filter(lambda x: x in arr1, arr2))

result = intersection(array1, array2)

print("Intersection of the said arrays:", result)