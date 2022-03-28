def conv_bin(num):
    return format(num, 'b')

def is_pal(string):
    return string == string[::-1]

vals = list(range(1000000))

pairs = {x: conv_bin(x) for x in vals}

good_ones = {}

for k, v in pairs.items():
    if is_pal(str(k)) and is_pal(str(v)):
        good_ones[k] = v

print(f'{sum(list(map(int, list(good_ones.keys()))))}')

