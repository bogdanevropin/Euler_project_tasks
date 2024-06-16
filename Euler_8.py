"""
The four adjacent digits in the
1000 -digit number that have the greatest product are 9*9*8*9=5832


Find the thirteen adjacent digits in the
1000-digit number that have the greatest product.
What is the value of this product?
"""
import os

slice_size = 13

ROOT_DIR = os.getcwd()

with open(ROOT_DIR + '/data/Euler_8') as f:
	lines = f.readlines()
	s = ''
	for line in lines:
		s += line[:-1]

product = 1
best_product = 1
for index in range(len(s) - 3):
	product = 1
	for digit in s[index: index + slice_size]:
		product *= int(digit)
	if product > best_product:
		best_product = product
print(best_product)
