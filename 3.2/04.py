n = int(input())
m = int(input())

a = set([input() for _ in range(n)])
b = set([input() for _ in range(m)])
c = a.intersection(b)
if len(c) == 0:
    print("Таких нет")
else:
    print(len(c))
