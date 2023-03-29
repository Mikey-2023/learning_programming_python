def main():
    # TODO: Clean this up
    a = [0, 1, 2]
    b = a  # b and a reference the same list object
    print(a,b)
    print(a is b)
    a[0] = 677  # the object that both a and b reference is changed
    print(a,b)
    print(a is b)

    a = [90, 80, 70]  # a now points to a different object
    print(a,b)
    print(a is b)

    x = 7
    y = x
    print(x,y)
    print(y is x)
    x = 8  # x now is a reference for a different object
    print(x,y)


if __name__ == '__main__':
    main()
