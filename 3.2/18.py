n = int(input())
res = {}
for _ in range(n):
    x, y = input().split()
    s = (x[:-1], y[:-1])
    if s in res:
        res[s] += 1
    else:
        res[s] = 1
print(max(res.values()))
