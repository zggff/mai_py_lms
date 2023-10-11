from math import sqrt

a = float(input())
b = float(input())
c = float(input())

res = []
if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif a == 0 and b == 0:
    print("No solution")
elif c == 0:
    res = [0, -b / a]
elif a == 0:
    res = [-c / b]
elif b == 0:
    sq = -c / a
    if sq < 0:
        print("No solution")
    elif sq == 0:
        res = [0]
    else:
        r = sqrt(sq)
        res = [-r, r]
else:
    D = b * b - 4 * a * c
    if D < 0:
        print("No solution")
    elif D == 0:
        res = [-b / (2 * a)]
    else:
        d = sqrt(D)
        res = [(-b - d) / (2 * a), (-b + d) / (2 * a)]

for r in sorted(res):
    print(f"{r:0.2f}", end=" ")
if len(res) > 0:
    print()
