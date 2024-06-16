"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 times 99.
Find the largest palindrome made from the product of two $3$-digit numbers.
"""

from tools.Palindrome import check_palindrome
max_v = 1000
p = 0
for n1 in range(100, max_v):
	for n2 in range(100, max_v):
		new = n1 * n2
		if new > p:
			if check_palindrome(str(new)):
				p = new

print(p)
