import itertools as it

res = it.chain(*[input().split(", ") for _ in range(3)])
for i, v in enumerate(sorted(res), 1):
    print(f"{i}. {v}")
