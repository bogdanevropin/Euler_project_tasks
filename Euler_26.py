numerator = 10**200
snumerator = str(numerator)
lnumerator = len(snumerator)

def find_rep(s):
    l = len(s)
    size = 1
    for start in range(0, l - size):
        end = start + size
        p0 = s[start:end]
        for i in range(end, l - start):
            p1 = s[i:i+len(p0)]
            if p0 != p1:
                break
        else:
            return p0
    return 'none'




    return '0'

def precision_devide(denominator):
    result = str(numerator // denominator)
    padding = '0' * (lnumerator - len(result) - 1)
    rep = find_rep(result)
    result = result.replace(rep, '')

    return '0.' + padding + result + ' len(rep) = ' + str(len(rep))



for d in range(2, 100):
    print(f'1/{d} = {precision_devide(d)}')