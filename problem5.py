import math


def primes(n):
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def main():
    limit = 20
    result = 1

    for prime in primes(limit):
        power = math.floor(math.log(limit) / math.log(prime))
        result *= int(math.pow(prime, power))

    print(result)


if __name__ == '__main__':
    main()
