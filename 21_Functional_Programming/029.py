is_number = lambda s: s.replace('.', '', 1).isdigit()

sample_strings = ["123", "3.14", "-123", "0", "abc", "2e10"]

for string in sample_strings:
    print(is_number(string))

print("Print checking numbers:")
print(is_number("123"))
print(is_number("3.14"))