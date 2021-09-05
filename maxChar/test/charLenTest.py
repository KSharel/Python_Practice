import unittest
import io
import unittest.mock
import sys
sys.path.append("../")
from src import charLen

class TestCharLen(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        charLen.printOP(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_values(self):
        self.assert_stdout("google", 'g 2\no 2\ne 1\n')

    def test_null(self):
        self.assert_stdout("", '')

    def test_null(self):
        self.assert_stdout("abbddd", 'd 3\nb 2\na 1\n')

if __name__ == '__main__':
    unittest.main()