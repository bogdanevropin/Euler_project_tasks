

def solutions_for_perimeter(p):
    max_sides = p // 2
    solutions = set()
    for a in range(1, max_sides):
        for b in range(1, max_sides):
            if (a+b) > p:
                continue
            c2 = a**2 + b**2
            c = c2 ** 0.5
            if c == int(c) and a + b + c == p:
                a, b = min(a, b), max(a, b)
                s = str(a) + ' ' + str(b) + ' ' + str(c)
                solutions.add(s)
    return solutions

#s = solutions_for_perimeter(120)
#print(f"len {len(s)}, {s}")
current_max_solution = 0

for p in range(1, 1001):
    s = solutions_for_perimeter(p)
    if len(s) > current_max_solution:
        current_max_solution = len(s)
        print(f"p = {p} len {len(s)}, {s}")



