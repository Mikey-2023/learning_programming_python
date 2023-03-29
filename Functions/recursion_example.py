# n is a non-negative integer
# n! = (n)(n-1)(n-2)...(3)(2)(1)
# (n-1)! = (n-1)(n-2)...(3)(2)(1) = n!/n
# 0! = 1 by definition
# n! = (n)(n-1)! IFF n >= 1; else n! = 0! = 1
# ex: 3! = 3(2)!
#     2! = (2)1!
#     1! = (1)0!
#        = 1

def factorial(n):
    """Returns n!, assuming n >= 0"""
    if n >= 1:  # if n is positive
        return n * factorial(n - 1)
    else:  # if n is 0
        return 1


def reverse_string(input_str):
    if input_str == "":
        return ""
    else:
        return (input_str[1:]) + input_str[0]


def main():
    print(factorial(0))
    print(factorial(3))
    print(factorial(15))

    print()

    print(reverse_string("Hello"))
    print(reverse_string("Papillaa"))
    print("This is the reverse of an empty string:", reverse_string(""))


if __name__ == '__main__':
    main()
