res = set()
while (s := input()) != "":
    s = list(s.split())
    for i in range(0, len(s)):
        if s[i] != "зайка":
            continue
        if i > 0:
            res.add(s[i - 1])
        if i < len(s) - 1:
            res.add(s[i + 1])

for r in res:
    print(r)
