"""
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large:
one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.
<p>Considering natural numbers of the form, a^b,
where a, b < 100, what is the maximum digital sum?
"""


def digit_sum(n: int):
	s = 0
	for d in str(n):
		s += int(d)
	return s


max_digit_sum = 0
for a in range(2, 100):
	for b in range(2, 100):
		ab = a**b
		ds = digit_sum(ab)
		if ds > max_digit_sum:
			print(a, b, max_digit_sum)
			max_digit_sum = ds

print(max_digit_sum)
