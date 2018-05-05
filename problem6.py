def main():
    limit = 100

    total = limit * (limit + 1) // 2
    total_square = limit * (2 * limit + 1) * (limit + 1) // 6

    result = total**2 - total_square
    print(result)


if __name__ == '__main__':
    main()
