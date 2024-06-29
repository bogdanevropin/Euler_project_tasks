"""
It is possible to show that the square root of two can be expressed
as an infinite continued fraction.
sqrt 2 = 1 + 1 / {2+  1  / {2 + 1 / {2+ ...}}}
By expanding this for the first four iterations, we get:
1 +  1/2 = 3/2 = 1.5
1 + 1 / {2 + 1 / 2} = 7/5 = 1.4
1 + 1 / {2 + 1 / {2 + 1 / 2}} = 7/5 = 1.4
1 + 1 / {2 + 1 / {2 + 1 / {2 + 1 / 2}}} = 41/29 = 1.41379
The next three expansions are 99/70, 239/169, and 577/408,
but the eighth expansion, 1393/985, is the first example where the number
of digits in the numerator exceeds the number of digits in the denominator.
In the first one-thousand expansions,
how many fractions contain a numerator with more digits than the denominator?
"""


def evaluate_new_fraction(num, den):
	return den, 2 * den + num


numerator = 1
denominator = 2
amount = 0
for i in range(1000):
	print(numerator + denominator, denominator)
	numerator, denominator = evaluate_new_fraction(numerator,
	                                               denominator)
	# input()
	if len(str(numerator + denominator)) > len(str(denominator)):
		amount += 1
print(amount)
