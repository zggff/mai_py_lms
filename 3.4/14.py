# Спортивные гадания
import itertools as it

people = [input() for _ in range(int(input()))]
for a in sorted(it.permutations(people, 3)):
    print(*a, sep=', ')
