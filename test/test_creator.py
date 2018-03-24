import unittest
from random import seed

from creator import Creator
from creator.individual import Individual


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
        expected_population = [Individual('00101'), Individual('11100'), Individual('10110')]

        population = creator._population
        self.assertEqual(population_size, len(population))
        self.assertEqual(expected_population, population)

    def test_create_individual(self):
        seed(1)
        expected_binary_string = Individual('00101')
        length = 5

        binary_string = self._creator._create_individual(length)

        self.assertEqual(length, len(binary_string))
        self.assertEqual(expected_binary_string, binary_string)

    def test_select_pairs_of_parents(self):
        seed(1)
        expected_pairs_of_parents = [(Individual('01111'), Individual('11100')),
                                     (Individual('11100'), Individual('11010')),
                                     (Individual('11001'), Individual('11100'))]
        pairs_of_parents = self._creator._select_pairs_of_parents(3)
        self.assertEqual(expected_pairs_of_parents, pairs_of_parents)

    def test_replace_population(self):
        seed(1)
        expected_new_population = [Individual('01110'), Individual('11100'),
                                   Individual('11100'), Individual('01010'),
                                   Individual('11011'), Individual('01000'),
                                   Individual('00100'), Individual('01111'),
                                   Individual('01011'), Individual('01111')]
        self._creator._replace_population()
        self.assertEqual(expected_new_population, self._creator._population)


if __name__ == '__main__':
    unittest.main()
