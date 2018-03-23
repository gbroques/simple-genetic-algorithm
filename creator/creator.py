from random import randint


class Creator:

    def __init__(self, population_size=10, string_size=5):
        self._population = []
        self._population_size = population_size
        self._string_size = string_size

    def _create_population(self):
        for i in range(self._population_size):
            binary_string = self._create_binary_string(self._string_size)
            self._population.append(binary_string)

    @staticmethod
    def _create_binary_string(size):
        binary_string = ''
        for i in range(size):
            binary_string += str(randint(0, 1))
        return binary_string

    @staticmethod
    def _fitness(binary_string):
        return binary_string.count('1')

    def _select_random_individual(self):
        index = randint(0, self._population_size - 1)
        return self._population[index]

    def _select_two_random_individuals(self):
        first_individual = self._select_random_individual()
        second_individual = self._select_random_individual()
        return first_individual, second_individual
