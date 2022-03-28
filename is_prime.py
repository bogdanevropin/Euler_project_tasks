import math

def is_prime(num):
    limit = math.ceil(math.sqrt(num))
    d = 2
    while d < limit + 1:
        if num % d == 0:
            return False
        d += 1
    return True

