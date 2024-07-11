def filter_strings_with_substring(strings, substring):

    return list(filter(lambda s: substring in s, strings))

strings = ["hello", "world", "example", "substring", "python", "programming"]

substring = "sub"

filtered_strings = filter_strings_with_substring(strings, substring)

print("Strings containing the substring '{}':".format(substring))
print(filtered_strings)