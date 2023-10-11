res = 0
while (s := input()) != "Приехали!":
    if "зайка" in s:
        res += 1
print(res)
