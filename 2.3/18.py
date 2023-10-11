n = int(input())
res = []
d = 2
while n > 1:
    if n % d == 0:
        n //= d
        res.append(d)
    else:
        d += 1
print(*res, sep=" * ")
