def print_numbers(*nums):
    print(nums)  # nums is a tuple of the arguments when called


def print_numbers2(*nums):
    for n in nums:
        print(n)


def multiply_numbers(*nums):
    total = 1  # Start with identity element for whatever operation you use
    for n in nums:
        total *= n
    return total


def main():
    print_numbers(1, 2, 3, 4)
    print_numbers2(1, 2, 3, 4)
    print(multiply_numbers(1, 2, 3, 4))


if __name__ == '__main__':
    main()
