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

initial = 200000

triangulars = get_triangular_number()
triangular_list = []
pentagonals = get_pentagonal_number()
pentagonal_list = []
hexagonals = get_hexagonal_number()
hexagonal_list = []

last_triangular = next(triangulars)
last_pentagonal = next(triangulars)
last_hexagonal = next(triangulars)

while last_triangular <= initial:
    last_triangular = next(triangulars)
while last_pentagonal <= initial:
    last_pentagonal = next(pentagonals)
while last_hexagonal <= initial:
    last_hexagonal = next(hexagonals)

while last_triangular != last_pentagonal != last_hexagonal:
    if last_triangular < last_pentagonal or last_triangular < last_hexagonal:
        last_triangular = next(triangulars)
        continue

    if last_pentagonal < last_triangular or last_pentagonal < last_hexagonal:
        last_pentagonal = next(pentagonals)
        continue

    if last_hexagonal < last_pentagonal or last_hexagonal < last_triangular:
        last_hexagonal = next(hexagonals)
        continue

print(last_triangular)
