from random import sample
from typing import List
from typing import Tuple


class Selector:
    def __init__(self, population: List[str]):
        self._population = population

    def select_parents(self) -> Tuple[str, str]:
        first_parent = self._select_parent()
        second_parent = self._select_parent()
        return first_parent, second_parent

    def _select_parent(self) -> str:
        a, b = self._select_two_random_individuals()
        return a if self._fitness(a) >= self._fitness(b) else b

    def _select_two_random_individuals(self) -> Tuple[str, str]:
        first_individual = self._select_random_individual()
        second_individual = self._select_random_individual()
        return first_individual, second_individual

    def _select_random_individual(self) -> str:
        return sample(self._population, 1)[0]

    @staticmethod
    def _fitness(binary_string: str) -> int:
        return binary_string.count('1')
