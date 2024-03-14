import unittest

def is_palindrome(s):
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
    return s == s[::-1]

class TestIsPalindrome(unittest.TestCase):

    def test_palindrome_strings(self):
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))

    def test_non_palindrome_strings(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("Palindrome"))

if __name__ == '__main__':
    unittest.main()