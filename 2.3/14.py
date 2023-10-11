n = int(input())
if n < 2:
    print("NO")
    exit()
if n < 4:
    print("YES")
    exit()
if n % 2 == 0:
    print("NO")
    exit()
for d in range(3, n, 2):
    if n % d == 0:
        print("NO")
        exit()
print("YES")
