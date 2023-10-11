N = int(input())
a = int(input())
for _ in range(N - 1):
    b = int(input())
    while (r := b % a) > 0:
        b = a
        a = r
print(a)
