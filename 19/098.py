def compute_depth(input_str):
    depth = 0
    depth_list = []

    for char in input_str:
        if char == '(':
            depth += 1
        elif char == ')':
            depth_list.append(depth)
            depth -= 1

    return depth_list

input_str1 = "(()) (()) () ((()()()))"
output1 = compute_depth(input_str1)
print(f"Output 1: {output1}")

input_str2 = "() (()) () () () ()"
output2 = compute_depth(input_str2)
print(f"Output 2: {output2}")

input_str3 = "((((((((()))))))) () (()) ((()()()))"
output3 = compute_depth(input_str3)
print(f"Output 3: {output3}")