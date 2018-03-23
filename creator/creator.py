from random import randint
from typing import List


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

    def _uniform_crossover(self, parent1: str, parent2: str) -> str:
        child = ''
        for i in range(self._string_size):
            if randint(0, 1):
                child += parent1[i]
            else:
                child += parent2[i]
        return child

    def _mutate(self, child: str) -> str:
        for i in range(self._string_size):
            should_mutate = randint(0, self._string_size)
            if should_mutate == 1:
                mutated_bit = '0' if child[i] == '1' else '1'
                child = child[0:i] + mutated_bit + child[i + 1:]
        return child
