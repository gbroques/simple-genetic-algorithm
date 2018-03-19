from random import randint


def main():
    binary_string = create_binary_string(5)
    print(binary_string)


def create_binary_string(size):
    binary_string = ''
    for i in range(size):
        binary_string += str(randint(0, 1))
    return binary_string


if __name__ == '__main__':
    main()
