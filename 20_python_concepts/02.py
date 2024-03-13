import unittest

def is_sorted_ascending(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

class TestIsSortedAscending(unittest.TestCase):

    def test_sorted_list(self):
        self.assertTrue(is_sorted_ascending([1, 2, 3, 4, 5]))
        self.assertTrue(is_sorted_ascending([-3, -2, 0, 1, 5]))

    def test_unsorted_list(self):
        self.assertFalse(is_sorted_ascending([5, 3, 2, 8, 1]))
        self.assertFalse(is_sorted_ascending([5, 5, 3, 2, 1]))

    def test_empty_list(self):
        self.assertTrue(is_sorted_ascending([]))

if __name__ == '__main__':
    unittest.main()