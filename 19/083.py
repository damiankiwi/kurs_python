def find_unhappy_indices(s):
    unhappy_indices = []
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i + 1] == s[i + 2] or s[i] == s[i + 2]:
            unhappy_indices.extend([i, i + 1])
            break
    return unhappy_indices if unhappy_indices else None

input1 = "Python"
output1 = find_unhappy_indices(input1)

input2 = "Unhappy"
output2 = find_unhappy_indices(input2)

input3 = "Find"
output3 = find_unhappy_indices(input3)

input4 = "Street"
output4 = find_unhappy_indices(input4)

print(f"Input 1: {input1}")
print(f"Output 1: {output1}")

print(f"Input 2: {input2}")
print(f"Output 2: {output2}")

print(f"Input 3: {input3}")
print(f"Output 3: {output3}")

print(f"Input 4: {input4}")
print(f"Output 4: {output4}")