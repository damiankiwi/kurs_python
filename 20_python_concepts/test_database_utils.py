import sys
import unittest
from unittest.mock import patch, MagicMock

# Dodaj ścieżkę do katalogu zawierającego moduł database_utils
sys.path.append('C:\\Python\\Python_Damian\\20_python_concepts')

import database_utils

class TestDatabaseConnection(unittest.TestCase):

    @patch('database_utils.connect_to_database')
    def test_successful_connection(self, mock_connect):
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        result = database_utils.connect_to_database()

        self.assertEqual(result, mock_connection)

if __name__ == '__main__':
    unittest.main()