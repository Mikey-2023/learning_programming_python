def main():
    words = ["Hey", "Hi", "Hello", "Yo"]
    lengths_old = []
    for word in words:
        lengths_old.append(len(word))
    print("Traditional way:", lengths_old)

    lengths_old1 = [len(word) for word in words]
    print("Equivalent result:", lengths_old1)

    lengths_new = list(map(len, words))
    print("Equivalent result with map function:", lengths_new)

    def cubed(x):
        return x ** 3

    numbers = [1, 2, 3, 4, 5]
    numbers_cubed = list(map(cubed, numbers))
    print("This is a list of numbers cubed:", numbers_cubed)

    numbers_cubed_lambda = list(map(lambda x: x ** 3, numbers))
    print("This is preferable if function 'cubed' is not to be used repeatedly:", numbers_cubed_lambda)

    values = (1, 2, 3, 4, 5)
    squared_values = list(map(lambda x: (x, x ** 2), values))  # Return more than one thing; could wrap in tuple()
    # instead if desired
    print("A list of tuples:", squared_values)

    numbers1 = [1, 2, 3, 4, 5]
    numbers2 = [100, 200, 300, 400, 500]
    multiply_lists = list(map(lambda x, y: x * y, numbers1, numbers2))
    print("Here's a way to handle mapping with multiple list objects:", multiply_lists)

    quiet_list = ["hey", "hi", "yo"]
    yell_list = list(map(str.upper, quiet_list))
    print("This is the loud version:", yell_list)


if __name__ == '__main__':
    main()
