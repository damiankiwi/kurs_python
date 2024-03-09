def custom_sort(input_list):
    sorted_list = sorted(input_list[1::2])
    result = [input_list[i] if i % 2 == 0 else sorted_list.pop(0) for i in range(len(input_list))]
    return result

input_list1 = [2, 5, 6, 3, 1, 4, 34]
output1 = custom_sort(input_list1)
print(f"Output 1: {output1}")

input_list2 = [8, 0, 7, 2, 9, 4, 1, 2, 8, 3]
output2 = custom_sort(input_list2)
print(f"Output 2: {output2}")