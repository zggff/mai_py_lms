a = input()
for i in range(len(a) // 2):
    if a[i] != a[-i - 1]:
        print("NO")
        exit()
print("YES")
