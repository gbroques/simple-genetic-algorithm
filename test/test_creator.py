import unittest
from random import seed

from creator import Creator


class TestCreator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        seed(1)
        cls._creator = Creator(population_size=10, string_size=5)
        cls._creator._create_population()

    def test_create_population(self):
        seed(1)
        population_size = 3
        creator = Creator(population_size=population_size, string_size=5)
        expected_population = ['00101', '11100', '10110']

        population = creator._population
        self.assertEqual(population_size, len(population))
        self.assertEqual(expected_population, population)

    def test_create_binary_string(self):
        expected_binary_string = '00101'
        length = 5

        seed(1)
        binary_string = self._creator._create_binary_string(length)

        self.assertEqual(length, len(binary_string))
        self.assertEqual(expected_binary_string, binary_string)

    def test_uniform_crossover(self):
        seed(1)
        expected_child = '10001'
        child = self._creator._uniform_crossover('01011', '10100')
        self.assertEqual(expected_child, child)

    def test_mutate(self):
        seed(1)
        expected_child = '00100'
        child = self._creator._mutate('10100')
        self.assertEqual(expected_child, child)


if __name__ == '__main__':
    unittest.main()
