"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000
Find the product abc
"""
s = 1000  # a + b + c

for a in range(1, s//2 + 1):  # a is bigger for example
	for b in range(1, s - (s//2 + 1)):  #
		if a**2 + b**2 == (s - a - b) ** 2:
			print(a*b*(s - a - b))

