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
