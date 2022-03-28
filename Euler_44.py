import sys

def get_pentagonal_number():
    n = 1
    while True:
        yield n * (3 * n - 1) / 2
        n += 1

def is_awesome(j, k):
    global max_pentagonal
    global pentagonal_list
    s = j + k
    d = k - j
    while s > max_pentagonal:
        max_pentagonal = pentagonals.__next__()
        pentagonal_list.append(max_pentagonal)
    if s in pentagonal_list:
        print(s)
    if s in pentagonal_list and d in pentagonal_list:
        return d
    return False

pentagonals = get_pentagonal_number()
pentagonal_list = []
max_pentagonal = 0
pentagonal_list.append(pentagonals.__next__())
pentagonal_list.append(pentagonals.__next__())
max_pentagonal = pentagonals.__next__()
min_awesome = 1000000

# for _ in range(1, 10):
#     b = pentagonals.__next__()
#     print(f"{b}")

while True:
    for j in range(0, len(pentagonal_list) - 2):
        for k in range(j, len(pentagonal_list) - 1):
            d = is_awesome(pentagonal_list[j], pentagonal_list[k])
            if d and d < min_awesome:
                min_awesome = d
    max_pentagonal = pentagonals.__next__()
    pentagonal_list.append(max_pentagonal)