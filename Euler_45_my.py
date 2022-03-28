def get_triangular_number():
    n = 1
    while True:
        yield n * (n + 1) / 2
        n += 1

def get_pentagonal_number():
    n = 1
    while True:
        yield n * (3 * n - 1) / 2
        n += 1

def get_hexagonal_number():
    n = 1
    while True:
        yield n * (2 * n - 1)
        n += 1

triangulars = get_triangular_number()
triangular_list = []
pentagonals = get_pentagonal_number()
pentagonal_list = []
hexagonals = get_hexagonal_number()
hexagonal_list = []

for i in range(1, 100000):
    triangular_list.append(triangulars.__next__())
    pentagonal_list.append(pentagonals.__next__())
    hexagonal_list.append(hexagonals.__next__())

for item in triangular_list:
    if item in pentagonal_list and item in hexagonal_list:
        print(item)