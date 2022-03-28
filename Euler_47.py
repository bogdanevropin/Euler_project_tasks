from math import ceil
import math
from Euler.Euler_tools import is_prime
from Euler.Euler_tools import prime_factors

consecutive = 4
current = 1
current_consecutives = []

while len(current_consecutives) < consecutive:
    primes = set(prime_factors(current))
    if len(primes) == consecutive:
        current_consecutives.append(current)
    else:
        current_consecutives = []
    current += 1

print(current_consecutives)

