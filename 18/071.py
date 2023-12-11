def reverse_vowels(input_str):
    vowels = set("aeiouAEIOU")
    input_list = list(input_str)
    left, right = 0, len(input_str) - 1

    while left < right:
        while left < right and input_list[left] not in vowels:
            left += 1
        while left < right and input_list[right] not in vowels:
            right -= 1

        input_list[left], input_list[right] = input_list[right], input_list[left]
        left += 1
        right -= 1

    return ''.join(input_list)

input1 = "w3resource"
output1 = reverse_vowels(input1)
print(output1)

input2 = "Python"
output2 = reverse_vowels(input2)
print(output2)

input3 = "Perl"
output3 = reverse_vowels(input3)
print(output3)

input4 = "USA"
output4 = reverse_vowels(input4)
print(output4)