def find_h_index(citations):
    citations.sort(reverse=True)
    for i, citation in enumerate(citations, start=1):
        if i > citation:
            return i - 1
    return -1

input1 = [1, 2, 2, 3, 3, 4, 4, 4, 4]
output1 = find_h_index(input1)
print(f"H-index: {output1}")

input2 = [1, 2, 2, 3, 4, 5, 6]
output2 = find_h_index(input2)
print(f"\nH-index: {output2}")

input3 = [3, 1, 4, 17, 5, 17, 2, 1, 41, 32, 2, 5, 5, 5, 5]
output3 = find_h_index(input3)
print(f"\nH-index: {output3}")