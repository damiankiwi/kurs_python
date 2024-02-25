def rearrange_ascii_order(input_string):
    words = input_string.split()
    result = []

    for word in words:
        sorted_word = ''.join(sorted(word, key=lambda x: ord(x)))
        result.append(sorted_word)

    return ' '.join(result)

input_str = "Ascii character table"
output_str = rearrange_ascii_order(input_str)
print(f"Input: {input_str}")
print(f"Output: {output_str}")