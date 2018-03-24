from typing import List

from .individual import Individual


class FitnessTracker:
    def __init__(self, population: List[Individual]):
        self._population = population
