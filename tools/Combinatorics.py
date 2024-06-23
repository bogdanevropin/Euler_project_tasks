import math


def binomial_coefficient(n, k):
	return math.comb(n, k)


def binomial_coefficient_with_repetition(n, k):
	# Используем формулу C(n + k - 1, k)
	return binomial_coefficient(n + k - 1, k)


def catalan_number(n):
	"""
	Количество правильных скобочных последовательностей длиной 2n
	Количество полных бинарных деревьев с n + 1 листьями
	Количество путей вдоль решетки из точки (0,0) (n, n)
	не пересекающих главную диагональ.
	"""
	return binomial_coefficient(2 * n, n) // (n + 1)


print(binomial_coefficient(10, 2))
