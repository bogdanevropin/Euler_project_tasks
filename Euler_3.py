"""
What is the largest prime factor of 600851475143
"""

from tools.Primes import dividers

number = 600851475143

print(dividers(number))
print(max(dividers(number)))
