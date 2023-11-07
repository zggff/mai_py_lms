import itertools as it

options = it.cycle([input() for _ in range(int(input()))])
for val in it.islice(options, int(input())):
    print(val)
