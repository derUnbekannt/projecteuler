def reverse(n):
    r = 0
    while n > 0:
        r = 10 * r + n % 10
        n //= 10
    return r


def is_palindrome(n):
    return n == reverse(n)


def main():
    """
    Consider the digits of P (let them be x, y and z. P must be at least 6 digits long since the
    palindrome 111111 = 143 * 777) the product of two 3-digit integers.
    Since P (P = a * b) is palindromic:

    P = 100000x + 10000y + 1000z + 100z + 10y + x
    P = 100001x + 10010y + 1100z
    P = 11(9091x + 910y + 100z)

    Since 11 is prime, at least one of the integers a or b must have a factor of 11.
    So if a is not divisible by 11 then we know b must be. Using this information
    we can determine what values of b we check depending on a:
    """
    largest_palindrome = 0
    a = 999

    while a >= 100:
        if a % 11 == 0:
            b = 999
            db = 1
        else:
            # The largest number less than or equal 999 and divisible by 11
            b = 990
            db = 11

        while b >= a:
            n = a * b
            if n <= largest_palindrome:
                break
            if is_palindrome(n):
                largest_palindrome = n
            b -= db
        a -= 1

    print(largest_palindrome)


if __name__ == '__main__':
    main()
