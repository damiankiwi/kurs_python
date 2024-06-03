import random

def interleave_lists_randomly(list1, list2):
    combined_list = list1 + list2
    random.shuffle(combined_list)
    result = []
    list1_index, list2_index = 0, 0

    def pick_element(element):
        nonlocal list1_index, list2_index
        if element in list1:
            result.append(list1[list1_index])
            list1_index += 1
        else:
            result.append(list2[list2_index])
            list2_index += 1

    list(map(pick_element, combined_list))

    return result

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

interleaved_list = interleave_lists_randomly(list1, list2)

print("Interleaved List:", interleaved_list)