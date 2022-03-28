from math import ceil
from numbers import Number

def is_base10pandigital(n):
    base10pandigital = ''.join(str(i) for i in range(1, 10))
    if isinstance(n, Number):
        n = str(n)
    return ''.join(sorted(n)) == base10pandigital


def is_prime(num, cache={2: True}):
    if isinstance(num, str):
        num = int(num)
    if num < 2:
        return False
    if num in cache:
        return cache[num]

    if num % 2 == 0:
        cache[num] = False
        return False

    top = int(ceil(num ** 0.5))
    for y in range(3, top + 1, 2):
        if num % y == 0:
            cache[num] = False
            return False
    cache[num] = True
    return True


def make_base10_pandigital_checker(max):
    pandigital = ''.join(str(i) for i in range(1, int(max) + 1))

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