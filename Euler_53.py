"""
There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation, binom 5 3 = 10
In general, binom n r = n!/{r!(n-r)!}, where,
n! = n times (n-1) times ...times 3 times 2 times 1, and 0! = 1
It is not until n = 23, that a value exceeds one-million:binom 23 10 = 1144066
How many, not necessarily distinct, values of binom n r for 1 < n < 100,
are greater than one-million?
"""
from tools.Combinatorics import binomial_coefficient

# binom n k = binom n (n -k)

greater_mil = 0
for n in range(1, 101):
	for k in range(1, n + 1):  # logically to n // 2 + 1, but we count repetitions
		if binomial_coefficient(n, k) > 10**6:
			print(n, k, binomial_coefficient(n, k))
			greater_mil += 1
print(greater_mil)
