def transform_string(input_str):
    result_str = ''
    space_count = 0

    for char in input_str:
        if char == ' ':
            space_count += 1
        else:
            if space_count >= 3:
                result_str += '-'
            elif space_count == 1 or space_count == 2:
                result_str += '_'
            result_str += char
            space_count = 0

    if space_count >= 3:
        result_str += '-'
    elif space_count == 1 or space_count == 2:
        result_str += '_'

    return result_str

input_str1 = "Python-Exercises"
output1 = transform_string(input_str1)
print(f"Output 1: {output1}")

input_str2 = "Python_Exercises"
output2 = transform_string(input_str2)
print(f"Output 2: {output2}")

input_str3 = "-Hello,_world!__This_is-so-easy!-"
output3 = transform_string(input_str3)
print(f"Output 3: {output3}")