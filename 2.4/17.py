N = int(input())
res = 0
for _ in range(N):
    a = input()
    for i in range(len(a) // 2):
        if a[i] != a[-i - 1]:
            break
    else:
        res += 1
print(res)
