toys = {}
for _ in range(int(input())):
    line = input().split(': ')[1]
    line = set(line.split(', '))
    for t in line:
        if t in toys:
            toys[t] += 1
        else:
            toys[t] = 1
for t in sorted([k for k, v in toys.items() if v == 1]):
    print(t)
