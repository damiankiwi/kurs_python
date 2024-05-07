original_list = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]

sorted_list = [sorted(sublist, key=lambda x: x.lower()) for sublist in original_list]

print("Original list:")
print(original_list)
print("After sorting each sublist of the said list of lists:")
print(sorted_list)