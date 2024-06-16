def gen_list_fibonnaci(n, fib_l: list = [1, 1]):
	while len(fib_l) < n + 1:
		f1 = fib_l[-1]
		f2 = fib_l[-2]
		fib_l.append(f1+f2)
	return fib_l[n], fib_l


def gen_fibonacci():
	f1 = 1
	f2 = 1
	yield f1
	yield f2
	while True:
		yield f1 + f2
		f2 = f1 + f2
		f1 = f2 - f1
