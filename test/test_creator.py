import unittest
from random import seed

from creator import Creator


class TestCreator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._creator = Creator(population_size=3, string_size=5)

    def test_create_population(self):
        expected_population = ['00101', '11100', '10110']
        length = 3

        seed(1)
        self._creator._create_population(length)

        population = self._creator._population
        self.assertEqual(length, len(population))
        self.assertEqual(expected_population, population)

    def test_create_binary_string(self):
        expected_binary_string = '00101'
        length = 5

        seed(1)
        binary_string = self._creator._create_binary_string(length)

        self.assertEqual(length, len(binary_string))
        self.assertEqual(expected_binary_string, binary_string)

    def test_fitness(self):
        self.assertEqual(3, self._creator._fitness('01101'))
        self.assertEqual(5, self._creator._fitness('11111'))
        self.assertEqual(1, self._creator._fitness('00001'))


if __name__ == '__main__':
    unittest.main()
