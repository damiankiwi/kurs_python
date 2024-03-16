import unittest
from unittest.mock import patch, MagicMock
import your_module

class TestDatabaseConnection(unittest.TestCase):

    @patch('your_module.connect_to_database')
    def test_successful_connection(self, mock_connect):
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        result = your_module.connect_to_database()

        self.assertEqual(result, mock_connection)

if __name__ == '__main__':
    unittest.main()
