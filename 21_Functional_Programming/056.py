extract_nth_element = lambda lst, n: [item[n] for item in lst]

original_list = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
print("Original list:")
print(original_list)

n = 0
print(f"Extract nth element (n = {n}) from the said list of tuples:")
print(extract_nth_element(original_list, n))

n = 2
print(f"Extract nth element (n = {n}) from the said list of tuples:")
print(extract_nth_element(original_list, n))