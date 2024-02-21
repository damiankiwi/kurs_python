def find_different_case_key(dictionary):
    for key in dictionary:
        lower_key = key.lower()
        upper_key = key.upper()
        if all(lower_key != other_key.lower() and upper_key != other_key.upper() for other_key in dictionary if other_key != key):
            return key

input1 = {'red': '', 'GREEN': '', 'blue': 'orange'}
output1 = find_different_case_key(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = {'RED': '', 'GREEN': '', 'orange': '#125GD'}
output2 = find_different_case_key(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")