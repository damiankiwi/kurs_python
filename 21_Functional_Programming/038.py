strings = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

palindromes = list(filter(lambda x: x == x[::-1], strings))

print("List of palindromes:")
print(palindromes)