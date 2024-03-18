import sys
sys.path.append('C:\\Python\\Python_Damian\\20_python_concepts')

import unittest
from unittest.mock import patch
import database_utils_2

class TestDatabaseQuery(unittest.TestCase):

    @patch('database_utils_2.execute_query')
    def test_query_results(self, mock_execute_query):
        expected_results = [('John', 'Doe'), ('Jane', 'Smith')]
        mock_execute_query.return_value = expected_results
        results = database_utils_2.execute_query()
        self.assertEqual(results, expected_results)

if __name__ == '__main__':
    unittest.main()