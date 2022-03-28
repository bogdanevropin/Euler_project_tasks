from itertools import permutations
from itertools import combinations

s = '0123456789'

def permute(s):
    if len(s) == 1:
        return [s]
    data = []

    for l in s:
        s0 = s.replace(l,'')
        s1 = permutate(s0)
        for partial in s1:
            data.append(l+partial)

    return data


def is_awesome(num):
    if num[0] == '0':
        return False

    if len(num) < 10:
        return False

    if int(num[7:10]) % 17 == 0:
        if int(num[6:9]) % 13 == 0:
            if int(num[5:8]) % 11 == 0:
                if int(num[4:7]) % 7 == 0:
                    if int(num[3:6]) % 5 == 0:
                        if int(num[2:5]) % 3 == 0:
                            if int(num[1:4]) % 2 == 0:
                                return True

all_base10_pandigitals = permutations('0123456789', 10)
awesome = []
for i in all_base10_pandigitals:
    num = ''.join(i)
    if is_awesome(num):
        awesome.append(num)
        print(num)
summa = str(sum(int(num) for num in awesome))
print(f"sum:", summa)