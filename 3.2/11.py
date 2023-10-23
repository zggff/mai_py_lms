n = int(input())
res = {}
for _ in range(n):
    s = input()
    if s in res:
        res[s] += 1
    else:
        res[s] = 1
r = 0
for v in res.values():
    if v > 1:
        r += v
print(r)
