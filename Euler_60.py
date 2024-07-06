from itertools import permutations
from tools.Primes import is_prime


def concat_check(primes: list):
    """
    We take list of primes and check for concat them
    """
    concat_new = []
    for index1, p1 in enumerate(primes[:-4]):
        for index2, p2 in enumerate(primes[index1+1:-3]):
            for index3, p3 in enumerate(primes[index2+2:-2]):
                for index4, p4 in enumerate(primes[index3+3:-1]):
                    for p5 in primes[index4+4:]:
                        five_primes = [p1, p2, p3, p4]
                        s = False
                        for index, prime1 in enumerate(five_primes[:-1]):
                            if s:
                                break
                            for prime2 in five_primes[index+1:]:
                                # print(prime1, prime2)
                                if not is_prime(int(str(prime1) + str(prime2))):
                                    s = True
                                    break
                                if not is_prime(int(str(prime2) + str(prime1))):
                                    s = True
                                    break
                        else:
                            concat_new.append(five_primes)
    return concat_new


def choose_four_primes(primes: list):
    all_fourth: list = []
    primes_amount = len(primes)
    for index1 in range(primes_amount - 3):
        for index2 in range(index1 + 1, primes_amount - 2):
            for index3 in range(index2 + 1, primes_amount - 1):
                for index4 in range(index3 + 1, primes_amount):
                    all_fourth.append([primes[index1], primes[index2], primes[index3], primes[index4]])
    return all_fourth


def choose_three_primes(primes: list):  # COULD BE MADE BY RECURSION AND SLICES
    all_threes: list = []
    primes_amount = len(primes)
    for index1 in range(primes_amount - 2):
        for index2 in range(index1 + 1, primes_amount - 1):
            for index3 in range(index2 + 1, primes_amount):
                all_threes.append([primes[index1], primes[index2], primes[index3]])
    return all_threes


def concat_check_add(primes: list, prime: int):
    for p in primes:
        if not is_prime(int(str(p) + str(prime))):
            return False
        if not is_prime(int(str(prime) + str(p))):
            return False
    return True


lowest_sum: None | int = None
all_primes = [3, 5, 7, 11, 13, 17, 19]
new_num = 19
stop = False


while not stop:
    new_num += 2
    if lowest_sum is not None and lowest_sum < new_num:
        print(new_num)
        stop = True
    if is_prime(new_num):  # Check new prime
        all_threes = choose_three_primes(primes=all_primes)
        print(new_num)
        if new_num == 673:
            print()
        for three in all_threes:
            if three == [3, 7, 109] and new_num == 673:
                breakpoint()
            if concat_check_add(primes=three, prime=new_num):
                new_sum = sum(three, new_num)
                if lowest_sum is None or lowest_sum > new_sum:
                    lowest_sum = new_sum
        all_primes.append(new_num)

print(lowest_sum)
