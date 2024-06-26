"""
https://projecteuler.net/problem=1
If we list all the natural numbers below
10 that are multiples of or
3, 5 we get 3, 5, 6, 9
The sum of these multiples is
Find the sum of all the multiples of 3 or 5
below 1000
"""


max_v = 1000

s = 0
for n in range(1, max_v):
	if n % 3 == 0 or n % 5 == 0:
		s += n
print(s)
