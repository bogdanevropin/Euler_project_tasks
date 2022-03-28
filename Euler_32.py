s = ''.join(str(i) for i in range(1, 10))

def is_pandigital(a, b, c):
    test = str(a) + str(b) + str(c)
    return ''.join(sorted(test)) == s



if __name__ == '__main__':
    products = {}
    count = 0
    for x1 in range(1, 10000):
        for x2 in range(1, 1000):
            if is_pandigital(x1, x2, x1*x2):
                products[str(x1*x2)] = str(x1) + ' * ' + str(x2)
    print(products)
    pandigital_product = 1
    for pandigital in products:
        pandigital_product *= int(pandigital)

    print(sum(int(key) for key in products))

    print(pandigital_product)


