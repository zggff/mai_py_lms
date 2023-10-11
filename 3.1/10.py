res = {}
while (s := input()) != "ФИНИШ":
    for c in s.lower():
        if c.isspace():
            continue
        if ord(c) in res:
            res[ord(c)] += 1
        else:
            res[ord(c)] = 1

r_key = ''
r_val = 0
for k, v in res.items():
    if v > r_val:
        r_key = chr(k)
        r_val = v
print(r_key)
