def main():
    s = 1000
    for a in range(3, (s - 3) // 3 + 1):
        for b in range(a + 1, (s - 1 - a) // 2 + 1):
            c = s - a - b
            if c * c == a * a + b * b:
                r = (a, b, c)
                break

    result = r[0] * r[1] * r[2]
    print(result)


if __name__ == '__main__':
    main()
