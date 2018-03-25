from creator import Creator


def main():
    creator = Creator()
    population = creator.create_population()
    print("Initial fitness: " + str(creator.get_average_fitness(population)))
    evolved_population = creator.evolve_population(population)
    print("Final fitness: " + str(creator.get_average_fitness(evolved_population)))


if __name__ == '__main__':
    main()
