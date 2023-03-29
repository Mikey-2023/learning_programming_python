def main():
    website = "http://google.com"
    website2 = "http://wikipedia.com"

    slice_var = slice(7, -4)
    print(website[slice_var])
    print(website2[slice_var])
    print(website[1:])


if __name__ == '__main__':
    main()
