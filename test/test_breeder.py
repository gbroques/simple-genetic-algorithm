import unittest
from random import seed

from creator.breeder import Breeder


class TestBreeder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._breeder = Breeder(5)

    def test_uniform_crossover(self):
        seed(1)
        expected_child = '10001'
        child = self._breeder._uniform_crossover('01011', '10100')
        self.assertEqual(expected_child, child)

    def test_mutate(self):
        seed(1)
        expected_child = '00100'
        child = self._breeder._mutate('10100')
        self.assertEqual(expected_child, child)


if __name__ == '__main__':
    unittest.main()
