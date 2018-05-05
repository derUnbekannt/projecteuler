def sum_of_multiples(base, maximum):
    p = maximum // base

    return base * p * (p + 1) // 2


def main():
    limit = 1000 - 1
    result = sum_of_multiples(3, limit) + sum_of_multiples(5, limit) - sum_of_multiples(15, limit)
    print(result)


if __name__ == '__main__':
    main()
