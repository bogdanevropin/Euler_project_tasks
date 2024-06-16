"""
The sum of the primes below 10 is 2+3+5+7=17
Find the sum of all the primes below two million.
"""
from tools.Primes import primes_below_n

print(sum(primes_below_n(2*10**6)))
