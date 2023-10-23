n = int(input())
res = {}
for _ in range(n):
    s = input().split()
    for t in s[1:]:
        if t in res:
            res[t].append(s[0])
        else:
            res[t] = [s[0]]
t = input()
if t in res:
    for name in sorted(res[t]):
        print(name)
else:
    print("Таких нет")
