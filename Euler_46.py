from math import floor
from math import ceil

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

def gen_primes():
    yield 2
    n = 3
    while True:
        yield n
        n += 2
        while not is_prime(n):
            n += 2

primes = gen_primes()
existing_primes = [next(primes)]

def check_Goldbach(n):
    while n > existing_primes[-1]:
        existing_primes.append(next(primes))
    for prime in existing_primes:
        for i in range(1, int(floor((n / 2) ** 0.5) + 1)):
            if prime + (2 * i ** 2) == n:
                return True
    return False

n = 3

while True:
    n += 2
    if not check_Goldbach(n) and not is_prime(n):
        break
print(n)