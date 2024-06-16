import os
from math import ceil

ROOT_DIR = os.getcwd()


def check_prime(p, value):
    import json
    try:
        # Define the file path
        file_path = os.path.join(ROOT_DIR, 'primes.json')
        # Read the existing JSON data
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
        else:
            data = {}
        # Ensure 'data' is a dictionary
        if not isinstance(data, dict):
            data = {}
        # Add the new prime if it is not already in the data
        str_p = str(p)
        if str_p not in data:
            data[str_p] = str(value)
        # Write the updated data back to the JSON file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"An error occurred: {e}")


def is_prime(num: int,
             cache: dict = {2: True},
             write: bool = False) -> bool | None:
    if num < 1:
        return None
    if num == 1:
        return False
    if num in cache:
        return cache[num]

    if num % 2 == 0:
        cache[num] = False
        # if write:
        #     check_prime(num, False)
        return False

    top = int(ceil(num ** 0.5))
    for y in range(3, top + 1, 2):
        if num % y == 0:
            cache[num] = False
            # if write:
            #     check_prime(num, False)
            return False
    cache[num] = True
    # if write:
    #     check_prime(num, True)
    return True


def gen_primes() -> int:
    yield 2
    num = 3
    while True:
        yield num
        num += 2
        while not is_prime(num):
            num += 2


def dividers(num: int) -> list:
    ans: list = []
    d = 2
    while d * d <= num:
        if num % d == 0:
            ans.append(d)
            num //= d
        else:
            d += 1
    if num > 1:
        ans.append(num)
    return ans


def prime_factors_list(n: int) -> list:
    factors: list = []
    while n % 2 == 0:
        factors.append(2)
        n /= 2
    for p in range(3, int(n + 1), 2):
        if n % p == 0 and is_prime(p):
            factors.append(p)
    return factors


def nth_prime_old(num):
    counter = 2
    for i in range(3, num**2, 2):
        k = 1
        while k*k < i:
            k += 2
            if i % k == 0:
                break
        else:
            counter += 1
        if counter == num:
            return i


def n_primes(n: int) -> list:
    prime_list: list = []
    for p in gen_primes():
        # print(p)
        prime_list.append(p)
        if len(prime_list) == n:
            return prime_list


def primes_below_n(n: int) -> list:
    prime_list: list = []
    for p in gen_primes():
        if p >= n:
            return prime_list
        prime_list.append(p)


def nth_prime(num: int | str) -> int:
    n = 0
    for p in gen_primes():
        n += 1
        if n == num:
            return p


def prime_factors_dict(n: int) -> dict:
    from copy import deepcopy
    factors: dict = {}
    while n % 2 == 0:
        if 2 not in factors:
            factors[2] = 1
        else:
            factors[2] = factors[2] + 1
        n /= 2
    current_n = deepcopy(n)
    for p in range(3, int(n + 1), 2):
        if n % p == 0 and is_prime(p):
            if p not in factors:
                factors[p] = 1
            else:
                factors[p] = factors[p] + 1
            current_n /= p
            while current_n % p == 0:
                factors[p] = factors[p] + 1
                current_n /= p
    return factors


# if __name__ == '__main__':
    # print(nth_prime(10001))
    # print(nth_prime_old(10001))
#     max_v = 10**6
#     for n in range(2, max_v):
#         print(is_prime(n))
#     else:
#         is_prime(max_v + 1, write=True)
