from numbers import Number

base10pandigital = ''.join(str(i) for i in range(1, 10))

def is_base10pandigital(n):
    base10pandigital = ''.join(str(i) for i in range(1, 10))
    if isinstance(n, Number):
        n = str(n)
    return ''.join(sorted(n)) == base10pandigital

pandigitals = []

def calculate_pandigital_set(n):


    max = 0
    while True:
        max += 1
        products = [str(x * n) for x in range(1, max + 1)]
        test_number = ''.join(products)
        if len(test_number) > 9:
            return False
        if len(test_number) < 9:
            continue
        if is_base10pandigital(test_number):
            print(f"max: {max}, number: {test_number}")
            pandigitals.append(test_number)
            return True

calculate_pandigital_set(192)
calculate_pandigital_set(9)

n = 1
while len(str(n)) < 9:
    calculate_pandigital_set(n)
    n += 1

print(max(pandigitals))

