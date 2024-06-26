"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two $2$-digit numbers is 9009 = 91 times 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import math


def polindromes():
    max_polindrom = 0
    for a in range(100,999):
        for b in range(100,999):
            pos = 0
            polindrom = str(a * b)
            all_pos = len(polindrom)
            while pos < (all_pos / 2):
                if polindrom[pos] == polindrom[all_pos - pos -1] and pos < all_pos:
                    pos += 1
                    if pos >= (all_pos / 2) and int(polindrom) > max_polindrom:
                        max_polindrom = int(polindrom)
                else:
                    break

    return max_polindrom
print(polindromes())