from math import ceil
from numbers import Number
from tools.Primes import is_prime


def is_base10pandigital(n):
    base10pandigital = ''.join(str(i) for i in range(1, 10))
    if isinstance(n, Number):
        n = str(n)
    return ''.join(sorted(n)) == base10pandigital


def make_base10_pandigital_checker(m):
    pandigital = ''.join(str(i) for i in range(1, int(m) + 1))

    def is_pandigital(n):
        if isinstance(n, Number):
            n = str(n)
        return ''.join(sorted(n)) == pandigital

    return is_pandigital


base10pandigital = make_base10_pandigital_checker(9)

biggest_pandigitals = []
test_max = 9

for x in range(2, test_max):
    is_pandigital = make_base10_pandigital_checker(x)
    m = int(''.join(str(i) for i in range(x, 0, -1)))
    n = m
    print(f"base maximum {m}")

    while n > 1 and (not (is_pandigital(n) and is_prime(n))):
        if n % (int(m / 10.0) + 1) == 0:
            print(n)
        n -= 1
        s = str(n)
        while s.find('0') != -1:
            n -= 1
            s = str(n)
    if n != 1:
        print(f"find {n}")
        biggest_pandigitals.append(n)

print(biggest_pandigitals)