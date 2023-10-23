res = {}
while (s := input()) != "":
    for s in s.split():
        if s in res:
            res[s] += 1
        else:
            res[s] = 1
for k, v in res.items():
    print(k, v)
