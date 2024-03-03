def find_matching_parentheses(s):
    stack = []
    result = []

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                result.extend([stack.pop(), i])
            else:
                result.append(None)

    return result

input1 = "()(()"
output1 = find_matching_parentheses(input1)

input2 = "()()()"
output2 = find_matching_parentheses(input2)

input3 = "((()))"
output3 = find_matching_parentheses(input3)

print(f"Input 1: {input1}")
print(f"Output 1: {output1}")

print(f"Input 2: {input2}")
print(f"Output 2: {output2}")

print(f"Input 3: {input3}")
print(f"Output 3: {output3}")
