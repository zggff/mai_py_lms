def convert_sum(n: int, base: int) -> int:
    res = 0
    while n > 0:
        res += n % base
        n //= base
    return res


n = int(input())
r = 0
res = 0
for base in range(2, 10 + 1):
    s = convert_sum(n, base)
    if s > r:
        r = s
        res = base
print(res)
