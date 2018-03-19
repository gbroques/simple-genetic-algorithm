import unittest
from random import seed

from main import create_binary_string


class TestMain(unittest.TestCase):
    def test_create_binary_string(self):
        seed(1)

        expected_binary_string = '00101'
        length = 5
        binary_string = create_binary_string(length)

        self.assertEqual(len(binary_string), length)
        self.assertEqual(binary_string, expected_binary_string)


if __name__ == '__main__':
    unittest.main()
