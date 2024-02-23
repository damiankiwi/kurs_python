def shift_characters(input_str, shift):
    shifted_result = ""

    for char in input_str:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
            shifted_result += shifted_char
        else:
            shifted_result += char

    return shifted_result

input_str = "Ascii character table"
shift_value_forward = 1
output_shifted_forward = shift_characters(input_str, shift_value_forward)
print(f"Input:\n{input_str}\nShift = {shift_value_forward}\nOutput:\n{output_shifted_forward}")

shift_value_backward = -1
output_shifted_backward = shift_characters(input_str, shift_value_backward)
print(f"\nInput:\n{input_str}\nShift = {shift_value_backward}\nOutput:\n{output_shifted_backward}")