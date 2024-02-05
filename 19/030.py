def find_shortest_list(lists):
    total_characters = lambda lst: sum(len(word) for word in lst)
    return min(lists, key=total_characters)

input1 = [['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
output1 = find_shortest_list(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = [['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]
output2 = find_shortest_list(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")