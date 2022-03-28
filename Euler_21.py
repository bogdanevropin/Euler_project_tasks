
def sum_devisors(n):
    sum = 0
    for dev in range(1,n):
        if n % dev == 0:
            sum += dev
    return sum

def find_pair(max):
    summa = 0
    for num in range(1, max + 1):
        if sum_devisors(num) < max and sum_devisors(sum_devisors(num)) == num and sum_devisors(num) != num:
            summa += num
            print(summa)
    return summa

print(find_pair(10000))