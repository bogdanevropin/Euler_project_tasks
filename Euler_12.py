"""
<p>The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be $1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55

We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
"""
from tools.Primes import factors_list


# print(factors_list(76576500))


def gen_triangle_num():
	n = 3
	while True:
		n += 1
		yield n * (n + 1) // 2


for num in gen_triangle_num():
	if len(factors_list(num)) > 500:
		print(num)
		break
	print(num)

