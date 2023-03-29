def print_save_user(**user):
    print(user)


def save_user(**user):
    return user


def main():
    print_save_user(id=1, name="Mike", age=22)  # Displays dictionary
    print(save_user(id=1, name="Mike", age=22))  # Creates dictionary
    print(save_user(first="hi", second=7))  # Different dictionary


if __name__ == '__main__':
    main()
