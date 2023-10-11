n = list(input())
res = []
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        r = int(n[i] + n[j])
        if r >= 10:
            res.append(r)
res.sort()
print(res[0], res[-1])
