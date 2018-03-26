from bisector import Bisector


def main():
    string_size = prompt_for_string_size()
    minimum_population_size = Bisector.find_minimum_population_size(string_size)
    print("Finding minimum population size", end='')
    print("Minimum population size: {}".format(minimum_population_size))


def prompt_for_string_size():
    string_size = 0
    while string_size < 1:
        try:
            string_size = int(input("String size: "))
        except ValueError as e:
            pass
    return string_size


if __name__ == '__main__':
    main()
