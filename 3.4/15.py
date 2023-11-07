# Список покупок 3.0
import itertools as it

n = int(input())
opts = it.chain(*[input().split(', ') for _ in range(n)])
for o in sorted(it.permutations(opts, 3)):
    print(*o)
