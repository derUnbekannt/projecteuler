import math


def is_prime(n):
    # Based on the Sieve of Eratosthenes
    if n == 1:
        return False
    if n < 4:
        # 2 and 3 are prime
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        # 5 and 7 are prime (we have already excluded 4, 6 and 8)
        return True
    if n % 3 == 0:
        return False

    root = math.sqrt(n)
    f = 5

    while f <= root:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6

    return True


def main():
    limit = 10001
    # We know that 2 is prime
    count = 1
    candidate = 1

    while count < limit:
        candidate += 2
        if is_prime(candidate):
            count += 1

    print(candidate)


if __name__ == '__main__':
    main()
