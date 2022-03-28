import math
def biggest_devidor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d ==0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans
print(biggest_devidor(600851475143))
print(max(biggest_devidor(600851475143)))