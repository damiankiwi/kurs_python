def compress_string(input_string):
    if not input_string:
        return ""

    result = []
    current_char = input_string[0]
    count = 1

    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = char
            count = 1

    result.append(current_char + str(count))

    return ''.join(result)


input_string = "aaabbbbccddddd"
compressed_string = compress_string(input_string)
print(f"Original string: {input_string}")
print(f"Compressed string: {compressed_string}")