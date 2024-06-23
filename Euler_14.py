"""
The following iterative sequence is defined for the set of positive integers:
n to n/2$ ($n$ is even)
n \to 3n + 1$ ($n$ is odd)
Using the rule above and starting with $13$, we generate the following sequence:
13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1.
It can be seen that this sequence (starting at $13$ and finishing at $1$)
contains $10$ terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at $1$.
Which starting number, under one million, produces the longest chain?
Once the chain starts the terms are allowed to go above one million.
"""

chained_nums = {1: 1}


def even_rule(num):
	return num // 2


def odd_rule(num):
	return 3 * num + 1


def evaluate_chain(num):
	global chained_nums
	start = num
	terms = 1
	while num != 1 and num not in chained_nums:
		if num % 2 == 0:
			num = even_rule(num)
		else:
			num = odd_rule(num)
		terms += 1
	chained_nums[start] = terms + chained_nums[num] - 1
	return chained_nums[start]
	

print(evaluate_chain(40))
print(evaluate_chain(13))
print(chained_nums)
max_length = 1
best_num = 1
for n in range(1, 10**6):
	length = evaluate_chain(n)
	if length > max_length:
		max_length = length
		best_num = n
print(best_num)
