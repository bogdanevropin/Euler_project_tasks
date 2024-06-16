listnums = ''
for i in range(1, 500000):
    listnums += str(i)

strlist = list(listnums)
for digit in listnums:
    strlist.append(digit)

print(int(strlist[0])*int(strlist[9])*int(strlist[99])*int(strlist[999])*int(strlist[9999])*int(strlist[99999])*int(strlist[999999]))
