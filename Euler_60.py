"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order
the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

"""

# from itertools import permutations
from tools.Primes import is_prime


# def concat_check(primes: list):
#     """
#     We take list of primes and check for concat them
#     """
#     concat_new = []
#     for index1, p1 in enumerate(primes[:-4]):
#         for index2, p2 in enumerate(primes[index1+1:-3]):
#             for index3, p3 in enumerate(primes[index2+2:-2]):
#                 for index4, p4 in enumerate(primes[index3+3:-1]):
#                     for p5 in primes[index4+4:]:
#                         five_primes = [p1, p2, p3, p4]
#                         s = False
#                         for index, prime1 in enumerate(five_primes[:-1]):
#                             if s:
#                                 break
#                             for prime2 in five_primes[index+1:]:
#                                 # print(prime1, prime2)
#                                 if not is_prime(int(str(prime1) + str(prime2))):
#                                     s = True
#                                     break
#                                 if not is_prime(int(str(prime2) + str(prime1))):
#                                     s = True
#                                     break
#                         else:
#                             concat_new.append(five_primes)
#     return concat_new


# compatible_two = []
# compatible_three = []
# compatible_four = []
#
# compatible = {}
#
#
# def choose_four_primes(primes: list, new_prime: int):
#     all_fourth: list = []
#     primes_amount = len(primes)
#     for index1 in range(primes_amount - 3):
#         if concat_check(primes[index1], new_prime):
#             compatible_two.append((primes[index1], new_prime))
#             for index2 in range(index1 + 1, primes_amount - 2):
#                 if concat_check_list_tuple((primes[index1], primes[index1], new_prime)):
#                     compatible_three.append((primes[index1], primes[index1], new_prime))
#                 two = (primes[index1], primes[index2])
#                 if two in compatible_two:
#                     for index3 in range(index2 + 1, primes_amount - 1):
#                         if concat_check_list_tuple()
#                         three = (primes[index1], primes[index2], primes[index3])
#                         if three in compatible_three:
#                             for index4 in range(index3 + 1, primes_amount):
#                                 new_four = (primes[index1], primes[index2], primes[index3], primes[index4])
#                                 if new_four not in compatible_four:
#                                     res = concat_check(new_four)
#                                     compatible_four[new_four] = res
#                                 if compatible_four[new_four]:  # This four primes compatible
#                                     all_fourth.append([primes[index1], primes[index2], primes[index3],
#                                     primes[index4]])
#     return all_fourth
#
#
# # def choose_three_primes(primes: list):  # COULD BE MADE BY RECURSION AND SLICES
# #     all_threes: list = []
# #     primes_amount = len(primes)
# #     for index1 in range(primes_amount - 2):
# #         for index2 in range(index1 + 1, primes_amount - 1):
# #             for index3 in range(index2 + 1, primes_amount):
# #                 all_threes.append([primes[index1], primes[index2], primes[index3]])
# #     return all_threes
#
# def concat_check(p1: int, p2: int):
#     return is_prime(int(str(p1) + str(p2))) and is_prime(int(str(p2) + str(p1)))
#
#
# def concat_check_list_tuple(primes: list | tuple) -> bool:
#     for index, p1 in enumerate(primes[:-1]):
#         for p2 in primes[index+1:]:
#             if not is_prime(int(str(p1) + str(p2))):
#                 return False
#             if not is_prime(int(str(p2) + str(p1))):
#                 return False
#     return True
#
#
# lowest_sum: None | int = None
# best_four = None
# all_primes = [3, 5, 7, 11, 13, 17, 19]
# new_num = 19
# stop = False
#
#
# while not stop:
#     new_num += 2
#     if lowest_sum is not None and lowest_sum < new_num:
#         print(new_num)
#         stop = True
#     if is_prime(new_num):  # Check new prime
#         if new_num > 673:
#             all_fours = choose_four_primes(primes=all_primes, new_prime=new_num)
#             print(new_num)
#             for four in all_fours:
#                 five_primes = four
#                 five_primes.append(new_num)
#                 if concat_check_list_tuple(primes=five_primes):
#                     new_sum = sum(five_primes)
#                     if lowest_sum is None or lowest_sum > new_sum:
#                         lowest_sum = new_sum
#                         best_five = five_primes
#                         # best_four.append(new_num)
#                         print(lowest_sum, best_five)
#         all_primes.append(new_num)
#
# print(lowest_sum, best_four)

lowest_sum: None | int = None
best_five = None
all_primes = [3, 5, 7, 11]
new_num = 19
stop = False

compatible = {
    2: [(3, 7), (3, 11)],
    3: [],
    4: []
}


def concat_check(p1: int, p2: int):
    return is_prime(int(str(p1) + str(p2))) and is_prime(int(str(p2) + str(p1)))


def concat_check_full(primes: list | tuple) -> bool:
    for index, p1 in enumerate(primes[:-1]):
        for p2 in primes[index+1:]:
            if not is_prime(int(str(p1) + str(p2))):
                return False
            if not is_prime(int(str(p2) + str(p1))):
                return False
    return True


def create_new_five(primes: list, new_prime):
    primes_amount = len(primes)
    fives = []
    for index1 in range(primes_amount - 3):
        if concat_check(primes[index1], new_prime):
            compatible[2].append((primes[index1], new_prime))
            for index2 in range(index1 + 1, primes_amount - 2):
                if concat_check_full((primes[index1], primes[index2], new_prime)):
                    compatible[3].append((primes[index1], primes[index2], new_prime))
                two = (primes[index1], primes[index2])
                if two in compatible[2]:
                    for index3 in range(index2 + 1, primes_amount - 1):
                        if concat_check_full((primes[index1], primes[index2], primes[index3], new_prime)):
                            compatible[4].append((primes[index1], primes[index2], primes[index3], new_prime))
                        three = (primes[index1], primes[index2], primes[index3])
                        if three in compatible[3]:
                            for index4 in range(index3 + 1, primes_amount):
                                four = (primes[index1], primes[index2], primes[index3], primes[index4])
                                if four in compatible[4]:
                                    if concat_check_full((primes[index1], primes[index2], primes[index3],
                                                          primes[index4], new_prime)):
                                        fives.append((primes[index1], primes[index2], primes[index3], primes[index4],
                                                      new_prime))
    return fives


while not stop:
    new_num += 2
    if lowest_sum is not None and lowest_sum < new_num:
        print(new_num)
        stop = True
    if is_prime(new_num):  # Check new prime
        for f in create_new_five(primes=all_primes, new_prime=new_num):
            new_sum = sum(f)
            if lowest_sum is None or lowest_sum > new_sum:
                lowest_sum = new_sum
                best_five = f
                print(lowest_sum, best_five)

print(lowest_sum, best_five)
