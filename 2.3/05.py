res = 0.0
while (s := float(input())) > 0:
    if s >= 500:
        s *= 0.9
    res += s
print(res)
