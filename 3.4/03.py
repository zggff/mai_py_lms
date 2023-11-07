from itertools import count

start, end, step = (float(i) for i in input().split())

for i in count(start, step):
    if i >= end:
        break
    print(f"{i:.2f}")
