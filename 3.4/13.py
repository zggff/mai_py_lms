import itertools as it

people = [input() for _ in range(int(input()))]
for a in sorted(it.permutations(people)):
    print(*a, sep=', ')
