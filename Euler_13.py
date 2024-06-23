"""
Work out the first ten digits of the sum of the following one-hundred
50-digit numbers.
"""

import os

ROOT_DIR = os.getcwd()
with open(ROOT_DIR + '/data/Euler_13') as f:
	lines = f.readlines()
	grid: list = []
	for line in lines:
		grid.append(list(line[:-1].split()))

s = 0
for row in grid:
	for digit in row:
		s += int(digit)

print(str(s)[:10])
