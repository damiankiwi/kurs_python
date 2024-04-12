def count_upper_lower(string):

    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

input_string = 'The quick Brow Fox'
upper_count, lower_count = count_upper_lower(input_string)
print("No. of Upper case characters:", upper_count)
print("No. of Lower case characters:", lower_count)