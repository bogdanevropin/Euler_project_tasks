from Euler_prime_tools import is_prime, gen_primes
from copy import deepcopy

prime_chain = []
best_sum = 0

max_v = 10**6


def check_lower(c, c_s, b_s):
	while c_s > b_s:
		c_s -= c[0]
		c.remove(c[0])
		if is_prime(c_s):
			return c, c_s
	else:
		return c, c_s


for prime in gen_primes():
	if prime < max_v:
		prime_chain.append(prime)
		prime_sum = sum(prime_chain)
		if is_prime(prime_sum):
			if best_sum < prime_sum < max_v:
				best_sum = prime_sum
				print(best_sum, prime_chain)
		else:
			# check_lower
			c, b = check_lower(deepcopy(prime_chain),
			                            deepcopy(prime_sum),
			                            deepcopy(best_sum))
			print(best_sum, b, c)
			if best_sum < b < max_v:
				best_sum = b
				print(best_sum, c)
	else:
		print(prime)
		break


