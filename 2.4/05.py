N = int(input())
r = 0
for i in range(N):
    hare = False
    while (s := input()) != "ВСЁ":
        if s == "зайка":
            hare = True
    if hare:
        r += 1
print(r)
