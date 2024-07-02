n = 1
for i in range(1, 101):
    n *= i
sum = 0
for digit in str(n):
    sum += int(digit)
print(sum)
