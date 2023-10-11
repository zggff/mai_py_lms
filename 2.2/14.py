a = input()
b = input()
c = input()
for i in range(2):
    if a[i] == b[i] and b[i] == c[i]:
        print(a[i])
        break
