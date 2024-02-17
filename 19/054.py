def remove_duplicates(input_list):
    unique_elements = []
    seen_elements = set()

    for element in input_list:
        if element not in seen_elements:
            unique_elements.append(element)
            seen_elements.add(element)

    return unique_elements

input1 = [1, 3, 4, 10, 4, 1, 43]
output1 = remove_duplicates(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = [10, 11, 13, 23, 11, 25, 23, 76, 99]
output2 = remove_duplicates(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")