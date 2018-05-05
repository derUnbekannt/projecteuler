def largest_prime_factor(number):
    n = number
    last_factor = 1

    while n % 2 == 0:
        n //= 2
        last_factor = 2

    factor = 3

    while factor * factor <= n:
        while n % factor == 0:
            last_factor = factor
            n //= factor
        factor += 2

    if n == 1:
        return last_factor

    return n


def main():
    result = largest_prime_factor(600851475143)
    print(result)


if __name__ == '__main__':
    main()
