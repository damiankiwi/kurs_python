def find_nested_brackets(s):
    stack = []
    result = ""
    max_length = 0

    for i, char in enumerate(s):
        if char == '[':
            stack.append(i)
        elif char == ']' and stack:
            start = stack.pop()
            length = i - start + 1

            if length > max_length:
                max_length = length
                result = s[start:i + 1]

    return result

input1 = "]][][[]]]"
output1 = find_nested_brackets(input1)

input2 = "]]]]]]]]]]]]]]]]][][][][]]]]]]]]]]][[[][[][[[[[][][][]][[[[[[[[[[[[[[[[[["
output2 = find_nested_brackets(input2)

print(f"Input 1: {input1}")
print(f"Output 1: {output1}")

print(f"Input 2: {input2}")
print(f"Output 2: {output2}")