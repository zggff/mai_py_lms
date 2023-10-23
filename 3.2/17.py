first = {}
while (s := input()) != "":
    [a, b] = s.split()
    if b in first:
        first[b].append(a)
    else:
        first[b] = [a]

    if a in first:
        first[a].append(b)
    else:
        first[a] = [b]

for k in sorted(first.keys()):
    res = set()
    for a in first[k]:
        for b in first[a]:
            if b != k and b not in first[k]:
                res.add(b)
    res = ", ".join(sorted(res))
    print(f"{k}: {res}")
