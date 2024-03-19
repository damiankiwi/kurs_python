import unittest
from my_module import parse_and_validate_input


class TestInputValidation(unittest.TestCase):

    def test_valid_input(self):
        input_data = "valid_input"
        result = parse_and_validate_input(input_data)
        self.assertTrue(result)

    def test_invalid_input(self):
        input_data = "invalid_input"
        result = parse_and_validate_input(input_data)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()