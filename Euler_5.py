"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible with no remainder
by all of the numbers from 1 to 20
"""
from tools.Primes import prime_factors_dict
max_v = 20
current_n = 1
current_factors = {}

for n in range(1, max_v + 1):
	required_factors = prime_factors_dict(n)
	for f in required_factors:
		if f not in current_factors:
			current_factors[f] = required_factors[f]
		else:
			if current_factors[f] < required_factors[f]:
				current_factors[f] = required_factors[f]

print(current_factors)
for f in current_factors:
	current_n = current_n * (f ** current_factors[f])

print(current_n)

