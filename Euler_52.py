"""
It can be seen that the number, 125874, and its double,
251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""


def make_sequence(x: int):
	return [i*x for i in range(1, 7)]


def check_digits(list_x: list):
	return len(tuple(set([str(sorted(str(v))) for v in list_x]))) - 1


print(check_digits(make_sequence(125874)))
input()
for num in range(10, 10**11+1):
	digits_amount = check_digits(make_sequence(num))
	print(num, digits_amount)
	if not digits_amount:
		break
