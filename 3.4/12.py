# Список покупок 2.0
import itertools as it

res = it.chain(*[input().split(", ") for _ in range(int(input()))])
for i, v in enumerate(sorted(res), 1):
    print(f"{i}. {v}")
