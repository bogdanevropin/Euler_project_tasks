l = []
s = '0123456789'
for a in s:
    s0 = s.replace(a, '')
    for b in s0:
        s1 = s.replace(b, '')
        for c in s1:
            s2 = s.replace(c, '')
            for d in s2:
                s3 = s.replace(d, '')
                for e in s3:
                    s4 = s.replace(e, '')
                    for f in s4:
                        s5 = s.replace(f, '')
                        for g in s5:
                            s6 = s.replace(g, '')
                            for h in s6:
                                s7 = s.replace(h, '')
                                for i in s7:
                                    s8 = s.replace(i, '')
                                    for j in s8:
                                        l.append(a + b + c + d + e + f + g + h + i + j)





                                    
print(l[1000000])