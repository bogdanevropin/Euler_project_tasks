from Euler.Euler_tools import gen_primes
from itertools import permutations

length = 4
primes = gen_primes()
length_digit_primes = set()

def differences_are_the_same(a):
    if len(a) < 3:
        return True
    s = sorted(a)
    diff = s[1] - s[0]
    if diff == 0:
        return False

    for i in range(2, len(s)):
        new_diff = s[i] - s[i - 1]
        if new_diff != diff:
            return False
    return True

p = next(primes)

while len(str(p)) < length + 1:
    p = next(primes)
    if len(str(p)) == length:
        length_digit_primes.add(p)


for p in length_digit_primes:
    permutations_primes = [p]
    possibles = permutations(str(p), length)
    for possible in possibles:
        q = int(''.join(possible))
        if q == p:
            continue
        if q in length_digit_primes:
            permutations_primes.append(q)

    if len(permutations_primes) >= 3:
        for s in permutations(permutations_primes, 3):
            if differences_are_the_same(s):
                print(s)
                print(''.join(str(i) for i in sorted(s)))



