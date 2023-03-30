def fibonacci(number):
    if number >= 3:
        return fibonacci(number-2) + fibonacci(number-1)
    elif number > 0:
        return 1
    else:
        return 0


def main():
    print(fibonacci(5))
    print(fibonacci(-5))
    print(fibonacci(2))
    print(fibonacci(10))


if __name__ == '__main__':
    main()
