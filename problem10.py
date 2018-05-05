import problem7


def main():
    limit = 2000000
    # We know that 2 and 3 are prime
    total = 5
    n = 5

    while n <= limit:
        if problem7.is_prime(n):
            total += n
        n += 2

        if n <= limit and problem7.is_prime(n):
            total += n
        n += 4

    print(total)


if __name__ == '__main__':
    main()
