"""
By replacing the 1-st digit of the 2-digit _number *3,
it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3-rd and 4-th digits of 56**3 with the same digit,
with 5-digit _number is the first example having seven primes among
the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently, 56003, being the first member of this family,
is the smallest prime with this property.
Find the smallest prime which,
by replacing part of the _number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
"""
from itertools import permutations
from tools.Primes import is_prime


def replace_a_digits(_number: int, a: int):
	str_number: str = str(_number)
	number_length: int = len(str_number)
	start_filter_list: list = [0] * (number_length - a) + [1] * a
	# list for filter
	filter_lists = set(permutations(start_filter_list))
	
	def replace(f_list: list):
		nonlocal str_number
		current_num = str_number
		new_num = ''
		for p, digit in enumerate(current_num):
			if f_list[p]:
				new_num += '_'
			else:
				new_num += digit
		replaced_list = []
		for dig in range(10):
			replaced_list.append(new_num.replace('_', str(dig)))
		return replaced_list
	
	return list(map(replace, filter_lists))


def check_primes(list_of_replaced_combinations: list, _n: int):
	required_length = len(str(_n))
	best_list: None | list = None
	for _list in list_of_replaced_combinations:
		first_prime = None
		current_primes = []
		for num in _list:
			if required_length == len(str(int(num))) and is_prime(int(num)):
				if first_prime is None:
					first_prime = num
				current_primes.append(num)
		if best_list is None or len(best_list) < len(current_primes):
			best_list = current_primes
	if best_list:
		min_prime = min(best_list)
		amount_of_primes = len(best_list)
	else:
		min_prime = None
		amount_of_primes = 0
	return best_list, min_prime, amount_of_primes


n = 10
primes_family = 0
info = None
while primes_family < 8:
	primes_family = 0
	for i in range(1, len(str(n))):
		info = check_primes(replace_a_digits(n, i), n)
		current_family = info[2]
		if current_family > primes_family:
			primes_family = current_family
			print(n, primes_family, info[0])
	n += 1
print(info)
n = 120300
print(is_prime(121313), is_prime(222323), is_prime(323333), is_prime(929393),
      is_prime(424343), is_prime(525353), is_prime(626363), is_prime(828383))
