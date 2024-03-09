import re

def split_matched_parentheses(input_str):
    matched_parentheses = re.findall(r'\([^()]*\)', input_str)

    return matched_parentheses

input_str1 = "( ()) ((()()())) (()) ()"
output1 = split_matched_parentheses(input_str1)
print(f"Output 1: {output1}")

input_str2 = "() (( ( )() ( )) ) ( ())"
output2 = split_matched_parentheses(input_str2)
print(f"Output 2: {output2}")