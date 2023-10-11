N = int(input())
res = 0
for _ in range(N):
    n = int(input())
    if n < 2:
        continue
    if n < 4:
        res += 1
        continue
    if n % 2 == 0:
        continue
    is_prime = True
    for d in range(3, n, 2):
        if n % d == 0:
            is_prime = False
            break
    if is_prime:
        res += 1
print(res)
