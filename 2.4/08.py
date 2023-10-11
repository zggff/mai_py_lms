N = int(input())
r = 0
res = ""
for _ in range(N):
    name = input()
    n = sum([int(i) for i in input()])
    if n >= r:
        r = n
        res = name
print(res)
