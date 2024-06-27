"""
By replacing the 1-st digit of the 2-digit number *3,
it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3-rd and 4-th digits of 56**3 with the same digit,
with 5-digit number is the first example having seven primes among
the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently, 56003, being the first member of this family,
is the smallest prime with this property.
Find the smallest prime which,
by replacing part of the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
"""
from itertools import combinations_with_replacement, combinations, permutations, \
	product


def replace_a_digits(number: str, a, ):
	number_length = len(number)
	filter_list = [0] * number_length + [1] * number_length
	# filter_list = [0, 1]
	print(filter_list)
	am = 0
	for i in set(permutations(filter_list)):
		print(i)
		am += 1
	print(am)
	# print(len(permutations(filter_list)))
	possible_removed_digits = range(0, number_length)


replace_a_digits('100', 2)
