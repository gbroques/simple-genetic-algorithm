from random import randint
from typing import List

from .selector import Selector


class Creator:

    def __init__(self, population_size=10, string_size=5):
        self._population_size = population_size
        self._string_size = string_size
        self._population = self._create_population()
        self._selector = Selector(self._population)

    def _create_population(self) -> List[str]:
        population = []
        for i in range(self._population_size):
            binary_string = self._create_binary_string(self._string_size)
            population.append(binary_string)
        return population

    @staticmethod
    def _create_binary_string(size: int) -> str:
        binary_string = ''
        for i in range(size):
            binary_string += str(randint(0, 1))
        return binary_string

    def _replace_population(self):
        # Select (N - 2) / 2 pairs of parents
        num_pairs = int((self._population_size - 2) / 2)
        pairs_of_parents = self._select_pairs_of_parents(num_pairs)
        # Breed N - 2 children
        # Replace all but the 2 best parents

    def _select_pairs_of_parents(self, num_pairs):
        return [self._selector.select_parents() for _ in range(num_pairs)]
