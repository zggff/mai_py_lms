ns = sorted(set([int(i) for i in input().split("; ")]))
primes = [2]
for i in range(3, ns[-1] + 1):
    for prime in primes:
        if i % prime == 0:
            break
    else:
        primes.append(i)

for n in ns:
    res = []
    for k in ns:
        if n == k:
            continue
        for prime in primes:
            if n % prime == 0 and k % prime == 0:
                break
        else:
            res.append(k)
    if len(res) == 0:
        continue
    res = ", ".join(map(str, res))
    print(f"{n} - {res}")
