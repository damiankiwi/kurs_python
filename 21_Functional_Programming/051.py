original_list = ['Python', 'list', 'exercises', 'practice', 'solution']

length_to_extract = 8

extracted_strings = list(filter(lambda x: len(x) == length_to_extract, original_list))

print("Original list:")
print(original_list)
print("Length of the string to extract:", length_to_extract)
print("After extracting strings of specified length from the said list:")
print(extracted_strings)