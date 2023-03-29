def divisible_three(x):
    if x % 3 == 0:
        return True
    else:
        return False


def divisible_five(x):
    if x % 5 == 0:
        return True
    else:
        return False


def fizz_buzz(num):
    if divisible_three(num) and divisible_five(num):  # This has to be the first check
        return "fizzbuzz"
    if divisible_three(num):
        return "fizz"
    if divisible_five(num):
        return "buzz"
    return num


def main():
    print("15:", fizz_buzz(15))
    print("3:", fizz_buzz(3))
    print("5:", fizz_buzz(5))
    print("11:", fizz_buzz(11))


if __name__ == '__main__':
    main()