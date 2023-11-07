from itertools import product, starmap

n = int(input())
for i in range(1, n + 1):
    print(*starmap(lambda a, b: a * b, product([i], range(1, n + 1))))
