from itertools import permutations

if __name__ == '__main__':
    for p in permutations('123456789', 9):
        p = ''.join(p)
        for a in range(1, 6):
            for b in range(a, 6):
                anum = int(p[0:a+1])
                bnum = int(p[a+1:b+1])
                pnum = int(p[b+1:])
                print(anum, bnum, pnum)
                if anum * bnum == pnum:
                    print(anum, bnum, pnum)