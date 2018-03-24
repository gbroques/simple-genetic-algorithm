import unittest

from creator.fitness_tracker import FitnessTracker
from creator.individual import Individual


class TestFitnessTracker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        population = [Individual('10101'), Individual('11000'), Individual('01111')]
        cls._fitness_tracker = FitnessTracker(population)

    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
