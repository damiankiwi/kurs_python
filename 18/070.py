def longest_common_prefix(strings):
    if not strings:
        return False

    strings.sort()
    first_string, last_string = strings[0], strings[-1]
    common_prefix = []

    for i, char in enumerate(first_string):
        if char == last_string[i]:
            common_prefix.append(char)
        else:
            break

    return ''.join(common_prefix)

input1 = ["abcdefgh", "abcefgh"]
output1 = longest_common_prefix(input1)
print(output1)

input2 = ["w3r", "w3resource"]
output2 = longest_common_prefix(input2)
print(output2)

input3 = ["Python", "PHP", "Perl"]
output3 = longest_common_prefix(input3)
print(output3)

input4 = ["Python", "PHP", "Java"]
output4 = longest_common_prefix(input4)
print(output4)