from math import ceil


def is_prime(num, cache: dict = {2: True}):
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


def gen_primes():
    yield 2
    n = 3
    while True:
        yield n
        n += 2
        while not is_prime(n):
            n += 2


def dividers(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    return ans


def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n /= 2
    for p in range(3, int(n + 1), 2):
        if n % p == 0 and is_prime(p):
            factors.append(p)
    return factors
