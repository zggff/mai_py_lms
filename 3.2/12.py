n = int(input())
res = {}
for _ in range(n):
    s = input()
    if s in res:
        res[s] += 1
    else:
        res[s] = 1
res = {k: v for k, v in res.items() if v > 1}
if len(res) == 0:
    print("Однофамильцев нет")
else:
    for k in sorted(res.keys()):
        print(f"{k} - {res[k]}")
