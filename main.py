from bisector import Bisector
from loading_indicator import LoadingIndicator


def main():
    string_size = prompt_for_string_size()
    loading_indicator = LoadingIndicator('Finding minimum population size', 1.0)
    loading_indicator.start()
    minimum_population_size = Bisector.find_minimum_population_size(string_size)
    loading_indicator.cancel()
    print('Minimum population size: {}'.format(minimum_population_size))


def prompt_for_string_size() -> int:
    """Get string size from user."""
    string_size = 0
    while string_size < 1:
        try:
            string_size = int(input("String size: "))
        except ValueError:
            pass
    return string_size


if __name__ == '__main__':
    main()
