def squared(n):
    """This function returns the squared value of the parameter n"""
    return n ** 2


def main():
    """This is a docstring for the main function"""
    print(squared.__doc__)
    print(main.__doc__)
    print("Here's the documentation for the print function:\n", print.__doc__)


if __name__ == '__main__':
    main()
