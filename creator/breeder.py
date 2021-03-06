from random import randint
from typing import Tuple

from .individual import Individual


class Breeder:

    def __init__(self, string_size):
        self._string_size = string_size

    def breed(self, parent1: Individual, parent2: Individual) -> Tuple[Individual, Individual]:
        num = randint(1, 10)
        if num <= 4:
            child1, child2 = parent1, parent2
        else:
            child1, child2 = self._uniform_crossover(parent1, parent2)
        return self._mutate(child1), self._mutate(child2)

    def _uniform_crossover(self, parent1: Individual, parent2: Individual) -> Tuple[Individual, Individual]:
        child1 = Individual('')
        child2 = Individual('')
        for i in range(self._string_size):
            if randint(0, 1):
                child1 += parent1[i]
                child2 += parent2[i]
            else:
                child1 += parent2[i]
                child2 += parent1[i]
        return child1, child2

    def _mutate(self, child: Individual) -> Individual:
        for i in range(self._string_size):
            should_mutate = randint(0, self._string_size)
            if should_mutate == 1:
                mutated_bit = '0' if child[i] == '1' else '1'
                mutated_string = child.binary_string[0:i] + mutated_bit + child.binary_string[i + 1:]
                child = Individual(mutated_string)
        return child
