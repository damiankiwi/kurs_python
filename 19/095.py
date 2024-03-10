def generate_palindrome(input_str, length):
    if length < len(input_str):
        return "Length should be greater than or equal to the length of the given string."

    prefix_length = (length - len(input_str)) // 2
    suffix_length = length - len(input_str) - prefix_length

    prefix = input_str[:prefix_length]
    suffix = input_str[::-1][:suffix_length]

    return prefix + input_str + suffix

input_str1 = "madam"
length1 = 7
output1 = generate_palindrome(input_str1, length1)
print(f"Output 1: {output1}")

input_str2 = "madam"
length2 = 6
output2 = generate_palindrome(input_str2, length2)
print(f"Output 2: {output2}")

input_str3 = "madam"
length3 = 5
output3 = generate_palindrome(input_str3, length3)
print(f"Output 3: {output3}")

input_str4 = "madam"
length4 = 3
output4 = generate_palindrome(input_str4, length4)
print(f"Output 4: {output4}")

input_str5 = "madam"
length5 = 2
output5 = generate_palindrome(input_str5, length5)
print(f"Output 5: {output5}")

input_str6 = "madam"
length6 = 1
output6 = generate_palindrome(input_str6, length6)
print(f"Output 6: {output6}")