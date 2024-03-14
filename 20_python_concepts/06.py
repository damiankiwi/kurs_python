import unittest

def divide(a, b):
    return a / b

class TestFloatingPointCalculations(unittest.TestCase):

    def test_divide(self):
        self.assertAlmostEqual(divide(1, 3), 0.3333333333333333)
        self.assertAlmostEqual(divide(5, 2), 2.5)
        self.assertAlmostEqual(divide(10, 4), 2.5)

if __name__ == '__main__':
    unittest.main()