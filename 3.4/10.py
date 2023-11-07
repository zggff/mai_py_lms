from itertools import product

n = int(input())
print("А Б В")
res = [a for a in product(range(1, n - 1), repeat=3) if sum(a) == n]
for r in res:
    print(*r)
