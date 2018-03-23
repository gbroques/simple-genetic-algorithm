from random import randint


class Breeder:
    def __init__(self, string_size):
        self._string_size = string_size

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
