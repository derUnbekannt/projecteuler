def main():
    """
    Every third fibonacci number is even:
            *     *        *        *
        1 1 2 3 5 8 13 21 34 55 89 144 ...
    So if, we only write the even numbers:
        2 8 34 144 ...
    They obey the following recursive relation: E(n) = 4*E(n-1) + E(n-2)
    """
    limit = 4000000
    x = 2
    y = 8
    total = x + y
    while total < limit:
        aux = x
        x = y
        y = 4 * y + aux
        total += y
    print(total)


if __name__ == '__main__':
    main()
