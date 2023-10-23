n = int(input())
m = int(input())

a = set()
for _ in range(n + m):
    s = input()
    if s in a:
        a.remove(s)
    else:
        a.add(s)

if len(a) == 0:
    print("Таких нет")
else:
    print(len(a))
