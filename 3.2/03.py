res = set()
for _ in range(int(input())):
    res = res.union(input().split())
for r in res:
    print(r)
