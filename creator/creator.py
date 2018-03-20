from random import randint


class Creator:

    def __init__(self, population_size=10, string_size=5):
        self._population = []
        self._population_size = population_size
        self._string_size = string_size

    def _create_population(self, size):
        for i in range(size):
            binary_string = self._create_binary_string(self._string_size)
            self._population.append(binary_string)

    @staticmethod
    def _create_binary_string(size):
        binary_string = ''
        for i in range(size):
            binary_string += str(randint(0, 1))
        return binary_string
