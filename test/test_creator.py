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

    def test_fitness(self):
        self.assertEqual(3, self._creator._fitness('01101'))
        self.assertEqual(5, self._creator._fitness('11111'))
        self.assertEqual(1, self._creator._fitness('00001'))

    def test_select_random_individual(self):
        seed(1)
        random_individual = self._creator._select_random_individual()
        self.assertEqual('10110', random_individual)

    def test_select_two_random_individuals(self):
        seed(1)
        first, second = self._creator._select_two_random_individuals()
        self.assertEqual('10110', first)
        self.assertEqual('01111', second)

    def test_select_parent(self):
        seed(1)
        expected_parent = '01111'
        parent = self._creator._select_parent()
        self.assertEqual(expected_parent, parent)

    def test_select_parents(self):
        seed(1)
        first_parent, second_parent = self._creator._select_parents()
        expected_first_parent = '01111'
        expected_second_parent = '11100'
        self.assertEqual(expected_first_parent, first_parent)
        self.assertEqual(expected_second_parent, second_parent)


if __name__ == '__main__':
    unittest.main()
