def are_isomorphic(str1, str2):
    if len(str1) != len(str2):
        return False

    mapping = {}
    seen = set()

    for char1, char2 in zip(str1, str2):
        if char1 not in mapping:
            if char2 in seen:
                return False
            mapping[char1] = char2
            seen.add(char2)
        else:
            if mapping[char1] != char2:
                return False

    return True

input1 = ("foo", "bar")
output1 = are_isomorphic(*input1)
print(output1)

input2 = ("bar", "foo")
output2 = are_isomorphic(*input2)
print(output2)

input3 = ("paper", "title")
output3 = are_isomorphic(*input3)
print(output3)

input4 = ("title", "paper")
output4 = are_isomorphic(*input4)
print(output4)

input5 = ("apple", "orange")
output5 = are_isomorphic(*input5)
print(output5)

input6 = ("aa", "ab")
output6 = are_isomorphic(*input6)
print(output6)

input7 = ("ab", "aa")
output7 = are_isomorphic(*input7)
print(output7)