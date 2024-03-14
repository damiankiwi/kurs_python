import unittest

def are_lists_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

class TestAreListsEqual(unittest.TestCase):

    def test_equal_lists(self):
        self.assertTrue(are_lists_equal([1, 2, 3], [1, 2, 3]))
        self.assertTrue(are_lists_equal([], []))
        self.assertTrue(are_lists_equal(['a', 'b', 'c'], ['a', 'b', 'c']))

    def test_unequal_lists(self):
        self.assertFalse(are_lists_equal([1, 2, 3], [1, 2, 4]))
        self.assertFalse(are_lists_equal([1, 2, 3], [1, 2]))
        self.assertFalse(are_lists_equal(['a', 'b', 'c'], ['a', 'b', 'd']))

if __name__ == '__main__':
    unittest.main()