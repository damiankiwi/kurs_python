from collections import defaultdict


def group_similar_items(input_list):
    grouped_items = defaultdict(list)

    for item in input_list:
        grouped_items[item].append(item)

    result = list(grouped_items.values())

    return result


input_list = [1, 2, 2, 3, 1, 4, 4, 4, 5]
grouped_items = group_similar_items(input_list)
print(grouped_items)