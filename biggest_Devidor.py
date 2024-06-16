import math


def biggest_devidor(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d ==0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    return ans


print(biggest_devidor(600851475143))
print(max(biggest_devidor(600851475143)))
