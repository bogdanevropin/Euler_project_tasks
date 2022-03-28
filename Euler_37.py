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
    for x in range(3, top + 1, 2):
        if num % x == 0:
            cache[num] = False
            return False
    cache[num] = True
    return True

def is_truncatable_prime(n):
    t = str(n)
    while len(t):
        if not is_prime(t):
            return False
        t = t[1:]
    t = str(n)
    while len(t):
        if not is_prime(t):
            return False
        t = t[:-1]
    return True


primes_found = []
num = 11
while len(primes_found) < 11:
    if is_truncatable_prime(num):
        primes_found.append(num)
    num += 1

print(sum(primes_found))