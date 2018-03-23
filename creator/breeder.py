from random import randint
from typing import Tuple


class Breeder:
    def __init__(self, string_size):
        self._string_size = string_size

    def breed(self, parent1: str, parent2: str) -> Tuple[str, str]:
        num = randint(1, 10)
        if num <= 4:
            child1, child2 = parent1, parent2
        else:
            child1 = self._uniform_crossover(parent1, parent2)
            child2 = self._uniform_crossover(parent1, parent2)
        return self._mutate(child1), self._mutate(child2)

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
