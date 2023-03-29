def example_func(req_param, opt_param=1):  # Always put optionals at the very end
    return req_param + opt_param


def main():
    print(example_func(5))
    print(example_func(5, 3))


if __name__ == '__main__':
    main()
