import itertools

def max_length_of_same_char_substring(s):
    groups = itertools.groupby(s)

    max_length = max(len(list(group)) for char, group in groups)

    return max_length

input_string = "aaabbcccccddddeee"
print(f"Maximum length of a substring with the same characters in '{input_string}':")
print(max_length_of_same_char_substring(input_string))