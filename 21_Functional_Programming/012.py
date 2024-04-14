def is_palindrome(s):

    s = ''.join(char.lower() for char in s if char.isalnum())

    return s == s[::-1]

print(is_palindrome("madam"))            # True
print(is_palindrome("nurses run"))        # True
print(is_palindrome("A man, a plan, a canal, Panama")) # True
print(is_palindrome("hello"))             # False