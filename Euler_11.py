"""
In the 20 times 20$ grid below,
four numbers along a diagonal line have been marked in red.
The product of these numbers is 26 times 63 times 78 times 14 = 1788696
What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20 times 20 grid?
"""

import os

ROOT_DIR = os.getcwd()
with open(ROOT_DIR + '/data/Euler_11') as f:
	lines = f.readlines()
	grid: list = []
	for line in lines:
		grid.append(list(line[:-1].split()))

a = 4


def check_up(g, row, column, amount):
	if row + 1 >= amount:
		product = 1
		for i in range(amount):
			print(f'{row=}{column=} {g[row-i][column]=}')
			product *= int(g[row-i][column])
		return product
	else:
		return 0


def check_down(g, row, column, amount):
	if row + amount <= len(g):
		product = 1
		for i in range(amount):
			print(f'{row=}{column=} {g[row+i][column]=}')
			product *= int(g[row+i][column])
		return product
	else:
		return 0


def check_left(g, row, column, amount):
	if column + 1 >= amount:
		product = 1
		for i in range(amount):
			print(f'{row=}{column=} {g[row][column-i]=}')
			product *= int(g[row][column-i])
		return product
	else:
		return 0


def check_right(g, row, column, amount):
	if column + amount <= len(g[0]):
		product = 1
		for i in range(amount):
			print(f'{row=}{column=} {g[row-i][column]=}')
			product *= int(g[row][column+i])
		return product
	else:
		return 0


def check_diagonal_l(g, row, column, amount):
	if row + 1 >= amount and column + 1 >= amount:
		product = 1
		for i in range(amount):
			print(f'{row=}{column=} {g[row-i][column-i]=}')
			product *= int(g[row-i][column-i])
		return product
	else:
		return 0


def check_diagonal_r(g, row, column, amount):
	if row + 1 >= amount and column + amount <= len(g[0]):
		product = 1
		for i in range(amount):
			print(f'{row=}{column=} {g[row-i][column+i]=}')
			product *= int(g[row-i][column+i])
		return product
	else:
		return 0


print(len(grid))
print(len(grid[0]))
best_prod = 0


for r_i, r in enumerate(grid):
	for c_i, col in enumerate(r):
		prod_up = check_up(g=grid, row=r_i, column=c_i, amount=a)
		print(f'{prod_up}')
		if prod_up > best_prod:
			best_prod = prod_up
		prod_down = check_down(g=grid, row=r_i, column=c_i, amount=a)
		print(f'{prod_down}')
		if prod_down > best_prod:
			best_prod = prod_down
		prod_left = check_left(g=grid, row=r_i, column=c_i, amount=a)
		print(f'{prod_left}')
		if prod_left > best_prod:
			best_prod = prod_left
		prod_right = check_right(g=grid, row=r_i, column=c_i, amount=a)
		print(f'{prod_right}')
		if prod_right > best_prod:
			best_prod = prod_right
		prod_diagonal_left = check_diagonal_l(g=grid, row=r_i, column=c_i, amount=a)
		print(f'{prod_diagonal_left}')
		if prod_diagonal_left > best_prod:
			best_prod = prod_diagonal_left
		prod_diagonal_right = check_diagonal_r(g=grid, row=r_i, column=c_i, amount=a)
		print(f"{prod_diagonal_right}")
		if prod_diagonal_right > best_prod:
			best_prod = prod_diagonal_right
		print('#' * 20)
print(best_prod)
