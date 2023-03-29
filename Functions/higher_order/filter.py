def main():
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def only_even(x):
        if x % 2 == 0:
            return x
    evens = list(filter(only_even, values))
    print(evens)

    evens2 = list(filter(lambda x: x % 2 == 0, values))
    print(evens2)

    more_than_five = list(filter(lambda x: x > 5, values))
    print(more_than_five)

    list_strings = ["hey", "hi", "hello", "yo", "what up", "nice to meet ya", "heyyyyy"]
    shorter_list_strings = list(filter(lambda x: len(x) <= 4, list_strings))
    print(shorter_list_strings)

    list_dictionaries = [{'name': 'Mike', 'age': 22},
                         {'name': 'Toddy', 'age': 37},
                         {'name': 'Michelle', 'age': 55}]
    people_thirty_plus = list(filter(lambda x: x.get('age') >= 30, list_dictionaries))
    print(people_thirty_plus)


if __name__ == '__main__':
    main()
