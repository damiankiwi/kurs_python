import unittest
import os

def file_exists(directory, filename):
    filepath = os.path.join(directory, filename)
    return os.path.exists(filepath)

class TestFileExists(unittest.TestCase):

    def test_existing_file(self):
        self.assertTrue(file_exists("path/to/directory", "existing_file.txt")) #EDIT

    def test_non_existing_file(self):
        self.assertFalse(file_exists("path/to/directory", "non_existing_file.txt")) #EDIT

if __name__ == '__main__':
    unittest.main()