from random import randint
from typing import List, Tuple


class Creator:

    def __init__(self, population_size=10, string_size=5):
        self._population_size = population_size
        self._string_size = string_size
        self._population = self._create_population()

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

    @staticmethod
    def _fitness(binary_string: str) -> int:
        return binary_string.count('1')

    def _select_parents(self) -> Tuple[str, str]:
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
        index = randint(0, self._population_size - 1)
        return self._population[index]

    def _uniform_crossover(self, parent1: str, parent2: str) -> str:
        child = ''
        for i in range(self._string_size):
            if randint(0, 1):
                child += parent1[i]
            else:
                child += parent2[i]
        return child
