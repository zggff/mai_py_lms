n = int(input())
i = 1
j = 1
while i <= n:
    for _ in range(j):
        if i > n:
            break
        print(i, end=' ')
        i += 1
    print()
    j += 1
